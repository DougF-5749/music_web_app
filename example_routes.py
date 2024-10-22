from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from flask import request

# You won't need to nest your routes in app.py in a method like this
def apply_example_routes(app):
    # GET /albums
    # Returns a list of albums
    @app.route('/albums', methods=['GET'])
    def get_albums():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        return "\n".join([
            str(album) for album in repository.all()
        ])


    # GET /albums/<id>
    # Returns a single album
    @app.route('/albums/<int:id>', methods=['GET'])
    def get_album(id):
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        return str(repository.find(id))


    # POST /albums
    # Creates a new album
    @app.route('/albums', methods=['POST'])
    def create_album():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        album = Album(None, request.form['title'], request.form['author_name'])
        album = repository.create(album)
        return "Album added successfully"


    # DELETE /albums/<id>
    # Deletes a album
    @app.route('/albums/<int:id>', methods=['DELETE'])
    def delete_album(id):
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        repository.delete(id)
        return "Album deleted successfully"
