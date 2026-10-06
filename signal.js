// CICADA 6845 — signál 01 // kanál 6845
//
// Pravidlo č. 4: tento kód je na ČÍTANIE, nie na spúšťanie.
// Kto číta pozorne, vidí viac.
//
// Zachytávame signál. Prišiel odzadu.

// --- zachytený signál ---
const SIGNAL = "=UkUFlUTFJFUgEkTgUkSgE0QVx0SgE0QJZ1TM9EUgEESVJFR";

function pocuvaj(s) {
  // signál prišiel odzadu — otoč ho
  return s.split("").reverse().join("");
}

console.log("Tento skript len počúva.");
console.log("Odpoveď nie je vo výstupe. Je v kóde.");
// Nápoveda: pozri funkciu pocuvaj(). Potom base64.
