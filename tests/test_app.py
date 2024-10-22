from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from flask import Flask, request

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


def test_post_album(web_client, db_connection):
    db_connection.seed("seeds/music_store.sql")
    response = web_client.post('/music_store', data={
        'title': 'Back in Black',
        'release_year': 1980,
        'artist_id': 2
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album successfully added!"

    response = web_client.get('/music_store')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Surface Sounds, 2021, 1)\n" \
        "Album(2, A/B, 2016, 1)\n" \
        "Album(3, Back in Black, 1980, 2)"
    
def test_get_all_artists(web_client, db_connection):
    db_connection.seed("seeds/music_store.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Kaleo, Sum 41"

def test_post_artist(web_client, db_connection):
    db_connection.seed("seeds/music_store.sql")
    response = web_client.post('/artists', data= {
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Artist successfully added"

    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Kaleo, Sum 41, Wild nothing"


