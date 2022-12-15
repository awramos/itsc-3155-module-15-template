from flask.testing import FlaskClient

from tests.utils import create_movie, refresh_db


def test_get_all_movies(test_app):
    refresh_db()
    
    test_movie = create_movie()
    res = test_app.get('/movies')
    page_data = res.data

    assert res.status_code == 200
    assert f'<td><a href="/movies/{test_movie.movie_id}">Ponyo</a></td>' in page_data
    assert '<td>Ghibli</td>' in page_data
    assert '<td>5</td>' in page_data

def test_get_all_movies_empty(test_app):
    refresh_db()

    res = test_app.get('/movies')
    page_data = res.data

    assert res.status_code == 200
    assert '<td>' not in page_data

def test_get_all_movies_single(test_app):
    refresh_db()

    test_movie = create_movie
    res = test_app.get(f'/movies/{test_movie.movie_id}')
    page_data = res.data.decode()

    assert res.status_code == 200
    assert '<td>Ponyo - 5</td>' in page_data
    assert '<td>Ghibli</td>' in page_data

def test_get_all_movies_404(test_app):
    refresh_db()

    test_movie = create_movie
    res = test_app.get(f'/movies/1')

    assert res.status_code == 200

def test_create_movie(test_app):
    refresh_db()
    res = test_app.get('/movies')
    page_data = res.data

    res = test_app.post('/movies', data={'title': 'Ponyo', 'director': 'Ghibli','rating': '5'}, follow_redirects=True)
    
    assert res.status_code == 200
    assert '<td>Ponyo - 5</td>' in page_data
    assert '<td>Ghibli</td>' in page_data

def test_create_movie_400(test_app):
    refresh_db()

    res = test_app.post('/movies', data={'title': 'Ponyo', 'director': 'Ghibli'} , follow_redirects=True)
    
    assert res.status_code == 400
