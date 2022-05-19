CREATE TABLE Wampiry
(pseudo_wampira varchar(15) CONSTRAINT wam_pk PRIMARY KEY,
wampir_w_rodzinie date CONSTRAINT wam_dat NOT NULL,
plec_wampira char(1) CONSTRAINT wam_pl_nn NOT NULL
CONSTRAINT wam_pl CHECK(plec_wampira IN ('K','M')),
pseudo_szefa varchar(15) CONSTRAINT wam_ps_sz_f REFERENCES Wampiry(pseudo_wampira)
);

CREATE TABLE Zlecenia(
nr_zlecenia number(6) CONSTRAINT zl_pk PRIMARY KEY
CONSTRAINT zl_nrzl CHECK(nr_zlecenia > 0),
data_zlecenia date CONSTRAINT zl_dt NOT NULL,
pseudo_wampira VARCHAR(15) CONSTRAINT zl_pw_nn NOT NULL,
CONSTRAINT zl_pw_fk FOREIGN KEY (pseudo_wampira) REFERENCES Wampiry(pseudo_wampira)
);

CREATE TABLE Dawcy(
pseudo_dawcy varchar(15) CONSTRAINT da_ps_pk PRIMARY KEY,
rocznik_dawcy number(4) CONSTRAINT da_rd NOT NULL,
plec_dawcy char(1) CONSTRAINT da_pl_nn NOT NULL
CONSTRAINT da_pl CHECK(plec_dawcy in('K','M')),
grupa_krwi varchar(2) CONSTRAINT da_gr_kw NOT NULL
CONSTRAINT da_gr_in CHECK(grupa_krwi in ('0','A','B','AB'))
);


CREATE TABLE Donacje(
nr_zlecenia number(6), 
pseudo_dawcy varchar(15),
data_oddania date CONSTRAINT do_d_nn NOT NULL,
ilosc_krwi number(3) CONSTRAINT do_ik NOT NULL,
pseudo_wampira varchar(15),
data_wydania date, CONSTRAINT do_dw CHECK(data_wydania >= data_oddania),
CONSTRAINT do_pw_fk FOREIGN KEY (pseudo_wampira) REFERENCES Wampiry(pseudo_wampira),
CONSTRAINT do_zl_pk PRIMARY KEY(nr_zlecenia, pseudo_dawcy),
CONSTRAINT do_zl_fk FOREIGN KEY (nr_zlecenia) REFERENCES Zlecenia(nr_zlecenia),
CONSTRAINT do_zl_fk2 FOREIGN KEY (pseudo_dawcy) REFERENCES DAWCY(pseudo_dawcy)
)

CREATE TABLE Sprawnosci(
sprawnosc varchar(20)CONSTRAINT sp_sp_pk PRIMARY KEY
)

CREATE TABLE Sprawnosci_w(
pseudo_wampira varchar(15),
sprawnosc varchar(20),
sprawnosc_od date CONSTRAINT sp_od NOT NULL,
CONSTRAINT sp_pw_fk FOREIGN KEY (pseudo_wampira) REFERENCES Wampiry(pseudo_wampira),
CONSTRAINT sp_sp_fk FOREIGN KEY (sprawnosc) REFERENCES Sprawnosci(sprawnosc),
CONSTRAINT sp_pss_pk PRIMARY KEY (pseudo_wampira, sprawnosc)
)

CREATE TABLE Jezyki_obce(
jezyk_obcy varchar(20) CONSTRAINT jo_jo_pk PRIMARY KEY
)

CREATE TABLE Jezyki_obcje_w(
pseudo_wampira varchar(15),
jezyk_obcy varchar(20),
jezyk_obcy_od date CONSTRAINT jo_jod_nn NOT NULL,
CONSTRAINT jo_ps_fk FOREIGN KEY (pseudo_wampira) REFERENCES Wampiry(pseudo_wampira),
CONSTRAINT jo_jo_fk FOREIGN KEY (jezyk_obcy) REFERENCES Jezyki_obce(jezyk_obcy),
CONSTRAINT jo_pk PRIMARY KEY (pseudo_wampira, jezyk_obcy)
)

ALTER SESSION SET NLS_DATE_FORMAT = 'dd.mm.yyyy'

