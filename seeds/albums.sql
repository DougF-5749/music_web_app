DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text,
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums(title, release_year, artist_id) VALUES ('Surface Sounds', 2021, 1);
INSERT INTO albums(title, release_year, artist_id) VALUES ('A/B', 2016, 1);

INSERT INTO artists(name, genre) VALUES ('Kaleo', 'Blues Rock');
INSERT INTO artists(name, genre) VALUES ('Sum 41', 'Punk Rock');