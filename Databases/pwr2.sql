SELECT pseudo_dawcy as dawca_A, rocznik_dawcy
FROM Dawcy
WHERE grupa_krwi = 'A';


ALTER SESSION SET NLS_DATE_FORMAT = 'dd.mm.yyyy'

SELECT DISTINCT pseudo_dawcy as Dawca
FROM Donacje
Where data_oddania between '20.07.2005' and '20.08.2005';

SELECT pseudo_dawcy, plec_dawcy
FROM Dawcy
WHERE rocznik_dawcy in (1971, 1977);

SELECT DISTINCT pseudo_dawcy
FROM Donacje 
Where months_between('17.05.2006',data_wydania) >= 10;

SELECT pseudo_dawcy as Dawca,ilosc_krwi, nvl(to_char(data_wydania), 'na stanie') Wydano
FROM Donacje 
Where data_oddania >'10.07.2005';

SELECT count(distinct sprawnosc)
FROM Sprawnosci_w
WHERE pseudo_wampira in ('Opoj', 'Czerwony')

SELECT sum(ilosc_krwi)as "Cieple buleczki"
FROM Donacje
WHERE data_wydania - data_oddania <=10

SELECT pseudo_wampira, count(jezyk_obcy) as "liczba jezykow"
FROM Jezyki_obcje_w
WHERE jezyk_obcy <> 'rosyjski'
GROUP BY pseudo_wampira

SELECT pseudo_wampira "Wampir", COUNT(data_wydania) "Liczba konsumpcji"
FROM Donacje 
HAVING COUNT(data_wydania) > 1
GROUP BY pseudo_wampira;

SELECT grupa_krwi, plec_dawcy, COUNT(pseudo_dawcy) "Liczba dawców"
FROM Dawcy
GROUP BY grupa_krwi, plec_dawcy
ORDER BY grupa_krwi;







