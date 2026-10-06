#!/usr/bin/env python3
"""
CICADA 6845 — signál 01 // kanál 6845

Pravidlo č. 4: tento kód je na ČÍTANIE, nie na spúšťanie.
Kto číta pozorne, vidí viac.

Zachytávame signál. Prišiel odzadu.
"""


# --- zachytený signál ---
SIGNAL = "=UkUFlUTFJFUgEkTgUkSgE0QVx0SgE0QJZ1TM9EUgEESVJFR"


def pocuvaj(s):
    """Signál prišiel odzadu. Otoč ho."""
    return s[::-1]


if __name__ == "__main__":
    print("Tento skript len počúva.")
    print("Odpoveď nie je vo výstupe. Je v kóde.")
    # Nápoveda: pozri funkciu pocuvaj(). Potom base64.
