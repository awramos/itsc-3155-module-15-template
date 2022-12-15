from src.models import Movie, db

def create_movie(title='Ponyo', director='Ghibli', rating='5'):
    test_movie = Movie(title=title, director=director, rating=rating)
    db.session.add(test_movie)
    db.session.commit()
    return test_movie

def refresh_db():
    Movie.query.delete()
    db.session.commit()