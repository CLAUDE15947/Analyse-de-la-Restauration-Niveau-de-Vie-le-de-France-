-- init_db.sql
CREATE TABLE restaurants_paris (
    -- Clé primaire et infos restaurant
    id_restaurant INT AUTO_INCREMENT PRIMARY KEY,
    nom_restaurant VARCHAR(150) NOT NULL,
    prix_moyen DECIMAL(10, 2),
    rating DECIMAL(2, 1),
    nb_notes INT,
    adresse VARCHAR(255),
    ville VARCHAR(100),
    main_category VARCHAR(100),
    commune VARCHAR(50),
    code_postal CHAR(5),
    arrondissement TINYINT,
    zone_paris VARCHAR(20),
    
    -- Infos INSEE (Codes et Noms)
    insee_from_cp VARCHAR(10),
    insee_com VARCHAR(10),
    nom_arrondissement VARCHAR(100),
    
    -- Indicateurs Socio-Démographiques (DECIMAL pour la précision)
    pop_totale INT,                     -- POP
    pop_3_20_ans DECIMAL(10, 2),        -- Population_3_20
    nb_familles DECIMAL(10, 2),         -- C20_FAM
    nb_familles_mono DECIMAL(10, 2),    -- C20_FAMMONO
    part_pop_3_20 DECIMAL(10, 5),       -- QL3_20
    part_fam_mono DECIMAL(10, 5),       -- QLFMONO
    revenu_median DECIMAL(10, 2),       -- RDISP_MED
    taux_bac DECIMAL(10, 5),            -- tx_BAC
    taux_ouvrier DECIMAL(10, 5),        -- tx_O
    taux_chomage DECIMAL(10, 5),        -- tx_Chom
    facteur_deprivation DECIMAL(10, 5), -- FDep
    part_apl DECIMAL(10, 5)             -- APL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;