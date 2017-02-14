CREATE TABLE user (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    email text,
    passw text
);
 
CREATE TABLE rubr (
    id_rubr INTEGER PRIMARY KEY AUTOINCREMENT,
    name_rubr TEXT
);
 
CREATE TABLE site (
    id_site INTEGER PRIMARY KEY AUTOINCREMENT,
    is_user INTEGER,
    id_rubr INTEGER,
    url TEXT,
    title TEXT,
    iq INTEGER
);
