"""
-Enter 'a' to add a movie , 1 to see movies , 'f' find movies , 'q' to quit
-add movies
-see movies
-find a movie
-stop running nthe application

tasks:
[]: decide where to store movies
[]:what is the format of a movie
[]: show the user the main interface and get the input
[]: allow user to add movies
[]: find a movie
[]: stop running the application (q)

"""
movies = []
"""
movie = {
    'name' : 
    'director':
    'year' :
}
"""

def menu():
    user_input = input("Enter 'a' to add a movie , 1 to see movies , 'f' find movies , 'q' to quit : ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movies()
        else:
            print("Unknown Command -- Please Try Again ! ! !")
        user_input = input("\nEnter 'a' to add a movie , 1 to see movies , 'f' find movies , 'q' to quit : ")


def add_movie():
    name = input("movie name : ")
    director = input('movie director : ')
    year = int(input("release year : "))
    movie = {
        'name':name,
        'director':director,
        'year':year
    }
    movies.append(movie)
def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)
def show_movie_details(movie):
    print(f"Name : {movie['name']}")
    print(f"Director : {movie['director']}")
    print(f"year : {movie['year']}")
def find_movies():
    find_by = input(" property to search by : (name, director , year ) : ")
    looking_for = input("what are you looking for :")
    found_movies = find_by_attributes(movies,looking_for,lambda  x: x[find_by])
    show_movies(found_movies)

def find_by_attributes(items,expected,finder):
    found = []

    for item in items:
        if finder(item) == expected:
            found.append(item)

    return found


menu()
print(movies)






