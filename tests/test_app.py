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
    db_connection.seed("seeds/albums.sql")
    response = web_client.post('/albums', data={
        'title': 'Back in Black',
        'release_year': 1980,
        'artist_id': 2
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album successfully added!"

    response = web_client.get('/albums')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Surface Sounds, 2021, 1)\n" \
        "Album(2, A/B, 2016, 1)\n" \
        "Album(3, Back in Black, 1980, 2)"