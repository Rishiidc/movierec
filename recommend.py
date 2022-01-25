from flask import Flask,jsonify,request
import csv

allmovies = []
with open("movies.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

likedmovies = []
unlikedmovies = []
notwatchedmovies = []
popularmovies = []

app = Flask(__name__)
@app.route("/getmovie")
def getmovie():
    return jsonify({
        "data":allmovies[0],
        "status":"Success!"
    })

@app.route("/likedmovies",methods=["POST"])
def likedmovies():
    movies = allmovies[0]
    allmovies = allmovies[1:]
    likedmovies.append(movies)
    return jsonify({
        "status":"Success!"
    }),200

@app.route("/notwatchedmovies",methods=["POST"])
def notwatchedmovies():
    movies = allmovies[0]
    allmovies = allmovies[1:]
    notwatchedmovies.append(movies)
    return jsonify({
        "status":"Success!"
    }),200

@app.route("/unlikemovies",methods=["POST"])
def unlikemovies():
    movies = allmovies[0]
    allmovies = allmovies[1:]
    unlikemovies.append(movies)
    return jsonify({
        "status":"Success!"
    }),200

@app.route("/popularmovies")
def popularmovies():
    moviedata = []
    for movie in output:
        d = {
            "title":movie[0],
            "poster_link":movie[1],
            "release_date":movie[2] or "N/A",
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5]
        }
        movie_data.append(d) 
    return jsonify({
        "data":movie_data,
        "status":"Success!"
    }),200

@app.route("/recommendedmovies")
def recommended():
    recommendedmovies = []
    for i in likedmovies:
        output = get_recommendations(i[19])
        for j in output:
            recommendedmovies.append(j)
    import itertools
    recommendedmovies.sort()
    recommendedmovies = list(recommendedmovies for recommendedmovies,_ in itertools.groupby(recommendedmovies))
    moviedata = []
    for k in recommendedmovies:
        d = {
            "title":movie[0],
            "poster_link":movie[1],
            "release_date":movie[2] or "N/A",
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5]
        }
        movie_data.append(d) 
    return jsonify({
        "data":movie_data,
        "status":"Success!"
    }),200

if __name__=="__main__":
    app.run()

