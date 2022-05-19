ALTER SESSION SET NLS_DATE_FORMAT = 'dd.mm.yyyy'

/* zad 1*/
SELECT nr_zlecenia "Zlecenie AB"
FROM Donacje INNER JOIN Dawcy on Donacje.pseudo_dawcy = Dawcy.pseudo_dawcy
WHERE grupa_krwi = 'AB';

/* zad 2*/
SELECT pseudo_wampira, plec_wampira "Plec",NVL(pseudo_szefa,' '), NVL((SELECT Wampiry.plec_wampira 
                                                        FROM Wampiry 
                                                        WHERE W.pseudo_szefa = pseudo_wampira),' ') "plec szefa"
FROM Wampiry W;


/* zad 3*/
SELECT pseudo_dawcy "dawcy przed  slodka", plec_dawcy
FROM Dawcy
WHERE rocznik_dawcy < (SELECT rocznik_dawcy
                        FROM Dawcy
                        WHERE pseudo_dawcy = 'Slodka');
                        
/* zad 4*/

SELECT pseudo_dawcy "Pseudonim", case when sum(ilosc_krwi) < 700 then 'ponizej 700'
                                      when sum(ilosc_krwi) > 1000 then 'powyzej 1000'
                                      else 'miedzy 700 a 1000' end "pobor"
From (
    SELECT pseudo_dawcy , ilosc_krwi 
    FROM Donacje
    union 
    select pseudo_dawcy, ilosc_krwi
    From Donacje)
GROUP BY pseudo_dawcy
ORDER BY pseudo_dawcy;


/* zad 5*/
SELECT Jezyki_obcje_w.pseudo_wampira, count(distinct jezyk_obcy)
from Jezyki_obcje_w INNER JOIN Sprawnosci_w on Jezyki_obcje_w.pseudo_wampira = Sprawnosci_w.pseudo_wampira
having count(distinct jezyk_obcy) = count(distinct sprawnosc)
GROUP BY  Jezyki_obcje_w.pseudo_wampira

/* zad 6*/
SELECT nr_zlecenia "zlecenie AB", data_oddania "data wykonania"
FROM Donacje natural join 
    (SELECT pseudo_dawcy
    FROM Dawcy
    WHERE grupa_krwi = 'AB')
    
/* zad 7*/
SELECT plec_wampira, count(*) "liczba lingwistow"
FROM Wampiry natural join
     (SELECT pseudo_wampira
     FROM Jezyki_obcje_w
     HAVING count(distinct jezyk_obcy_od) > 1
     GROUP BY pseudo_wampira)
GROUP BY plec_wampira

/* zad 8a*/
SELECT ilosc_krwi "objetosc", pseudo_dawcy "dawca"
FROM Donacje don
WHERE 3 >(SELECT count(distinct ilosc_krwi)
         FROM Donacje
         WHERE ilosc_krwi > don.ilosc_krwi)

/* zad 8b*/
SELECT don.ilosc_krwi "objetosc",don.pseudo_dawcy "dawca"
FROM Donacje don, Donacje pom
WHERE don.ilosc_krwi <= pom.ilosc_krwi
Group by don.pseudo_dawcy, don.ilosc_krwi
HAVING count(distinct pom.ilosc_krwi) <= 3

/* zad 9a podzapytania*/
SELECT pseudo_dawcy, grupa_krwi
FROM Dawcy
WHERE pseudo_dawcy 
        IN (SELECT pseudo_dawcy
            FROM Donacje
            WHERE nr_zlecenia
        IN (SELECT nr_zlecenia
            FROM Zlecenia
             WHERE pseudo_wampira
        IN (SELECT pseudo_wampira
            FROM Wampiry
            WHERE pseudo_wampira
        IN (SELECT pseudo_wampira
            FROM Jezyki_obcje_w
            WHERE jezyk_obcy='polski'))))

/* zad 9b laczenia*/
SELECT DISTINCT
    d.pseudo_dawcy "Dawca",
    d.grupa_krwi "Grupa",
    z.pseudo_wampira "Biorca"
	FROM((((
            dawcy d
            JOIN donacje do ON 
            d.pseudo_dawcy = do.pseudo_dawcy)
            JOIN zlecenia z ON 
            do.nr_zlecenia = z.nr_zlecenia)
            JOIN wampiry w ON 
            z.pseudo_wampira = w.pseudo_wampira)
            JOIN jezyki_obce_w j ON 
            j.pseudo_wampira = w.pseudo_wampira)
WHERE
        w.plec_wampira = 'M' AND j.jezyk_obcy = 'polski'
        
