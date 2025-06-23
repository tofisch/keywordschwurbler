import streamlit as st
from collections import Counter
import re

st.title("Keyword Wortzähler")

st.write("Füge deine Keyword-Phrasen unten ein (eine Phrase pro Zeile):")
phrases_input = st.text_area("Phrasen", height=200)

if phrases_input:
    # Split input into lines and extract words using regex
    words = []
    for line in phrases_input.splitlines():

        line_words = re.findall(r"\b\w+\b", line.lower())

        line_words = [w.lower() for w in line.split()]

        words.extend(line_words)

    # Count word frequency
    word_counts = Counter(words)

    # Sort words by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Prepare result text
    result_lines = [f"{word} ({count})" for word, count in sorted_words]
    result_text = "\n".join(result_lines)

    st.write("**Wörter nach Häufigkeit:**")
    st.text_area("Ergebnis", result_text, height=200)
else:
    st.write("Gib oben Phrasen ein, um die Wortzählung zu sehen.")
