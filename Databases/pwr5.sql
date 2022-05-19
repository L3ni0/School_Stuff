 ALTER SESSION SET NLS_DATE_FORMAT = 'dd.mm.yyyy'
 
 
INSERT INTO Funkcje Values
('kucharz',10,25);

INSERT INTO Funkcje Values
('szef',80, 90);

INSERT INTO Funkcje Values
('sprzatacz',10, 20);

INSERT INTO Funkcje Values
('bankier',20,40);

INSERT INTO Funkcje Values
('opiekun kociat',15,30);

INSERT INTO Funkcje Values
('ochroniarz',30,60);

INSERT INTO Funkcje Values
('organizator',25,50);

INSERT INTO Funkcje Values
('dostawca',30,50);

INSERT INTO Funkcje Values
('gratyfikator',40,70);

INSERT INTO Funkcje Values
('lapacz',10,30);


/* bandy */

INSERT INTO Bandy Values
(1,'zausznicy','wszytko','tygrys');

INSERT INTO Bandy Values
(2,'szaraki','smietniki','bili');

INSERT INTO Bandy Values
(3,'zakolaki','za fryzjerem','lysy');

INSERT INTO Bandy Values
(4,'pazury','sklepy','pan puszek');

INSERT INTO Bandy Values
(5,'ogoniaki','centrum','pan kot');

INSERT INTO Bandy Values
(6,'siersciuchy', 'kosciol','gruby');

INSERT INTO Bandy Values
(7,'lapki', 'domy','kicia');

INSERT INTO Bandy Values
(8,'dachowce','rzeczka','ricardo');

INSERT INTO Bandy Values
(9,'dzikusy', 'pole','biala');

INSERT INTO Bandy Values
(10, 'lapacze', 'stodoly','coco');




/* koty */
INSERT INTO Koty Values
('tygrys','25.01.2013', 90, 'M', Null, 1, 'szef');

INSERT INTO Koty Values
('pan puszek','01.01.2014',60,'M','tygrys',4,'gratyfikator');

INSERT INTO Koty Values
('pan kot','20.02.2015',45,'M','tygrys',5,'dostawca');

INSERT INTO Koty Values
('gruby','22.06.2019',40,'M','tygrys',6,'organizator');

INSERT INTO Koty Values
('kicia','11.07.2017',30,'K','tygrys',7,'bankier');

INSERT INTO KOTY Values
('ricarco','31.3.2014',48,'M','tygrys',8,'ochroniarz');

INSERT INTO Koty Values
('bili','09.03.2014',55,'M','tygrys',2,'gratyfikator');

INSERT INTO Koty Values
('biala','13.11.2015',24,'K','tygrys',9,'opiekun kociat');

INSERT Into Koty Values
('coco','26.12.2016',45,'K','tygrys',10,'dostawca');

INSERT INTO Koty Values
('lysy','10.09.2015',25,'M','tygrys',3,'kucharz');

/*podrzedne koty */

INSERT INTO Koty Values
('tosia','28.05.2017',15,'K','biala',9,'sprzatacz');

INSERT INTO Koty Values
('oli','18,07.2017',10,'M','lysy',3,'lapacz');

INSERT INTO Koty Values
('kropka','05.04.2018',18,'K','kicia',7,'lapacz');

INSERT INTO Koty Values
('ares','21.12.2018',30,'M','tygrys',1,'lapacz');

INSERT INTO Koty Values
('rudy','19.04.2019',22,'M','gruby',6,'lapacz');

INSERT INTO Koty Values
('lola','15.06.2019',14,'K','pan kot',5,'lapacz');

/*gratyfikacje*/
INSERT INTO Gratyfikacje Values
('kocimetka');

INSERT INTO Gratyfikacje Values
('krakersy');

INSERT INTO Gratyfikacje Values
('kocia trawa');

INSERT INTO Gratyfikacje Values
('zakretki');

INSERT INTO Gratyfikacje Values
('sznurek');

INSERT INTO Gratyfikacje Values
('wloczka');

INSERT INTO Gratyfikacje Values
('karma');

INSERT INTO Gratyfikacje Values
('pilka');

INSERT INTO Gratyfikacje Values
('piorka');

INSERT INTO Gratyfikacje Values
('gumka');

/*wrogowie*/
INSERT INTO Wrogowie Values
('pimpek',1,'shistu');

