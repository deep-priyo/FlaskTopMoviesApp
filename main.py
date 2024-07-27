from datetime import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATED DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)


# CREATED TABLE HERE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, unique=False)
    description: Mapped[str] = mapped_column(String, unique=False)
    rating: Mapped[float] = mapped_column(Float, unique=False)
    ranking: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    review: Mapped[str] = mapped_column(String, unique=False)
    img_url: Mapped[str] = mapped_column(String, unique=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


#create all
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    sortby = request.args.get('category', None)
    print(sortby)
    if sortby is None:
        movies = Movie.query.order_by(Movie.ranking).all()

    if sortby == 'title':
        movies = Movie.query.order_by(Movie.title).all()
    if sortby == 'year':
        movies = Movie.query.order_by(Movie.year).all()
    if sortby == 'rating':
        movies = Movie.query.order_by(Movie.rating).all()
    if sortby == 'ranking':
        movies = Movie.query.order_by(Movie.ranking).all()
    movie_count = Movie.query.count()
    return render_template("index.html", movies=movies, movie_count=movie_count)


class EditMovieForm(FlaskForm):
    rating = StringField('Rating', render_kw={"placeholder": "Your Rating Out Of 10"})
    review = StringField('Review', render_kw={"placeholder": "How was the movie?"})
    submit = SubmitField('Make Changes')


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    form = EditMovieForm()
    if form.validate_on_submit():
        rating = request.form["rating"]
        review = request.form["review"]
        if rating:
            movie.rating = rating
        if review:
            movie.review = review
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=EditMovieForm(), movie=movie)
@app.route("/delete/<int:movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

class AddMovieForm(FlaskForm):
    title = StringField('Title', render_kw={"placeholder": "Movie Title"})
    year = StringField('Year', render_kw={"placeholder": "Movie Year"})
    description = StringField('Description', render_kw={"placeholder": "Movie Description"})
    rating = StringField('Rating', render_kw={"placeholder": "Your Rating Out Of 10,eg 7.5"})
    ranking = StringField('Ranking', render_kw={"placeholder": "Your Ranking Of 10,eg 1,2,3..."})

    review = StringField('Review', render_kw={"placeholder": "How was the movie?"})
    img_url = StringField('Image URL', render_kw={"placeholder": "Poster Url Here..."})
    submit = SubmitField('Add Movie')
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = request.form["title"]
        year = request.form["year"]
        description = request.form["description"]
        rating = request.form["rating"]
        ranking = request.form["ranking"]
        review = request.form["review"]
        img_url = request.form["img_url"]
        new_movie = Movie(title=title, year=year, description=description, rating=rating,ranking=ranking, review=review, img_url=img_url)
        db.session.add(new_movie)
        db.session.commit()
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html",form=form)




if __name__ == '__main__':
    app.run(debug=True)
