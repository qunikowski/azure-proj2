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

## Funkcjonalności
* Rozpoznawanie chorób roślin na podstawie wprowadzonych zdjęć
* Zapisywanie zwracanych predykcji w bazie danych
* Analizowanie chorób roślin w zwracanych przez aplikację predykcjach
* Prezentowanie panujących tendencji dotyczących chorób roślin

## Technologie
W projekcie wykorzystane zostały nastepujące technologie:
- Azure Custom Vision
- Azure Postgresql
- Azure Analitycs
- Azure Web App

## Opis rozwiązania

### 1. Stworzenie modelu
Model do rozpoznawania chorób roślin stworzony został przy wykorzystaniu serwisu Azure Custom Vision. Do trenowania użyto //źródłaDanych

### 2. Stworzenie aplikacji webowej
Do stworzenia aplikacji webowej wykorzystano Pythonowego frameworka Flask. Z aplikacją powiązana jest baza postgresql Aplikacja dostepna jest pod adresem: //LINK

### 3. Wykorzystanie Azure Analitycs

## Demo działania

Demo działania aplikacji - >LINK<