INSERT INTO Wampiry VALUES
('Drakula','12.12.1217','M',NULL);
INSERT INTO Wampiry VALUES
('Opoj','07.11.1777','M','Drakula');
INSERT INTO Wampiry VALUES
('Wicek','11.11.1721','M','Drakula');
INSERT INTO Wampiry VALUES
('Baczek','13.04.1855','M','Opoj');
INSERT INTO Wampiry VALUES
('Bolek','31.05.1945','M','Opoj');
INSERT INTO Wampiry VALUES
('Gacek','21.02.1891','M','Wicek');
INSERT INTO Wampiry VALUES
('Pijawka','03.11.1901','K','Wicek');
INSERT INTO Wampiry VALUES
('Czerwony','13.09.1823','M','Wicek');
INSERT INTO Wampiry VALUES
('Komar','23.07.1911','M','Wicek');
INSERT INTO Wampiry VALUES
('Zyleta','23.09.1911','K','Opoj');
INSERT INTO Wampiry VALUES
('Predka','29.03.1877','K','Drakula');

INSERT INTO Zlecenia VALUES
(221,'04.07.2005','Opoj');
INSERT INTO Zlecenia VALUES
(222,'04.07.2005','Baczek');
INSERT INTO Zlecenia VALUES
(223,'17.07.2005','Bolek');
INSERT INTO Zlecenia VALUES
(224,'22.07.2005','Opoj');
INSERT INTO Zlecenia VALUES
(225,'01.08.2005','Pijawka');
INSERT INTO Zlecenia VALUES
(226,'07.08.2005','Gacek');

INSERT INTO Dawcy VALUES
('Slodka',1966,'K','AB');
INSERT INTO Dawcy VALUES
('Miodzio',1983,'M','B');
INSERT INTO Dawcy VALUES
('Gorzka',1958,'K','0');
INSERT INTO Dawcy VALUES
('Lolita',1987,'K','0');
INSERT INTO Dawcy VALUES
('Wytrawny',1971,'M','A');
INSERT INTO Dawcy VALUES
('Okocim',1966,'M','B');
INSERT INTO Dawcy VALUES
('Adonis',1977,'M','AB');
INSERT INTO Dawcy VALUES
('Zywiec',1969,'M','A');
INSERT INTO Dawcy VALUES
('Eliksir',1977,'M','0');
INSERT INTO Dawcy VALUES
('Zenek',1959,'M','B');
INSERT INTO Dawcy VALUES
('Zoska',1963,'K','0');
INSERT INTO Dawcy VALUES
('Czerwonka',1953,'M','A');

INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(221,'Slodka','04.07.2005',455,'Drakula','06.08.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(221,'Miodzio','04.07.2005',680,'Gacek','15.08.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(221,'Gorzka','05.07.2005',471,'Pijawka','11.08.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(221,'Lolita','05.07.2005',340,'Czerwony','21.08.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(222,'Wytrawny','07.07.2005',703,'Drakula','17.07.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(222,'Okocim','07.07.2005',530,'Komar','01.09.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(222,'Adonis','08.07.2005',221,'Zyleta','11.09.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(223,'Zywiec','17.07.2005',587,'Wicek','18.09.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(224,'Gorzka','22.07.2005',421,'Drakula','23.08.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(224,'Eliksir','25.07.2005',377,'Predka','26.07.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(225,'Zenek','04.08.2005',600,'Opoj','15.08.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(225,'Zoska','06.08.2005',450,NULL,NULL);
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(226,'Czerwonka','10.08.2005',517,'Pijawka','30.09.2005');
INSERT INTO Donacje(nr_zlecenia,pseudo_dawcy,data_oddania,ilosc_krwi,pseudo_wampira,data_wydania) VALUES
(226,'Miodzio','11.08.2005',644,NULL,NULL);

INSERT INTO Sprawnosci(sprawnosc) VALUES
('podryw');
INSERT INTO Sprawnosci(sprawnosc) VALUES
('gorzala');
INSERT INTO Sprawnosci(sprawnosc) VALUES
('kasa');
INSERT INTO Sprawnosci(sprawnosc) VALUES
('przymus');
INSERT INTO Sprawnosci(sprawnosc) VALUES
('niesmiertelnosc');

INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Drakula','podryw','12.12.1217');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Drakula','gorzala','12.12.1217');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Wicek','kasa','11.11.1721');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Wicek','przymus','07.01.1771');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Opoj','podryw','07.11.1777');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Czerwony','niesmiertelnosc','13.09.1823');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Drakula','kasa','13.09.1823');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Opoj','gorzala','11.12.1844');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Baczek','gorzala','13.04.1855');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Drakula','przymus','14.06.1857');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Drakula','niesmiertelnosc','21.08.1858');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Opoj','przymus','15.07.1861');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Wicek','gorzala','19.01.1866');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Predka','podryw','29.03.1877');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Czerwony','kasa','03.02.1891');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Gacek','kasa','21.02.1891');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Pijawka','podryw','03.11.1901');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Komar','gorzala','23.07.1911');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Zyleta','przymus','23.09.1911');
INSERT INTO Sprawnosci_w(pseudo_wampira,sprawnosc,sprawnosc_od) VALUES
('Bolek','gorzala','31.05.1945');


