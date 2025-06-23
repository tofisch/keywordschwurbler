"""Streamlit app that counts word frequency from user-provided phrases."""

import streamlit as st
from collections import Counter
import re

# --- Session State Setup ---
if "phrases_input" not in st.session_state:
    st.session_state.phrases_input = ""

if "prefix" not in st.session_state:
    st.session_state.prefix = ""

if "hide_counts" not in st.session_state:
    st.session_state.hide_counts = False

if "result_text" not in st.session_state:
    st.session_state.result_text = ""

# --- App Title ---
st.title("🔤 Keyword Wortzähler")

# --- Eingabefelder ---
st.write("Füge deine Keyword-Phrasen unten ein (eine Phrase pro Zeile):")
phrases_input = st.text_area("Phrasen", height=200, key="phrases_input")

prefix = st.text_input(
    "Präfix vor jedem Keyword (optional)", 
    value=st.session_state.prefix, 
    key="prefix"
)

# --- Reset Button ---
if st.button("🔄 Fenster zurücksetzen"):
    st.session_state.phrases_input = ""
    st.session_state.prefix = ""
    st.session_state.hide_counts = False
    st.session_state.result_text = ""

# --- Verarbeitung ---
if phrases_input:
    words = []
    for line in phrases_input.splitlines():
        line_words = re.findall(r"\b\w+\b", line.lower())
        words.extend(line_words)

    word_counts = Counter(words)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    with_counts = [f"{prefix}{word} ({count})" for word, count in sorted_words]
    without_counts = [f"{prefix}{word}" for word, _ in sorted_words]

    result_text = "\n".join(without_counts if st.session_state.hide_counts else with_counts)
    st.session_state.result_text = result_text

    st.write("**Wörter nach Häufigkeit:**")
    st.text_area("Ergebnis", result_text, height=200)

    # --- Umschalter für Zählung anzeigen/verstecken ---
    st.session_state.hide_counts = st.checkbox(
        "Zählungen ausblenden", 
        value=st.session_state.hide_counts
    )

    st.download_button(
        label="⬇️ Ergebnis herunterladen",
        data=result_text,
        file_name="wortliste.txt",
        mime="text/plain",
    )
else:
    st.write("Gib oben Phrasen ein, um die Wortzählung zu sehen.")
