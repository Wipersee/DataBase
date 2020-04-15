CREATE TABLE Game(
    name_of_game VARCHAR2(256) PRIMARY KEY,
    rank INTEGER UNIQUE,
    NA_sales DECIMAL NOT NULL,
    EU_sales DECIMAL NOT NULL,
    JP_sales DECIMAL NOT NULL,
    Other_sales DECIMAL NOT NULL
);
CREATE TABLE Genre(
    genre VARCHAR2(256),
    name_of_game VARCHAR2(256),
    CONSTRAINT FK_genre FOREIGN KEY (name_of_game)
    REFERENCES Game(name_of_game)
);

CREATE TABLE Year(
    release_year VARCHAR2(30),
    name_of_game VARCHAR2(256),
    CONSTRAINT FK_year FOREIGN KEY (name_of_game)
    REFERENCES Game(name_of_game)
);

CREATE TABLE Companies(
    company VARCHAR2(256) PRIMARY KEY,
    name_of_game VARCHAR2(256),
    CONSTRAINT FK_company FOREIGN KEY (name_of_game)
    REFERENCES Game(name_of_game)
);

CREATE TABLE Platform(
    platform VARCHAR2(256),
    company VARCHAR2(256),
    CONSTRAINT FK_platform FOREIGN KEY (platform)
    REFERENCES Companies(company)
);