INSERT INTO Wrogowie Values
('burek',9,null);

INSERT INTO Wrogowie Values
('maks',5,'owczarek');

INSERT INTO Wrogowie Values
('balbina',6,'ges');

INSERT INTO Wrogowie Values
('baska',3,'koza');

INSERT INTO Wrogowie Values
('stefan',4,'koziol');

INSERT INTO Wrogowie Values
('lucian',5,'labedz');

INSERT INTO Wrogowie Values
('furia',7,null);

INSERT INTO Wrogowie Values
('ela',1,'krowa');

INSERT INTO Wrogowie Values
('michal',2,'czlowiek');

/* incydenty */
INSERT INTO Incydenty Values
('13.09.2022','lola wskoczyla na ele','lola','ela');

INSERT INTO Incydenty Values
('22.01.2021','grubego zaskoczyl maly michal','gruby','michal');

INSERT INTO Incydenty Values
('06.07.2021','oli polowal obok budy pimpka','oli','pimpek');

INSERT INTO Incydenty Values
('01.01.2019','wystraszona balbina wpadla na bilego','bili','balbina');

INSERT INTO Incydenty Values
('28.02.2018','lola wdala sie w bujke z burkiem','lola','burek');

INSERT INTO Incydenty Values
('14.09.2019','ricardo walczyl o teren z lucianem','ricarco','lucian');

INSERT INTO Incydenty Values
('09.02.2018','stefan zabral coco pilke','coco','stefan');

INSERT INTO Incydenty VAlues
('04.04.2019','furia probowala zapolowac na rudego','rudy','furia');

INSERT INTO Incydenty VAlues
('12.03.2019','kicia nie poszla gratyfikacja maksa','kicia','maks');

INSERT INTO Incydenty VAlues
('17.09.2020','baska chciala zjesc wloczke tysego','lysy','baska');

/*gratyfikacja wrogow*/
INSERT INTO Gratyfikacje_wrogow Values
('kocia trawa','balbina');

INSERT INTO Gratyfikacje_wrogow Values
('sznurek','burek');

INSERT INTO Gratyfikacje_wrogow Values
('krakersy','burek');

INSERT INTO Gratyfikacje_wrogow Values
('pilka','burek');

INSERT INTO Gratyfikacje_wrogow Values
('zakretki','pimpek');

INSERT INTO Gratyfikacje_wrogow Values
('krakersy','lucian');

INSERT INTO Gratyfikacje_wrogow Values
('piorka','furia');

INSERT INTO Gratyfikacje_wrogow Values
('kocia trawa','ela');

INSERT INTO Gratyfikacje_wrogow Values
('kocimietka','stefan');

INSERT INTO Gratyfikacje_wrogow Values
('wloczka','burek');

/* myszy */

INSERT INTO myszy Values
(1,20,30,'01.01.2022','02.01.2022','tygrys','tygrys');

INSERT INTO myszy Values
(2,10,25,'01.01.2022','01.02.2022','pan puszek','lysy');

INSERT INTO myszy(nr_myszy,waga_myszy, rozmiar_myszy, data_upolowania, lapacz) Values
(3,40,45,'02.01.2022','lysy');

INSERT INTO myszy(nr_myszy,waga_myszy, rozmiar_myszy, data_upolowania, lapacz) Values
(4,13,22,'01.01.2022','kicia');

INSERT INTO myszy(nr_myszy,waga_myszy, rozmiar_myszy, data_upolowania, lapacz) Values
(5,16,33,'04.01.2022','coco');

INSERT INTO myszy Values
(6,20,19,'05.01.2022','08.01.2022','kropka','tygrys');

INSERT INTO myszy Values
(7,20,35,'06.02.2022','20.02.2022','biala','bili');

INSERT INTO myszy Values
(8,13,22,'08.03.2022','01.04.2022','gruby','lola');

INSERT INTO myszy Values
(9,19,27,'22.03.2022','22.03.2022','kicia','rudy');

INSERT INTO myszy Values
(10,30,60,'03.04.2022','05.04.2022','oli','biala');

INSERT INTO myszy Values
(11,26,33,'06.04.2022','06.05.2022','pan kot','pan puszek');

INSERT INTO myszy Values
(12,24,28,'12.04.2022','20.04.2022','ares','tygrys');

