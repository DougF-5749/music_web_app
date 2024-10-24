from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, "Surface Sounds", 2021, 1),
        Album(2, "A/B", 2016, 1),
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(2)
    assert album == Album(2, "A/B", 2016, 1)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Back in Black", 1980, 2))

    result = repository.all()
    assert result == [
        Album(1, "Surface Sounds", 2021, 1),
        Album(2, "A/B", 2016, 1),
        Album(3, "Back in Black", 1980, 2),
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_store.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(2) # Apologies to Maggie Nelson fans

    result = repository.all()
    assert result == [
        Album(1, "Surface Sounds", 2021, 1)
    ]
