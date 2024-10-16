# Movie data stored in a list of dictionaries
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama"},
    {"title": "The Godfather", "genre": "Crime"},
    {"title": "The Dark Knight", "genre": "Action"},
    {"title": "12 Angry Men", "genre": "Drama"},
    {"title": "Schindler's List", "genre": "Biography"},
    {"title": "The Lord of the Rings: The Return of the King", "genre": "Fantasy"},
    {"title": "Pulp Fiction", "genre": "Crime"},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "genre": "Fantasy"},
    {"title": "Forrest Gump", "genre": "Drama"},
    {"title": "Star Wars: Episode V - The Empire Strikes Back", "genre": "Science Fiction"}
]

# User preferences stored in a dictionary
user_preferences = {
    "Alice": {"genre": "Drama", "liked_movies": []},
    "Bob": {"genre": "Action", "liked_movies": []},
    "Charlie": {"genre": "Fantasy", "liked_movies": []}
}

def recommend_movies(user):
    """Recommend movies based on user preferences"""
    recommended_movies = set()
    for movie in movies:
        if movie["genre"] == user_preferences[user]["genre"]:
            recommended_movies.add(movie["title"])
    return recommended_movies

def display_recommendations():
    """Display movie recommendations for each user"""
    for user in user_preferences:
        print(f"Recommendations for {user}:")
        recommended_movies = recommend_movies(user)
        for movie in recommended_movies:
            print(f"- {movie}")
        print()

display_recommendations()