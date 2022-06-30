import csv


from cs50 import SQL 

open ("flicks.db","w").close()


db = SQL("sqlite:///flicks.db")

db.execute("CREATE TABLE movies (id INTEGER,title TEXT,PRIMARY KEY(id))")
db.execute("CREATE TABLE movies_genres (movies2_id INTEGER, genre_id INTEGER, PRIMARY KEY(genre_id), FOREIGN KEY(movies2_id) REFERENCES movies(id))")

db.execute("CREATE TABLE genre (genre_id INTEGER PRIMARY KEY, genre TEXT,FOREIGN KEY(genre_id) REFERENCES movies_genres(genre_id))")


with open("gross movies.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        title = row ["Film"].strip().capitalize()

        id=db.execute("INSERT INTO movies (title) VALUES(?)", title)

        for Genre in row["Genre"].split(","):
            genre=Genre.strip().capitalize()
            genre_id =db.execute("INSERT INTO movies_genres(movies2_id) VALUES((SELECT id FROM movies WHERE title =?))",title)
            db.execute("INSERT INTO genre (genre_id,genre) VALUES((SELECT genre_id FROM movies_genres WHERE movies2_id=?),?)",genre_id,genre)