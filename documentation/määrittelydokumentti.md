# Määrittelydokumentti

- Harjoitustyön tekijä: Teemu Bergman
- Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)
- Toteutettavat algoritmit:
  - Shunting yard algorithm [Dijkstra, 1961]
  - Postfix expression stack evaluator (reverse Polish notation) [Hamblin, 1962]
- Ohjelmointikieli: Python (^3.10)
  - Riippuvuuksien hallinta: Poetry
  - Yksikkötestaus: Pytest
  - Testauksen raportointi: Coverage
  - Koodin laadullinen hallinta: Autopep8
  - Koodin laadullinen testaus: Pylint

## Harjoitustyön kuvaus

Harjoitustyönäni toteutan Edsger Dijkstran Shunting yard [Dijkstra, 1961] -algoritmia hyödyntävän tieteellisen laskimen, joka ottaa syötteeksi lausekkeita jotka voivat sisältää lukuarvoja, muuttujia, peruslaskutoimituksia sekä funktioita. 

## Lähteet

- Dijkstra, Edsger, W. (1961). Algol 60 translation : An algol 60 translator for the x1 and making a translator for algol 60. p. 22. URL: https://www.cs.utexas.edu/~EWD/MCReps/MR35.PDF
- Hambling, Charles, Leonard. (1962). Translation to and from Polish notation. Computer Journal. **5** (3): 210–213. URL: https://doi.org/10.1093%2Fcomjnl%2F5.3.210