/* zad 10*/
SELECT  pseudo_wampira, to_char(wampir_w_rodzinie, 'YYYY') "rok wstapienia"
FROM Wampiry W
WHERE EXISTS (SELECT pseudo_wampira, wampir_w_rodzinie
                FROM Wampiry
                WHERE W.pseudo_wampira != Wampiry.pseudo_wampira
                AND to_char(W.wampir_w_rodzinie, 'YYYY') = to_char(Wampiry.wampir_w_rodzinie, 'YYYY'))
                
                
/* zad 11*/
SELECT to_char(wampir_w_rodzinie, 'YYYY') "rok", count(to_char(wampir_w_rodzinie, 'YYYY')) "liczba wstopien"
FROM Wampiry
GROUP BY to_char(wampir_w_rodzinie, 'YYYY')
UNION
SELECT 'srednia' , avg(count(to_char(wampir_w_rodzinie, 'YYYY')))
FROM Wampiry
GROUP BY to_char(wampir_w_rodzinie, 'YYYY')
ORDER BY 2

/* zad 12b*/
SELECT  *
FROM 
    (SELECT Dawcy.grupa_krwi, round(avg(suma),0)
      FROM Dawcy 
      NATURAL JOIN  
      (SELECT d.pseudo_dawcy, sum(d.ilosc_krwi) as suma
      FROM Donacje d
      GROUP BY d.pseudo_dawcy)
      
      WHERE plec_dawcy = 'K'
      GROUP BY Dawcy.grupa_krwi)
        
    NATURAL JOIN

      (SELECT do.pseudo_dawcy, do.grupa_krwi
        FROM DAWCY do
        WHERE plec_dawcy = 'K')
      FROM Donacje dd JOIN Dawcy on dd.pseudo_dawcy = Dawcy.pseudo_dawcy
      WHERE plec_dawcy = 'K'
      GROUP BY Dawcy.grupa_krwi)
      
/* zad 13*/    
SELECT pseudo_wampira "wampir", da.pseudo_dawcy "zrudlo", ilosc_krwi "wypil ml"
FROM Donacje do join Dawcy da on do.pseudo_dawcy = da.pseudo_dawcy
WHERE plec_dawcy = 'K' and da.pseudo_dawcy = (select d.pseudo_dawcy
                                            FROM Donacje d
                                            WHERE d.pseudo_dawcy = da.pseudo_dawcy
                                            HAVING sum(d.ilosc_krwi) > 800
                                            GROUP BY d.pseudo_dawcy)
    AND NOT EXISTS (SELECT *
                    FROM Zlecenia
                    where do.pseudo_wampira = pseudo_wampira)

/* zad 14*/  
SELECT pseudo_dawcy "dawca", rocznik_dawcy + 5 "rocznik"
FROM Dawcy
WHERE grupa_krwi = '0'

/* zad 15*/
SELECT pseudo_wampira, pseudo_szefa, (SELECT wampir_w_rodzinie
                                      FROM Wampiry ww
                                      where ww.pseudo_wampira = w.pseudo_szefa) as szef_w_rodzinie,
                                      
                                      (SELECT pseudo_szefa
                                      FROM Wampiry ww
                                      where ww.pseudo_wampira = w.pseudo_szefa)as szef_szefa,
                                      
                                      (SELECT (SELECT wampir_w_rodzinie
                                                FROM Wampiry www
                                                where www.pseudo_wampira = ww.pseudo_szefa)
                                      FROM Wampiry ww
                                      WHERE ww.pseudo_wampira = w.pseudo_szefa)
                        
                                      
                                      
                                      
FROM Wampiry w 
ORDER BY 4,2

/* zad 16*/
SELECT DECODE(plec_wampira,'K','Wampirki','Wampiry') "plec", pod_drakula ,pod_wickiem, nvl(pod_Opojem,0) "pod_Opojem"
FROM (SELECT plec_wampira, sum(ilosc_krwi) as pod_drakula
        FROM Donacje natural join Wampiry
        WHERE pseudo_szefa = 'Drakula'
        GROUP BY plec_wampira)
    
    NATURAL JOIN
    (SELECT plec_wampira, sum(ilosc_krwi) as pod_wickiem
        FROM Donacje natural join Wampiry
        WHERE pseudo_szefa = 'Wicek'
        GROUP BY plec_wampira) 
    
   left join
    (SELECT plec_wampira, sum(ilosc_krwi) as pod_Opojem
        FROM Donacje natural join Wampiry
        WHERE pseudo_szefa = 'Opoj'
        GROUP BY plec_wampira) 
    using(plec_wampira)
