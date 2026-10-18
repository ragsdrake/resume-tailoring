#!/usr/bin/env python3
"""Gibt die Bewerbungsübersicht als Markdown-Tabelle aus."""
import csv, sys
from datetime import date, datetime

OFFEN = {"Idee", "Unterlagen fertig", "Abgeschickt", "Rückmeldung", "Gespräch"}

def d(s):
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None

def main(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    heute = date.today()
    rows.sort(key=lambda r: (d(r.get("frist", "")) is None, d(r.get("frist", "")) or date.max))
    print("| Firma | Stelle | Status | Frist | Nächster Schritt |")
    print("|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['firma']} | {r['stelle']} | {r['status']} | {r.get('frist') or '-'} | {r.get('naechster_schritt') or '-'} |")
    hinweise = []
    for r in rows:
        fr, ab = d(r.get("frist", "")), d(r.get("datum", ""))
        if r["status"] in ("Idee", "Unterlagen fertig") and fr and fr < heute:
            hinweise.append(f"Frist überschritten: {r['firma']} ({r['stelle']}, {fr})")
        if r["status"] == "Abgeschickt" and ab and (heute - ab).days >= 14:
            hinweise.append(f"Seit {(heute - ab).days} Tagen keine Rückmeldung: {r['firma']} ({r['stelle']})")
    zaehler = {}
    for r in rows:
        zaehler[r["status"]] = zaehler.get(r["status"], 0) + 1
    print("\nStatus:", ", ".join(f"{k} {v}" for k, v in sorted(zaehler.items())))
    if hinweise:
        print("\nHinweise:")
        for h in hinweise:
            print("-", h)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bewerbungen.csv")
