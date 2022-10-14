"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 A
__updated__ = "2019-01-08"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    # Your code here
    title = input("Title: ")
    year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating: "))
    genres = read_genres()
    
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    # Your code here
    line_list = line.split("|")
    title = line_list[0]
    year = int(line_list[1])
    director = line_list[2]
    rating = float(line_list[-2])
    genres_list = line_list[-1].split(',')
    genres = []
    for genre in genres_list:
        genres.append(int(genre))
    
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    fv.seek(0)
    movies = []
    line = fv.readline()
    while line != "":
        movie = read_movie(line)
        movies.append(movie)
        line = fv.readline()
    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    print("Genres")
    for i in Movie.GENRE_CODES:
        genre = Movie.GENRES[i]
        print("{}: {}".format(i, genre))
    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    # Your code here
    menu()  # Display genre choices and genre codes
    genres = []
    number = input("Enter a genre number (ENTER to quit): ")
    while number != "":
        if number.isdigit():
            number_int = int(number)
            if number_int < 0:
                print("Error: Not a positive number.")
            elif number_int >= len(Movie.GENRES):
                print("Error: Input must be < {}".format(len(Movie.GENRE_CODES)))
            elif number_int in genres:
                print("Error: Genre already chosen.")
            else:
                genres.append(number_int)
        else: # Number not able to be cast
            print("Error: Not a positive number.")
        number = input("Enter a genre number (ENTER to quit): ")
    genres.sort()   # Sort in ascending order
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    
    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    ymovies = []
    for movie in movies:
        if movie.year == year:
            ymovies.append(movie)
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    rmovies = []
    for movie in movies:
        if movie.rating >= rating:
            rmovies.append(movie)
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    gmovies = []
    for movie in movies:
        if genre in movie.genres:
            gmovies.append(movie)
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    movie_index = 0
    matches = 0
    while movie_index < len(movies):
        movie = movies[movie_index]
        for genre in genres:
            if genre in movie.genres:
                matches += 1
        if matches == len(genres) and matches == len(movie.genres):
            gmovies.append(movie)
        movie_index += 1
        matches = 0
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """

    # Create list initialized to 0's, with a length of len(Movie.GENRE_CODES)
    counts = [0 for i in Movie.GENRE_CODES]
    for movie in movies:
        for genre_code in movie.genres:
            counts[genre_code] += 1
    return counts
