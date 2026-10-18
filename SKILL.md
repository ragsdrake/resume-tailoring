---
name: kreative-bewerbung
description: Schreibt und verbessert Anschreiben und Lebenslauf persönlich, kreativ und ohne Floskeln, aber ehrlich, und führt eine Bewerbungsübersicht. Bei jeder Bewerbung nutzen.
---

# Kreative Bewerbung

Ziel: aus der Masse stechen durch eigene Stimme und konkrete Details, nicht durch Übertreibung. Auffallen und ehrlich bleiben schließen sich nicht aus.

## Persönliche Daten
Lies zuerst `profil.md` im Skill-Ordner (Vorlage: `profil.example.md`): Kontaktdaten, Lebenslauf-Pfad, Tonwunsch, belegbare Fakten, No-Gos. Fehlt die Datei, frag kurz nach dem Nötigsten und lege sie an. `profil.md` und `bewerbungen.csv` gehören nicht ins öffentliche Repo (.gitignore).

## Vorgehen
1. **Material:** Stellenanzeige lesen, Firma kurz recherchieren (Produkte, Ton der Karriereseite). Lebenslauf aus der Quelle in `profil.md` verwenden, nicht neu erfinden.
2. **Interview (2–3 Fragen):** Frag nach Details, die nicht im Lebenslauf stehen: Was hat dich zum Thema gebracht? Was war ein nerviger oder witziger Moment? Was würdest du dort gern bauen/verbessern? Daraus entstehen die persönlichen Stellen.
3. **Aufhänger:** Ein Punkt, der nur zu dieser Firma und dieser Person passt.
4. **Entwurf:** Bei wichtigen Bewerbungen zwei Varianten (mutiger / ruhiger).
5. **Prüfen** (Checkliste unten), PDF bauen, Seite ansehen.
6. **Übersicht aktualisieren** (siehe unten).
7. **Ehrliche Hinweise** am Ende: wo es formal nicht passt, was ungeklärt ist (Fristen, offene Stelle, Adresse).

## Anschreiben-Regeln
- Kein „Sehr geehrte Damen und Herren“, kein „hiermit bewerbe ich mich“, kein „mit großem Interesse habe ich gelesen“, kein „Teamplayer/belastbar/hochmotiviert“. Anrede mit Namen, sonst eine freundliche, zur Firma passende Zeile; bei sehr konservativen Firmen eine Stufe ruhiger.
- Erster Satz erzählt etwas Konkretes, keine Selbstvorstellung.
- Zwei bis drei Erlebnisse genau erzählen (Problem, Handeln, Ergebnis) und die Anforderungen der Stelle spiegeln. Den Lebenslauf nicht wiederholen.
- Ton aus `profil.md`; Standard: direkt, neugierig, kurze Sätze, höchstens ein Augenzwinkern.
- Brüche im Lebenslauf (Studienwechsel, Lücken) offen und kurz als Entscheidung benennen.
- Schluss konkret (was im Gespräch gezeigt oder gefragt werden soll).
- Eine Seite, ca. 200–280 Wörter. Betreff darf kreativ sein, muss die Stelle klar nennen.

## Ehrlichkeit (nicht verhandelbar)
- Nur behaupten, was belegbar ist. Keine erfundenen Zahlen, Rollen, Anekdoten oder Sprachniveaus.
- Keine Superlative über sich selbst; Stärke über Beispiele zeigen.
- Bei Unsicherheit fragen oder weglassen.

## Lebenslauf verbessern
- Eine Seite, neueste Station zuerst, pro Zeile: was, womit, mit welchem Ergebnis.
- Nach Stelle gewichten (z. B. Projekte und GitHub-Link nach vorn bei IT).
- Erst streichen, was nichts beiträgt, dann kürzen, was zählt.
- Keine Platzhalter, einheitliche Daten. Foto/Geburtsdatum nur, wenn üblich oder verlangt.

## Bewerbungsübersicht
Datei `bewerbungen.csv` (Vorlage: `bewerbungen.example.csv`) mit den Spalten:
`firma;stelle;datum;status;frist;naechster_schritt;ansprechpartner;link;unterlagen`

Status: `Idee`, `Unterlagen fertig`, `Abgeschickt`, `Rückmeldung`, `Gespräch`, `Zusage`, `Absage`, `Zurückgezogen`.

- Nach jeder erstellten oder verschickten Bewerbung eine Zeile anlegen oder den Status ändern. Nur Status setzen, den Nutzer bestätigt oder den die Tools belegen (z. B. gesendete Mail); sonst `Unterlagen fertig`.
- Übersicht anzeigen: `python3 scripts/uebersicht.py [bewerbungen.csv]` gibt eine Markdown-Tabelle aus, sortiert nach Frist, mit Hinweisen zu überfälligen Fristen und Bewerbungen ohne Rückmeldung nach 14 Tagen.
- Auf Wunsch die Übersicht als Tabelle (Sheet) oder Seite aufbereiten.

## Vor dem Senden
- [ ] Erster Satz ist keine Floskel und passt nur zu dieser Firma
- [ ] Keine Behauptung ohne Beleg
- [ ] Bruch/Wechsel ehrlich, aber kurz
- [ ] Eine Seite, keine Platzhalter, Firmenname und Adresse stimmen
- [ ] Anschreiben und Lebenslauf widersprechen sich nicht
- [ ] Übersicht aktualisiert
