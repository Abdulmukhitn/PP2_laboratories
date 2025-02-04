# List of movie dictionaries
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# 1.
def is_good_movie(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False

# 2.
def filter_good_movies(movie_list):
    good_movies = []
    for movie in movie_list:
        if is_good_movie(movie):
            good_movies.append(movie)
    return good_movies

# 3.
def filter_movies_by_category(movie_list, category):
    category_movies = []
    for movie in movie_list:
        if movie["category"].lower() == category.lower():
            category_movies.append(movie)
    return category_movies

# 4.
def average_imdb(movie_list):
    if len(movie_list) == 0:
        return 0
    total_score = 0
    for movie in movie_list:
        total_score += movie["imdb"]
    avg_score = total_score / len(movie_list)
    return avg_score

# 5.
def average_imdb_by_category(movie_list, category):
    movies_in_category = filter_movies_by_category(movie_list, category)
    return average_imdb(movies_in_category)

print("Movies with an IMDB score above 5.5:")
good_movies = filter_good_movies(movies)
for movie in good_movies:
    print(" -", movie["name"], "(IMDB:", movie["imdb"], ")")

print("Romance movies:")
romance_movies = filter_movies_by_category(movies, "Romance")
for movie in romance_movies:
    print(" -", movie["name"], "(IMDB:", movie["imdb"], ")")

avg_all = average_imdb(movies)
print("Average IMDB score for all movies:", avg_all)

avg_romance = average_imdb_by_category(movies, "Romance")
print("Average IMDB score for Romance movies:", avg_romance)
