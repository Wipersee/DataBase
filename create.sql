---CREATING TABLES-----
CREATE TABLE game(
game_rank INTEGER PRIMARY KEY,
genre_id INTEGER UNIQUE,
company_id INTEGER UNIQUE,
platform_id INTEGER UNIQUE,
year_id INTEGER UNIQUE,
name_of_game VARCHAR2(256)
);
CREATE TABLE sales(
NA_sales DECIMAL,
EU_sales DECIMAL,
JP_sales DECIMAL,
Other_sales DECIMAL,
game_rank INTEGER 
);
CREATE TABLE genre(
genre VARCHAR2(256),
genre_id INTEGER PRIMARY KEY
);
CREATE TABLE release_year(
year_id INTEGER PRIMARY KEY,
realease_year INTEGER
);
CREATE TABLE platform(
platform_id INTEGER PRIMARY KEY,
platfrom VARCHAR2(256)
);
CREATE TABLE companies(
company_id INTEGER PRIMARY KEY,
company VARCHAR2(256)
);


---ALTER TABLE WITH FOREIGN KEYS---
ALTER TABLE game
ADD CONSTRAINT fk_genre_id
  FOREIGN KEY (genre_id)
  REFERENCES genre(genre_id);
  
ALTER TABLE game
ADD CONSTRAINT fk_company_id
  FOREIGN KEY (company_id)
  REFERENCES companies(company_id);
  
ALTER TABLE game
ADD CONSTRAINT fk_platform_id
  FOREIGN KEY (platform_id)
  REFERENCES platform(platform_id);
  
ALTER TABLE game
ADD CONSTRAINT fk_year_id
  FOREIGN KEY (year_id)
  REFERENCES release_year(year_id);  
  
ALTER TABLE sales
ADD CONSTRAINT fk_game_rank
  FOREIGN KEY (game_rank)
  REFERENCES game(game_rank);    
