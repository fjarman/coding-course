DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS professions;
DROP TABLE IF EXISTS people_professions;
DROP TABLE IF EXISTS title_types;
DROP TABLE IF EXISTS titles;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS title_genres;
DROP TABLE IF EXISTS people_known_for_titles;
DROP TABLE IF EXISTS title_directors;
DROP TABLE IF EXISTS title_writers;
DROP TABLE IF EXISTS title_episodes;
DROP TABLE IF EXISTS title_participants;
DROP TABLE IF EXISTS ratings;

CREATE TABLE people
(
    id         TEXT PRIMARY KEY NOT NULL,
    name       TEXT NOT NULL,
    birth_year INTEGER  NOT NULL,
    death_year INTEGER
);

CREATE TABLE professions
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    profession TEXT NOT NULL
);

CREATE TABLE people_professions
(
    people_id      TEXT NOT NULL,
    professions_id INTEGER  NOT NULL,
    FOREIGN KEY (people_id) REFERENCES people (id),
    FOREIGN KEY (professions_id) REFERENCES professions (id)
);
CREATE INDEX people_professions_people_idx ON people_professions (people_id);
CREATE INDEX people_professions_professions_idx ON people_professions (professions_id);

CREATE TABLE titles
(
    id               TEXT NOT NULL,
    title_type       TEXT  NOT NULL,
    primary_title    TEXT NOT NULL,
    original_title   TEXT,
    is_adult         BOOLEAN,
    start_year       INTEGER,
    end_year         INTEGER,
    run_time_minutes INTEGER,
    FOREIGN KEY (title_type) REFERENCES title_types (id)
);
CREATE INDEX titles_primary_idx ON titles (primary_title);
CREATE INDEX titles_start_year_idx ON titles (start_year);
CREATE INDEX titles_runtime_idx ON titles (run_time_minutes);

CREATE TABLE genres
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    genre TEXT NOT NULL
);

CREATE TABLE title_genres
(
    title_id TEXT NOT NULL,
    genre_id INTEGER  NOT NULL,
    FOREIGN KEY (title_id) REFERENCES titles (id),
    FOREIGN KEY (genre_id) REFERENCES genres (id)
);
CREATE INDEX title_genres_title_idx ON title_genres (title_id);
CREATE INDEX title_genres_genre_idx ON title_genres (genre_id);

CREATE TABLE people_known_for_titles
(
    people_id TEXT NOT NULL,
    title_id  TEXT NOT NULL,
    FOREIGN KEY (people_id) REFERENCES people (id),
    FOREIGN KEY (title_id) REFERENCES titles (id)
);
CREATE INDEX people_known_for_titles_people_idx ON people_known_for_titles (people_id);
CREATE INDEX people_known_for_titles_professions_idx ON people_known_for_titles (title_id);

CREATE TABLE title_directors
(
    people_id TEXT NOT NULL,
    title_id  TEXT NOT NULL,
    FOREIGN KEY (people_id) REFERENCES people (id),
    FOREIGN KEY (title_id) REFERENCES titles (id)
);
CREATE INDEX title_directors_people_idx ON title_directors (people_id);
CREATE INDEX title_directors_title_idx ON title_directors (title_id);

CREATE TABLE title_writers
(
    people_id TEXT NOT NULL,
    title_id  TEXT NOT NULL,
    FOREIGN KEY (people_id) REFERENCES people (id),
    FOREIGN KEY (title_id) REFERENCES titles (id)
);
CREATE INDEX title_writers_people_idx ON title_writers (people_id);
CREATE INDEX title_writers_title_idx ON title_writers (title_id);

CREATE TABLE title_episodes
(
    series_id      TEXT NOT NULL,
    episode_id     TEXT NOT NULL,
    season_number  INTEGER,
    episode_number INTEGER,
    FOREIGN KEY (series_id) REFERENCES titles (id),
    FOREIGN KEY (episode_id) REFERENCES titles (id)
);
CREATE INDEX title_episodes_series_idx ON title_episodes (series_id);
CREATE INDEX title_episodes_episode_idx ON title_episodes (episode_id);

CREATE TABLE title_participants(
    title_id TEXT NOT NULL,
    ordering INTEGER NOT NULL,
    people_id TEXT NOT NULL,
    profession_id INTEGER,
    characters TEXT,
    FOREIGN KEY(title_id) REFERENCES titles(id),
    FOREIGN KEY(people_id) REFERENCES people(id),
    FOREIGN KEY(profession_id) REFERENCES professions(id)
);

CREATE INDEX title_participants_title_idx ON title_participants (title_id);
CREATE INDEX title_participants_people_idx ON title_participants (people_id);
CREATE INDEX title_participants_profession_idx ON title_participants (profession_id);

CREATE TABLE ratings(
    title_id TEXT PRIMARY KEY NOT NULL,
    average_rating DECIMAL NOT NULL,
    num_votes INTEGER NOT NULL,
    FOREIGN KEY(title_id) REFERENCES titles(id)
);
CREATE INDEX ratings_average_idx ON ratings(average_rating);
CREATE INDEX ratings_num_votes_idx ON ratings(num_votes);
CREATE INDEX ratings_average_num_votes_idx ON ratings(average_rating, num_votes);