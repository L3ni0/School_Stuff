CREATE TABLE Koty(
pseudo_kota varchar(15) CONSTRAINT kt_pk PRIMARY KEY,
w_stadku_od date CONSTRAINT kt__wso_nn Not Null,
przydzial_myszy number(3) CONSTRAINT kt_pm_nn NOT NULL,
plec_kota char CONSTRAINT kt_plk_nn NOT NULL 
CONSTRAINT kt_plk_km CHECK(plec_kota IN('K','M')),
szef varchar(15),
nr_bandy number(15),
funkcja varchar(20) CONSTRAINT kt_f_nn NOT NULL,
CONSTRAINT kt_sz_PK FOREIGN KEY(szef) REFERENCES Koty(pseudo_kota),
CONSTRAINT kt_nrb_pk FOREIGN KEY(nr_bandy) REFERENCES Bandy(nr_bandy),
CONSTRAINT kt_f_pk FOREIGN KEY(funkcja) REFERENCES Funkcje(funkcja)
);

CREATE TABLE Myszy(
nr_myszy number(6) CONSTRAINT m_nrm_pk PRIMARY KEY,
waga_myszy number(3) CONSTRAINT m_wm_nn NOT NULL
CONSTRAINT m_w_ch CHECK(waga_myszy >= 10 and waga_myszy <999),
rozmiar_myszy number(2) CONSTRAINT m_rm_nn NOT NULL
CONSTRAINT m_rm_ch CHECK(rozmiar_myszy >= 10 and rozmiar_myszy <=100),
data_upolowania date,
data_wydania date,
lapacz varchar(15) CONSTRAINT m_l_nn NOT NULL,
zjadacz varchar(15),
CONSTRAINT m_l_fk FOREIGN KEY(lapacz) REFERENCES Koty(pseudo_kota),
CONSTRAINT m_zj_fk FOREIGN KEY(zjadacz) REFERENCES Koty(pseudo_kota),
CONSTRAINT m_dat_ch CHECK(data_upolowania <= data_wydania)
);

CREATE TABLE Bandy(
nr_bandy number(6) CONSTRAINT b_nrb_pk PRIMARY KEY,
nazwa_bandy varchar(15) CONSTRAINT b_nb_nn NOT NULL,
teren_bandy varchar(20) CONSTRAINT b_tb_nn NOT NULL,
dowodca varchar(15)
/* CONSTRAINT b_d_fk FOREIGN KEY(dowodca) REFERENCES Koty(pseudo_kota) */
);
ALTER TABLE Bandy
ADD CONSTRAINT d_b_fk FOREIGN KEY(dowodca) REFERENCES Koty(pseudo_kota);
/*constraint disable - zawieszenie po nazwie*/



CREATE TABLE Wrogowie(
imie_wroga varchar(15) CONSTRAINT w_iw_pk PRIMARY KEY,
stopien_wrogosci number(2) CONSTRAINT w_sw_ch CHECK(stopien_wrogosci >= 1 and stopien_wrogosci <= 10),
gatunek varchar(20)
);

CREATE TABLE Incydenty(
data_incydentu date CONSTRAINT i_di_nn NOT NULL,
opis_incydentu varchar(40) CONSTRAINT i_oi_nn NOT NULL,
pseudo_kota varchar(15),
imie_wroga varchar(15),
CONSTRAINT i_pk_fk FOREIGN KEY(pseudo_kota) REFERENCES Koty(pseudo_kota),
CONSTRAINT i_iw_fk FOREIGN KEY(imie_wroga) REFERENCES Wrogowie(imie_wroga),
CONSTRAINT i_pk PRIMARY KEY (pseudo_kota, imie_wroga) 
);

CREATE TABLE Funkcje(
funkcja varchar(20) CONSTRAINT f_f_pk PRIMARY KEY,
min_myszy number(6) CONSTRAINT f_mim_nn NOT NULL,
max_myszy number(6) CONSTRAINT f_mam_nn NOT NULL
);

CREATE TABLE Gratyfikacje(
gratyfikacja varchar(20) CONSTRAINT g_g_pk PRIMARY KEY
);


CREATE TABLE Gratyfikacje_wrogow(
gratyfikacja varchar(20),
imie_wroga varchar(15),
CONSTRAINT gw_g_fk FOREIGN KEY(gratyfikacja) REFERENCES Grafitykacje(gratyfikacja),
CONSTRAINT gw_iw_fk FOREIGN KEY(imie_wroga) REFERENCES Wrogowie(imie_wroga)
);