DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int
    artist_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surface Sounds', 2021, 1);