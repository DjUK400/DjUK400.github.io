# Limesi funkcija

👉 [djuk400.github.io/limes-funkcije](https://djuk400.github.io/limes-funkcije/)

Rješavač limesa funkcija **korak po korak** (DIR, prva godina Građevinskog fakulteta). Cilj je da naučiš postupak: svaki korak ima hint i obrazloženje *zašto* se radi baš tako. Radi na računaru i telefonu, bez instalacije.

## Tipovi zadataka

| # | Tip | Primjer | Metoda |
|---|-----|---------|--------|
| 0 | **Limes kad x → a bez Lopitala / Makloren (kao na rokovima)** | (eˣ − cos 2x)/(2 sin x + ln(1−x)) → 1; (cos x − e^(−x²/2))/x⁴ → −1/12 | dodaj i oduzmi 1 + standardni limesi; Maklorenova formula kad se vodeći članovi poništavaju |
| 1 | Racionalna funkcija, x → a | (x³−3x+2)/(x⁴−4x+3), x→1 → 1/2 | Hornerova šema, skraćivanje (x − a); za c/0 lijevi i desni limes |
| 2 | Racionalna funkcija, x → ±∞ | (x³+1)/(x²+1), x→−∞ → −∞ | izvlačenje najvećeg stepena |
| 3 | Iracionalni izraz 0/0 | (√(x+5) − 3)/(x−4), x→4 → 1/6 | racionalizacija (konjugovani izraz) |
| 4 | Razlika korijena ∞ − ∞ | √(x²+x) + x, x→−∞ → −1/2 | racionalizacija, izvlačenje \|x\| |
| 5 | Standardni limesi (x → 0) | (1 − cos x)/(x·sin x) → 1/2 | sin t/t, (1−cos t)/t², (eᵗ−1)/t, ln(1+t)/t, (bᵗ−1)/t, ⁿ√(1+t) |
| 6 | Oblik 1^∞ | ((x+3)/(x+1))ˣ → e² | (1 + 1/t)ᵗ → e |
| 7 | Jednostrani limesi | e^(1/x), arctg(1/(x−1)), \|x−3\|/(x−3) | znak sa lijeve i desne strane |
| 8 | Asimptote racionalne funkcije | x³/(x²−1) → x = ±1, y = x | jednostrani limesi, k = lim f/x, n = lim (f − kx) |

Tip 0 ima kao primjere svih 10 zadataka sa limesom funkcije sa kolokvijuma i rokova DIR 1 / M2 (5.12.2025 – 25.9.2026). Izrazi se upisuju kao na papiru: `e^x - cos(2x)`, `sqrt(cos(x)) - cbrt(cos(x))`, `|tg(3x)|`.

## Učenje
- **Hintovi:** prvo vidiš samo pitanje-hint, pa korak otvaraš sam; rezultat je sakriven.
- **„Zašto?“** uz svaki korak.
- **Pokušaj sam:** upišeš svoj odgovor (npr. `2/3`, `-inf`, `e^2`, `sqrt(7)/84`, `ln2/ln3`, `pi/2`, `ne postoji`) i dobiješ provjeru.
- **Pravila i pojmovi:** definicija, jednostrani limesi, standardni limesi, računanje sa ∞, neodređeni oblici, teoreme, ekvivalentne veličine, asimptote, „koju metodu kada“ i česte greške.

## Pouzdanost
- Računa se tačnom racionalnom aritmetikom (razlomci, korijeni, ln, e i π ostaju simbolički).
- Prije prikaza svaki rezultat se automatski provjerava numerički; ako provjera ne prođe, rezultat se ne prikazuje.
- Za nepodržan unos stranica prikaže obavještenje sa razlogom i ne izmišlja rješenje.

## Ograničenja
- Bez Lopitalovog pravila. U tipu 0 funkcije moraju u tački a imati „lijepu“ vrijednost (argument sin/cos/tg/e jednak 0, argument ln jednak 1, korijen iz savršenog stepena) — inače rezultat nije racionalan i prikazuje se obavještenje.
- Tip 0 ne radi limese kad x → ±∞ niti eksponente oblika f(x)^g(x) (za to su tipovi 2, 4 i 6).
- Asimptote: samo kad su nule imenioca racionalne (ili ih nema).
