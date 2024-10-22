from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/albums.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, "Invisible Cities", "Italo Calvino"),
        Album(2, "The Man Who Was Thursday", "GK Chesterton"),
        Album(3, "Bluets", "Maggie Nelson"),
        Album(4, "No Place on Earth", "Christa Wolf"),
        Album(5, "Nevada", "Imogen Binnie"),
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/album_store.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album == Album(3, "Bluets", "Maggie Nelson")

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/album_store.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "The Great Gatsby", "F. Scott Fitzgerald"))

    result = repository.all()
    assert result == [
        Album(1, "Invisible Cities", "Italo Calvino"),
        Album(2, "The Man Who Was Thursday", "GK Chesterton"),
        Album(3, "Bluets", "Maggie Nelson"),
        Album(4, "No Place on Earth", "Christa Wolf"),
        Album(5, "Nevada", "Imogen Binnie"),
        Album(6, "The Great Gatsby", "F. Scott Fitzgerald"),
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/album_store.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3) # Apologies to Maggie Nelson fans

    result = repository.all()
    assert result == [
        Album(1, "Invisible Cities", "Italo Calvino"),
        Album(2, "The Man Who Was Thursday", "GK Chesterton"),
        Album(4, "No Place on Earth", "Christa Wolf"),
        Album(5, "Nevada", "Imogen Binnie"),
    ]
