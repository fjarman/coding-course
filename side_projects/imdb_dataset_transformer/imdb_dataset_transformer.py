import csv
import sqlite3
from fileinput import close
from math import trunc

DB_PATH = '/Users/subhe/DataGripProjects/movie_data/movie_base.sql'


IMDB_DATA_PATH = '/Users/subhe/Downloads/imdb_data'
BATCH_SIZE = 100000

def read_tsv_file(file_path, raw_mapper, batch_raw_processor):
    with open(file_path, newline='', encoding='utf-8') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        next(reader, None)
        rows = []
        i = 0
        batch_number = 0
        for row in reader:
            if i == BATCH_SIZE:
                batch_raw_processor(rows)
                i = 0
                batch_number += 1
                rows = []
                print('Processed first ' + str(batch_number * BATCH_SIZE) + ' rows')
            rows.extend(raw_mapper(row))
            i += 1
        batch_raw_processor(rows)

def bulk_insert(query, data, conn):
    cursor = conn.cursor()
    try:
        cursor.executemany(query, data)
        conn.commit()
        print('Bulk ' + query  + 'insert completed successfully!')
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

def init_people():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        res = cur.execute("SELECT count(*) FROM people").fetchone()
        if res[0] > 0:
            print('people table is already initialised')
            return

        def raw_mapper(row):
            return [(row[0],
                    row[1],
                    row[2],
                    row[3] if row[3] != '\\N' else None)]

        def process_rows(rows):
            query = 'INSERT INTO people(id, name, birth_year, death_year) VALUES (?, ?, ?, ?)'
            bulk_insert(query, rows, conn)

        read_tsv_file(IMDB_DATA_PATH + '/name.basics.tsv', raw_mapper, process_rows)
    finally:
        conn.close()


def init_professions():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        res = cur.execute("SELECT count(*) FROM professions").fetchone()
        if res[0] > 0:
            print('professions table is already initialised')
            return
        professions = {}
        def raw_mapper(row):
            return [str(row[4]).split(',')]

        def process_rows(rows):
            for row in rows:
                for prof in row:
                    if prof not in professions.keys():
                        if prof != '\\N':
                            professions[prof] = True

        read_tsv_file(IMDB_DATA_PATH + '/name.basics.tsv', raw_mapper, process_rows)
        query = 'INSERT INTO professions(profession) VALUES (?)'
        data = []
        for profession in professions.keys():
            data.append((profession,))
        bulk_insert(query, data, conn)
    finally:
        conn.close()


def init_people_professions():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        res = cur.execute("SELECT count(*) FROM people_professions").fetchone()
        if res[0] > 0:
            print('people_professions table is already initialised')
            return
        res = cur.execute("SELECT id, profession FROM professions").fetchall()
        professions_dict = {}
        for prof in res:
            professions_dict[prof[1]] = prof[0]

        def raw_mapper(row):
            professions = str(row[4]).split(',')
            data = []
            for profession in professions:
                if professions_dict[profession] is not None:
                    data.append((row[0], professions_dict[profession]))
            return data

        def process_rows(rows):
            query = 'INSERT INTO people_professions(people_id, professions_id) VALUES (?, ?)'
            bulk_insert(query, rows, conn)

        read_tsv_file(IMDB_DATA_PATH + '/name.basics.tsv', raw_mapper, process_rows)
    finally:
        conn.close()




def init_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open('schema.sql', 'r') as file:
        ddl_script = file.read()
    try:
        cursor.executescript(ddl_script)
        print("Database initialized successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    conn.commit()
    conn.close()

def launch():
    # init_schema()
    init_people()
    init_professions()
    init_people_professions()

if __name__ == '__main__':
    launch()