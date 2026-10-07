/*
CICADA 6845 — signál 03 // kanál 6845

Pravidlo č. 4: tento kód je na ČÍTANIE, nie na spúšťanie.
Kto číta pozorne, vidí viac.

Zachytávame signál. Prišiel po častiach a odzadu.
*/
using System;
using System.Linq;

class Signal {
    // --- zachytený signál (3 časti, pomiešané poradie) ---
    const string CAST_A = "1TQBSRJ5URUNVVMBSQOBSVPJURTBCRF"; // 2/3
    const string CAST_B = "JFUgMVQNBiWVBCVOVUTHFkUGBSWWJFU"; // 3/3
    const string CAST_C = "GVESDJVRCl1QgEEIJlEVQllULBSSaV";  // 1/3

    // Signál prišiel po častiach a odzadu.
    // Najprv zlož časti v správnom poradí, potom ho otoč.
    static string Pocuvaj(string s) {
        return new string(s.Reverse().ToArray());
    }

    static void Main() {
        Console.WriteLine("Tento program len počúva.");
        Console.WriteLine("Odpoveď nie je vo výstupe. Je v kóde.");
        // Nápoveda: pozri číslovanie častí. Potom Pocuvaj(). Potom base64.
    }
}
