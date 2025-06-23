import streamlit as st
from collections import Counter
import re

# --- App Title ---
st.title("🔤 Keyword Wortzähler")

# --- Reset Button ---
reset = st.button("🔄 Fenster zurücksetzen")
if reset:
    # Session State auf Anfangswerte setzen und Seite neu laden
    for k in ["phrases_input", "prefix", "hide_counts", "result_text"]:
        if k in st.session_state:
            del st.session_state[k]
    st.rerun()

# --- Eingabefelder ---
st.write("Füge deine Keyword-Phrasen unten ein (eine Phrase pro Zeile):")
phrases_input = st.text_area(
    "Phrasen",
    height=200,
    key="phrases_input",
    value=st.session_state.get("phrases_input", "")
)

prefix = st.text_input(
    "Präfix vor jedem Keyword (optional)",
    value=st.session_state.get("prefix", ""),
    key="prefix"
)

# --- Umschalter für Zählung anzeigen/verstecken ---
hide_counts = st.checkbox(
    "Zählungen ausblenden",
    value=st.session_state.get("hide_counts", False),
    key="hide_counts"
)

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

    result_text = "\n".join(without_counts if hide_counts else with_counts)
    st.session_state["result_text"] = result_text

    st.write("**Wörter nach Häufigkeit:**")
    st.text_area("Ergebnis", result_text, height=200)

    st.download_button(
        label="⬇️ Ergebnis herunterladen",
        data=result_text,
        file_name="wortliste.txt",
        mime="text/plain",
    )
else:
    st.write("Gib oben Phrasen ein, um die Wortzählung zu sehen.")
