# Määrittelydokumentti

- Harjoitustyön tekijä: Teemu Bergman
- Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)
- Toteutettavat algoritmit:
  - `Shunting yard algorithm` [Dijkstra, 1961]
  - `Postfix expression stack evaluator` (reverse Polish notation) [Hamblin, 1962]
- Ohjelmointikieli: `Python` (^3.10)
  - Riippuvuuksien hallinta: `Poetry`
  - Yksikkötestaus: `Pytest`
  - Testauksen raportointi: `Coverage`
  - Koodin laadullinen hallinta: `Autopep8`
  - Koodin laadullinen testaus: `Pylint`

## Harjoitustyön kuvaus

Harjoitustyönäni toteutan Dijkstran `Shunting yard` [Dijkstra, 1961] -algoritmia sekä Hamblinin `Postfix expression stack evaluator` [Hamblin, 1962] -algoritmia hyödyntävän tieteellisen laskimen. 

Shunting Yard -algoritmi on matemaattisten lausekkeiden uudelleen jäsentämisessä käytetty algoritmi joka muuntaa infix-muotoisen syötteen Reverse Polish notation (RPN)/postfix-muotoon. Postfix expression stack evaluator -algoritmi (harjoitustyössä nimeltään: `RPNEvaluator`) arvioi RPN/postfix-muotoisen lausekkeen arvon suorittamalla pinoa apunaan käyttäen siinä olevat laskutoimitukset. 

Kummatkin algoritmit käyvät syötteen läpi vain kerran ja suorittavat siinä olevat laskutoimituksen vain kerran, joten yksinkertaisina algoritmeina ne ovat verrattain tehokkaita monimutkaistenkin laskutoimitusten ratkaisemiseen.

## Aika- ja tilavaativuudet

Shunting Yard sekä Postfix expression stack evaluator -algoritmien aikavaativuudet ovat `O(n)`. Kun kyseessä on tieteellinen laskin, on tilavaatimus hyvin maltillinen, noin kymmenistä kilotavuista muutamiin satoihin kilotavuihin.

## Lähteet

- Dijkstra, Edsger, W. (1961). Algol 60 translation : An algol 60 translator for the x1 and making a translator for algol 60. p. 22. //www.cs.utexas.edu/~EWD/MCReps/MR35.PDF
- Hambling, Charles, Leonard. (1962). Translation to and from Polish notation. Computer Journal. p. 210–213. //[doi.org/10.1093%2Fcomjnl%2F5.3.210](https://doi.org/10.1093%2Fcomjnl%2F5.3.210)
- Reverse Polish notation. (n.d.). Wikipedia. Haettu 12.3.2023 osoitteesta:     //[en.wikipedia.org/wiki/Reverse_Polish_notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