INSERT INTO Jezyki_obce VALUES
('niemiecki');
INSERT INTO Jezyki_obce VALUES
('wegierski');
INSERT INTO Jezyki_obce VALUES
('bulgarski');
INSERT INTO Jezyki_obce VALUES
('rosyjski');
INSERT INTO Jezyki_obce VALUES
('portugalski');
INSERT INTO Jezyki_obce VALUES
('francuski');
INSERT INTO Jezyki_obce VALUES
('angielski');
INSERT INTO Jezyki_obce VALUES
('polski');
INSERT INTO Jezyki_obce VALUES
('hiszpanski');
INSERT INTO Jezyki_obce VALUES
('czeski');
INSERT INTO Jezyki_obce VALUES
('wloski');
INSERT INTO Jezyki_obce VALUES
('szwedzki');


INSERT INTO Jezyki_obcje_w VALUES
('Drakula','niemiecki','12.12.1217');
INSERT INTO Jezyki_obcje_w VALUES
('Drakula','wegierski','12.12.1217');
INSERT INTO Jezyki_obcje_w VALUES
('Drakula','bulgarski','03.04.1455');
INSERT INTO Jezyki_obcje_w VALUES
('Wicek','rosyjski','11.11.1721');
INSERT INTO Jezyki_obcje_w VALUES
('Opoj','portugalski','07.11.1777');
INSERT INTO Jezyki_obcje_w VALUES
('Czerwony','francuski','13.09.1823');
INSERT INTO Jezyki_obcje_w VALUES
('Drakula','angielski','13.09.1823');
INSERT INTO Jezyki_obcje_w VALUES
('Wicek','polski','18.08.1835');
INSERT INTO Jezyki_obcje_w VALUES
('Opoj','hiszpanski','12.03.1851');
INSERT INTO Jezyki_obcje_w VALUES
('Baczek','czeski','13.04.1855');
INSERT INTO Jezyki_obcje_w VALUES
('Wicek','niemiecki','11.06.1869');
INSERT INTO Jezyki_obcje_w VALUES
('Wicek','wloski','14.03.1873');
INSERT INTO Jezyki_obcje_w VALUES
('Predka','czeski','29.03.1877');
INSERT INTO Jezyki_obcje_w VALUES
('Opoj','polski','13.09.1883');
INSERT INTO Jezyki_obcje_w VALUES
('Czerwony','rosyjski','23.11.1888');
INSERT INTO Jezyki_obcje_w VALUES
('Gacek','polski','21.02.1891');
INSERT INTO Jezyki_obcje_w VALUES
('Predka','niemiecki','07.06.1894');
INSERT INTO Jezyki_obcje_w VALUES
('Baczek','angielski','04.12.1899');
INSERT INTO Jezyki_obcje_w VALUES
('Pijawka','angielski','03.11.1901');
INSERT INTO Jezyki_obcje_w VALUES
('Komar','szwedzki','23.07.1911');
INSERT INTO Jezyki_obcje_w VALUES
('Zyleta','angielski','23.09.1911');
INSERT INTO Jezyki_obcje_w VALUES
('Bolek','francuski','31.05.1945');




