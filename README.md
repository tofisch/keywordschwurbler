# Keywordschwurbler

Dieses Repository enthält eine kleine Streamlit-App, um die einzelnen Wörter aus einer Liste von Keyword-Phrasen zu zählen.
Requires Python 3.8 or higher.

## Nutzung

1. Installiere die Abhängigkeiten (z. B. in einer virtuellen Umgebung):
   ```bash
   pip install -r requirements.txt
   ```
2. Starte die Anwendung:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Füge deine Keyword-Phrasen in das Textfeld ein. Die App zeigt die Wörter nach Häufigkeit sortiert an.

    Optional kannst du im Feld "Präfix vor jedem Keyword" einen Text eingeben,
    der vor jedes ausgegebene Wort gesetzt wird.

    Nach der Berechnung kannst du über den Button "Zahlen entfernen"
    die Häufigkeiten aus dem Ergebnis entfernen. Mit "Fenster zurücksetzen"
    löschst du alle Eingaben.

4. Über den Button "Ergebnis herunterladen" kannst du die Liste als `wortliste.txt` speichern.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

