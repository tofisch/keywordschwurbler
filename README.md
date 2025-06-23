# 🧠 Keywordschwurbler

**Keywordschwurbler** ist eine kleine Streamlit-App, die aus benutzerdefinierten Phrasen die Häufigkeit einzelner Wörter zählt – mit optionalem Präfix und Exportfunktion.

---

## 🔍 Features

- Zählt Wörter aus beliebigen Text-Phrasen
- Zeigt Häufigkeit an oder blendet sie aus
- Fügt optional ein Präfix vor jedes Keyword
- Download des Ergebnisses als `.txt`
- Einfache Bedienung via Webinterface (Streamlit)

---

## 🚀 Online testen

👉 Die App läuft z. B. auf [Streamlit Community Cloud](https://streamlit.io/cloud)  
(Deployment-Hinweise siehe unten)

---

## 🖥️ Lokale Installation

```bash
# Klone das Repo
git clone https://github.com/DEIN_USERNAME/keywordschwurbler.git
cd keywordschwurbler

# Virtuelle Umgebung (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# App starten
streamlit run streamlit_app.py
