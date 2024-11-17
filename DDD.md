# Opis zadania
Celem zadania było zamodelowanie fragmentu bezpieczenej aplikacji bankowej, wykorzystując zasady Domain Driven Design. Opisano fragment odpowiedzialny za podstawowe transakcje bankowe. Zidentyfikowano konteksty w obrębie systemu i podstawowe agregaty/encje oraz obiekt wartości.

# Wyniki

W pliku DDD.png umieszczono obrazek przedstawiający model

## Założenia

### Encje i Obiekty wartości
#### KontoBankowe (agregat)
* NumerKonta - unikalny numer konta (standard NBR) - ciąg 26 cyfr
* SaldoKonta
* TypKonta
#### SaldoKonta (obiektWartość)
* Kwota - liczba zmiennoprzecinkowa
* Waluta - enum
#### TypKonta (obiektWartosc)
* Typ - enum

#### Przelew (agregat)
* DanePrzelewu 
* PrzelewNadawca - identyfikator KontoBankowe 
* PrzelewOdbiorca - unikalny numer konta (standard NBR) - ciąg 26 cyfr
#### DanePrzelewu (encja)
* DataPrzelewu 
* WartoscPrzelewu
* RodzajPrzelewu
#### DataPrzelewu (obiektWartosc)
* Data - data dzień/godzina (dokładność do sekund)
#### WartoscPrzelewu (obiektWartosc)
* Wartosc - liczba zmiennoprzecinkowa
#### RodzajPrzelewu (obiektWartosc)
* Rodzaj - enum

#### Użytkownik (agregat)
* Login - string, unikalny
* SposobLogowania
* Klient
#### SposobLogowania (encja)
* Sposob
* DaneUwierzytelniajace
#### DaneUwierzytelniajace (obiektWartosc)
* Haslo - zaszyfrowane, ciag znakow - min. 8 znakow (haslo lub wyliczany kod zaleznie od sposobu logowania)
#### Sposob (obiektWartosc)
* Sposob - enum

#### Klient (agregat)
* KontoBankowe
* DaneKlienta
#### DaneKlienta (encja)
* Imiona - string, 2-50 znaków, bez cyfr
* Nazwisko - string, 2-30 znaków, bez cyfr
* DaneKontaktowe 
#### DaneKontaktowe (obiektWartosc)
* E-mail - string, z jednym znakiem @
* Telefon - ciąg max 9 cyfr
* Kierunkowy - enum (nr kierunkowy kraju telefonu)
* Adres - ciąg znaków - litery i cfyr oraz znaki: /,-



