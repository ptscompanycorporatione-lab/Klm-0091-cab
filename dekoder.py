#!/usr/bin/env python3
"""
CICADA 6845 — pomocný dekodér (nástroj pre riešiteľov).

Čo robí: dekóduje text z base64 / hex / binárne / morzeovky,
prípadne skúša všetky posuny Caesarovej šifry.
Čo nerobí: nič neinštaluje, nikam sa nepripája, nič nezapisuje na disk.

BEZPEČNOSŤ: aj tak platí pravidlo — kód najprv čítaj, spúšťaj až keď
rozumieš, čo robí. Pravidlá: PRAVIDLA.md, bod 2.
"""

import base64
import binascii

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}
MORSE_OBRATENE = {v: k for k, v in MORSE.items()}


def z_base64(s):
    s = ''.join(s.split())
    chyba = len(s) % 4
    if chyba:
        s += '=' * (4 - chyba)
    return base64.b64decode(s).decode('utf-8', errors='replace')


def z_hex(s):
    s = ''.join(s.split()).lower()
    if s.startswith('0x'):
        s = s[2:]
    return bytes.fromhex(s).decode('utf-8', errors='replace')


def z_binarne(s):
    bity = ''.join(s.split())
    znaky = [bity[i:i + 8] for i in range(0, len(bity), 8)]
    return ''.join(chr(int(b, 2)) for b in znaky if len(b) == 8)


def z_morzeovky(s):
    slova = s.strip().split(' / ')
    vysledok = []
    for slovo in slova:
        vysledok.append(''.join(MORSE_OBRATENE.get(p, '?') for p in slovo.split()))
    return ' '.join(vysledok)


def caesar_vsetky(s):
    vysledky = []
    for posun in range(1, 26):
        prelozene = []
        for ch in s:
            if 'a' <= ch <= 'z':
                prelozene.append(chr((ord(ch) - 97 - posun) % 26 + 97))
            elif 'A' <= ch <= 'Z':
                prelozene.append(chr((ord(ch) - 65 - posun) % 26 + 65))
            else:
                prelozene.append(ch)
        vysledky.append((posun, ''.join(prelozene)))
    return vysledky


def main():
    print('CICADA 6845 — dekodér')
    print('Vlož zakódovaný text (prázdny riadok = koniec):')
    riadky = []
    while True:
        try:
            r = input()
        except EOFError:
            break
        if not r.strip():
            break
        riadky.append(r)
    text = '\n'.join(riadky)
    print('\n--- base64 ---')
    try:
        print(z_base64(text))
    except (binascii.Error, ValueError):
        print('(nie je platné base64)')
    print('\n--- hex ---')
    try:
        print(z_hex(text))
    except ValueError:
        print('(nie je platný hex)')
    print('\n--- binárne ---')
    try:
        print(z_binarne(text))
    except ValueError:
        print('(nie je platné binárne)')
    print('\n--- morzeovka ---')
    print(z_morzeovky(text))
    print('\n--- Caesar (všetky posuny) ---')
    for posun, vysl in caesar_vsetky(text):
        print(f'{posun:2}: {vysl}')


if __name__ == '__main__':
    main()
