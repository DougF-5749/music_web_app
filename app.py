import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/music_store', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, "Back in Black", 1980, 2)
    album = repository.create(album)
    return "Album successfully added!"

@app.route('/music_store')
def get_all_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join([
            str(album) for album in repository.all()
        ])

@app.route('/artists')
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return ", ".join([
            artist.name for artist in repository.all()
        ])

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    return "Artist successfully added"



# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

