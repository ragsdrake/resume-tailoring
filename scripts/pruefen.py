#!/usr/bin/env python3
"""Prüft ein Anschreiben (Textdatei) auf Floskeln, Platzhalter, Länge und typische Belegprobleme."""
import re, sys

FLOSKELN = [
    r"sehr geehrte", r"hiermit bewerbe", r"mit großem interesse", r"teamplayer", r"teamfähig",
    r"belastbar", r"hochmotiviert", r"ich bin überzeugt", r"hiermit möchte ich", r"ideale(r)? kandidat",
    r"über eine einladung .* freue",
]
UNBELEGT = [  # Formulierungen, die einen Beleg im Profil brauchen
    r"viel(e)? erfahrung", r"langjährig", r"stets", r"immer", r"hervorragend", r"exzellent",
    r"flexibel einsetzbar", r"sehr gut(e|en)? kenntnisse", r"expert",
]
PLATZHALTER = r"\[[^\]]+\]|XXX|TODO|Lorem"

def main(path):
    t = open(path, encoding="utf-8").read()
    low = t.lower()
    n = len(t.split())
    probleme = []
    if n > 300: probleme.append(f"Zu lang: {n} Wörter (Ziel 200-280)")
    if n < 150: probleme.append(f"Sehr kurz: {n} Wörter")
    for p in FLOSKELN:
        if re.search(p, low): probleme.append(f"Floskel: /{p}/")
    for m in re.finditer(PLATZHALTER, t): probleme.append(f"Platzhalter: {m.group(0)}")
    hinweise = [f"Belegen oder streichen: /{p}/" for p in UNBELEGT if re.search(p, low)]
    first = re.split(r"(?<=[.!?])\s", t.strip(), maxsplit=1)[0].lower()
    if re.match(r"^(hiermit|ich bewerbe|mein name ist|ich möchte mich)", first):
        probleme.append("Erster Satz ist eine Selbstvorstellung statt eines konkreten Einstiegs")
    print(f"Wörter: {n}")
    for p in probleme: print("PROBLEM:", p)
    for h in hinweise: print("HINWEIS:", h)
    if not probleme and not hinweise: print("Keine Auffälligkeiten.")
    sys.exit(1 if probleme else 0)

if __name__ == "__main__":
    main(sys.argv[1])
