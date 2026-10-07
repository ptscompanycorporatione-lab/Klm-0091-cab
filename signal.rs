/*
CICADA 6845 — signál 04 // kanál 6845

Pravidlo č. 4: tento kód je na ČÍTANIE, nie na spúšťanie.
Kto číta pozorne, vidí viac.

Zachytávame signál. Prišiel po častiach a odzadu.
*/

// --- zachytený signál (3 časti, pomiešané poradie) ---
const CAST_KONIEC: &str = "kWP1EIBRkVBJFUgUkSg80Q";   // koniec
const CAST_ZACIATOK: &str = "=QlTF10RBJlRgkFRaF0Sg";  // začiatok
const CAST_STRED: &str = "k0UgIVRW9EIUFUTBx0SgU";     // stred

// Signál prišiel po častiach a odzadu.
// Najprv zlož časti v správnom poradí, potom ho otoč.
fn pocuvaj(s: &str) -> String {
    s.chars().rev().collect()
}

fn main() {
    println!("Tento program len počúva.");
    println!("Odpoveď nie je vo výstupe. Je v kóde.");
    // Nápoveda: pozri popisky častí. Potom pocuvaj(). Potom base64.
}
