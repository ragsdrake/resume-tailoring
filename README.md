# kreative-bewerbung

Ein Claude-Skill für persönliche, ehrliche Bewerbungen auf Deutsch: Anschreiben ohne Floskeln, Lebenslauf-Feinschliff und eine Bewerbungsübersicht.

## Was er macht
- Fragt vor dem Schreiben 2–3 persönliche Details ab, aus denen die Geschichten im Anschreiben entstehen
- Kein „Sehr geehrte Damen und Herren“, keine Phrasen; ein Aufhänger, der zur Firma passt
- Hält sich an belegbare Fakten (keine erfundenen Zahlen oder Anekdoten)
- Passt den Lebenslauf an die Stelle an
- Führt `bewerbungen.csv` und zeigt sie als Tabelle mit Hinweisen zu Fristen und fehlenden Rückmeldungen

## Installation
Ordner nach `~/.claude/skills/kreative-bewerbung` kopieren (oder in Claude als Skill hinzufügen), dann `profil.example.md` zu `profil.md` kopieren und ausfüllen.

## Übersicht anzeigen
```bash
python3 scripts/uebersicht.py bewerbungen.csv
```
Vorlage: `bewerbungen.example.csv` (Trennzeichen `;`, Datum `JJJJ-MM-TT`).

## Datenschutz
`profil.md` und `bewerbungen.csv` stehen in der `.gitignore` und werden nicht mitveröffentlicht.

## Lizenz
MIT
