"""Streamlit app that counts word frequency from user-provided phrases."""

import streamlit as st
from collections import Counter
import re

# Display the title of the page
st.title("Keyword Wortzähler")

# Show an input area for phrases, one per line
st.write("Füge deine Keyword-Phrasen unten ein (eine Phrase pro Zeile):")
phrases_input = st.text_area("Phrasen", height=200, key="phrases_input")

# Optional prefix to put in front of each keyword in the result
prefix = st.text_input(
    "Präfix vor jedem Keyword (optional)",
    value="",
    key="prefix",
)

if st.button("Fenster zurücksetzen"):
    st.session_state.phrases_input = ""
    st.session_state.prefix = ""
    st.session_state.hide_counts = False

if "hide_counts" not in st.session_state:
    st.session_state.hide_counts = False

if phrases_input:
    # Convert all phrases into individual words
    words = []
    for line in phrases_input.splitlines():
        line_words = re.findall(r"\b\w+\b", line.lower())
        words.extend(line_words)

    # Count how often each word appears
    word_counts = Counter(words)

    # Sort words by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Prepare the text for display with and without counts
    with_counts = [f"{prefix}{word} ({count})" for word, count in sorted_words]
    without_counts = [f"{prefix}{word}" for word, _ in sorted_words]

    if st.session_state.hide_counts:
        result_text = "\n".join(without_counts)
    else:
        result_text = "\n".join(with_counts)

    st.write("**Wörter nach Häufigkeit:**")
    st.text_area("Ergebnis", result_text, height=200, key="result_text")

    if not st.session_state.hide_counts:
        if st.button("Zahlen entfernen"):
            st.session_state.hide_counts = True

    st.download_button(
        label="Ergebnis herunterladen",
        data=result_text,
        file_name="wortliste.txt",
        mime="text/plain",
    )
else:
    # Ask the user to provide phrases if the input is empty
    st.write("Gib oben Phrasen ein, um die Wortzählung zu sehen.")
