"""Streamlit app that counts word frequency from user-provided phrases."""

import streamlit as st
from collections import Counter

# Display the title of the page
st.title("Keyword Wortzähler")

# Show an input area for phrases, one per line
st.write("Füge deine Keyword-Phrasen unten ein (eine Phrase pro Zeile):")
phrases_input = st.text_area("Phrasen", height=200)

if phrases_input:
    # Convert all phrases into individual words
    words = []
    for line in phrases_input.splitlines():
        line_words = line.split()
        words.extend(line_words)

    # Count how often each word appears
    word_counts = Counter(words)

    # Sort words by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Prepare the text for display
    result_lines = [f"{word} ({count})" for word, count in sorted_words]
    result_text = "\n".join(result_lines)

    st.write("**Wörter nach Häufigkeit:**")
    st.text_area("Ergebnis", result_text, height=200)
else:
    # Ask the user to provide phrases if the input is empty
    st.write("Gib oben Phrasen ein, um die Wortzählung zu sehen.")
