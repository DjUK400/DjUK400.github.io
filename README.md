# Aplikacije za fakultet

**Link:** https://djuk400.github.io/

Početna stranica sa svim mojim aplikacijama za prvu godinu Građevinskog fakulteta (Banja Luka): rješavač inverznih funkcija, limesi nizova, MM rješavač za prvi kolokvijum, rješavač ortogonalnih projekcija i zadaci sa vježbi iz nacrtne.

Sve aplikacije dijele isti dizajn (po uzoru na Rješavač inverznih funkcija): iste boje, fontove, zaglavlje, tabove i gornju traku „← Sve aplikacije“ sa dugmetom za temu. Izbor teme važi za sve aplikacije odjednom.

## Dodavanje nove aplikacije
1. U `alati/hub.py` dodaj red u listu `APPS` (grupa, oznaka, boja, naslov, opis, oznake, link) i pokreni `python3 alati/hub.py` → nastaje novi `index.html`.
2. U novoj aplikaciji primijeni zajednički dizajn funkcijom `apply()` iz `alati/skin.py` (primjeri za postojeće aplikacije su u `alati/apply_all.py`). Blok između `<!--fk-dizajn:start-->` i `<!--fk-dizajn:end-->` se može ponovo generisati bez dupliranja.
