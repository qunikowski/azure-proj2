# azure-proj2
Project 2 for Microsoft Azure on WUT

## Table of contents
* [Team](#the-team)
* [Tematyka projektu](#tematyka-projektu)
* [Architektura](#architektura)
* [Rozwiązanie](#rozwiązanie)
* [Demo dzałania](#demo-działania)

## The Team
* Krzysztof Maciejewski - https://github.com/kristoph4822
* Marcin Kotecki  - https://github.com/marcinkotecki
* Hubert Kunikowski - https://github.com/qunikowski
* Danuta Stawiarz  - https://github.com/DanutaStawiarz

## Tematyka projektu
W czasach niedoboru żywności na świecie niezwykle istotnym zagadnieniem okazuje się poszukiwanie sposobów, dzieki którym produkcja jedzenia stanie się bardziej wydajna. Obecnie, w niektórych regionach świata straty spowodowane chorobami roślin sięgają nawet 100%.

Aplikacja ma na celu wsparcie rolników -  umożliwia zeskanowanie zdjęcia liścia w celu postawienia diagnozy. W wyniku użytkownik otrzymuje gatunek rośliny, z jakiej pochodzi liść, a także diagnozę, czy roślina jest zdrowa lub jaką z chorób posiada. Obecnie w aplikacja umożliwia diagnostykę dla:
* jabłek - liść zdrowy/ apple scab( parch jabłoni)/ apple black rot (czarna zgnilizna)/ cedar apple rust
* kukurydzy - liść zdrowy/ corn common rust (rdza zwykła) / gray leaf spot (szara plamistość liści)/ northern leaf blight
* pomidor - liść zdrowy/ late blight/ leaf mold/ septoria leaf spot/ two-spotted spider mite/ mosaic virus/ target spot/ yellow curl virus

W przyszłości możliwe jest rozszerzenie zakresu funckjonowania aplikacji o kolejne gatunki oraz choroby.


## Architektura
Aplikacja korzysta z serwisów oferowanych w całości przez platformę Azure. Schemat działania przedstawia się następująco:
![Optional Text](images/architektura.png)

### Custom Vision
W obrębie serwisu zostały umieszczone zdjęcia liści zdrowych oraz z różnymi chorobami. Następnie model został wytrenowany. Wyniki można uznać za zadowalające, co potwierdziły wykonywane na zbiorze testowym doświadczenia. Wyniki modelu przedstawiają się następująco:

![Optional Text](images/performance.png)
