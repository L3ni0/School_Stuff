SELECT plec_wampira
FROM (SELECT plec_wampira, sum(ilosc_krwi)"pod drakula"
        FROM Donacje natural join Wampiry
        WHERE pseudo_szefa = 'Drakula'
        GROUP BY plec_wampira)
    
    NATURAL JOIN
    (SELECT plec_wampira, sum(ilosc_krwi)"pod wickiem"
        FROM Donacje natural join Wampiry
        WHERE pseudo_szefa = 'Wicek'
        GROUP BY plec_wampira) 
    
   left join
    (SELECT plec_wampira, nvl(sum(ilosc_krwi),0)"pod Opojem"
        FROM Donacje natural join Wampiry
        WHERE pseudo_szefa = 'Opoj'
        GROUP BY plec_wampira) 
    using(plec_wampira)
    
      
