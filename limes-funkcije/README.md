# Limesi funkcija

👉 [djuk400.github.io/limes-funkcije](https://djuk400.github.io/limes-funkcije/)

Rješavač limesa funkcija **korak po korak** (DIR, prva godina Građevinskog fakulteta). Cilj je da naučiš postupak: svaki korak ima hint i obrazloženje *zašto* se radi baš tako. Radi na računaru i telefonu, bez instalacije.

## Tipovi zadataka

| # | Tip | Primjer | Metoda |
|---|-----|---------|--------|
| 1 | Racionalna funkcija, x → a | (x³−3x+2)/(x⁴−4x+3), x→1 → 1/2 | Hornerova šema, skraćivanje (x − a); za c/0 lijevi i desni limes |
| 2 | Racionalna funkcija, x → ±∞ | (x³+1)/(x²+1), x→−∞ → −∞ | izvlačenje najvećeg stepena |
| 3 | Iracionalni izraz 0/0 | (√(x+5) − 3)/(x−4), x→4 → 1/6 | racionalizacija (konjugovani izraz) |
| 4 | Razlika korijena ∞ − ∞ | √(x²+x) + x, x→−∞ → −1/2 | racionalizacija, izvlačenje \|x\| |
| 5 | Standardni limesi (x → 0) | (1 − cos x)/(x·sin x) → 1/2 | sin t/t, (1−cos t)/t², (eᵗ−1)/t, ln(1+t)/t, (bᵗ−1)/t, ⁿ√(1+t) |
| 6 | Oblik 1^∞ | ((x+3)/(x+1))ˣ → e² | (1 + 1/t)ᵗ → e |
| 7 | Jednostrani limesi | e^(1/x), arctg(1/(x−1)), \|x−3\|/(x−3) | znak sa lijeve i desne strane |
| 8 | Asimptote racionalne funkcije | x³/(x²−1) → x = ±1, y = x | jednostrani limesi, k = lim f/x, n = lim (f − kx) |

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
- Nema Lopitalovog pravila ni Tejlorovih razvoja: npr. (sin x − x)/x³ nije podržano (standardni limesi važe samo u proizvodu i količniku).
- Korijeni su samo kvadratni (u tipovima 3 i 4); trigonometrija samo za x → 0.
- Asimptote: samo kad su nule imenioca racionalne (ili ih nema).
