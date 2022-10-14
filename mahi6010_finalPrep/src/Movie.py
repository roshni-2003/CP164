"""
-------------------------------------------------------
Movie class definition.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2019-01-08"
-------------------------------------------------------
"""


class Movie:
    """
    Defines data for a single movie: title, year, director, rating, genres.
    """
    # Constants
    MIN_RATING = 0
    MAX_RATING = 10
    FIRST_YEAR = 1888
    GENRES = ("science fiction", "fantasy", "drama",
              "romance", "comedy", "zombie", "action",
              "historical", "horror", "war")
    # Defines a range of valid integer genre codes:
    GENRE_CODES = range(len(GENRES))

    def __init__(self, title, year, director, rating, genres):
        """
        -------------------------------------------------------
        Initializes a Movie object.
        Use: movie = Movie(title, year, director, rating, genres)
        -------------------------------------------------------
        Parameters:
            title - movie title (str)
            year - year of release (int)
            director - name of director (str)
            rating - rating of 1 - 10 from IMDB (float)
            genres - numbers representing movie genres_list (list of int)
        Returns:
            A new Movie object (Movie)
        -------------------------------------------------------
        """
        assert year >= Movie.FIRST_YEAR, "Movie year must be >= {}".format(
            Movie.FIRST_YEAR)
        assert rating is None or Movie.MIN_RATING <= rating <= Movie.MAX_RATING, \
            "Movie ratings must be between {} and {}".format(
                Movie.MIN_RATING, Movie.MAX_RATING)
        assert genres is None or genres == [] or min(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(
            min(genres))
        assert genres is None or genres == [] or max(genres) in Movie.GENRE_CODES, "Invalid genre code {}".format(
            max(genres))

        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genres = genres

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie data.
        Use: print(movie)
        Use: print( "{}".format(movie))
        Use: string = str(movie)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of movie (str)
        -------------------------------------------------------
        """
        # Generate the list of genres as a string.
        genres_list = self.genres_string()

        if self.director is None or \
        self.rating is None or self.genres is None:
            string = "{}, {}".format(self.title, self.year)
        else:
            string = """Title:    {}
    Year:     {}
    Director: {}
    Rating:   {}
    Genres:   {}""".format(self.title, self.year, self.director, self.rating, genres_list)
        return string

    def __eq__(self, other):
        """
        -------------------------------------------------------
        Compares this movie against another movie for equality.
        Use: movie == other
        -------------------------------------------------------
        Parameters:
            other - other movie to compare to (Movie)
        Returns:
            result - True if title and year match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) == \
            (other.title.lower(), other.year)
        return result

    def __lt__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie comes before another movie.
        Use: movie < other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if movie precedes other, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) < \
            (other.title.lower(), other.year)
        return result

    def __le__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie precedes or is or equal to another movie.
        Use: movie <= other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if this movie precedes or is equal to other,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < other or self == other
        return result

    def genres_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genres based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "science fiction, drama"
        Use: string = movie.genres_string()
        -------------------------------------------------------
        Returns:
            string - string of genres (str)
        -------------------------------------------------------
        """

        # Your code here
        string = ""
        if self.genres is not None:
            for num in self.genres:
                genre_name = Movie.GENRES[num]
                if num == self.genres[-1]:
                    string += genre_name
                else:
                    string += genre_name + ", "
        return string

    def genres_list_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genre indexes based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "0,2"
        Use: string = movie.genres_list_string()
        -------------------------------------------------------
        Returns:
            string - string of genre indexes (str)
        -------------------------------------------------------
        """

        # Your code here
        string = ""
        for genre_code in self.genres:
            if genre_code == self.genres[-1]:   # Last value, so no comma
                string += str(genre_code)
            else:
                string += str(genre_code) + ","
        #print(string)
        return string

    def write(self, fv):
        """
        -------------------------------------------------------
        Writes a single line of movie data to an open file fv
        in the format
              title|year|director|rating|code
        Use: movie.write(fv)
        -------------------------------------------------------
        Parameters:
            fv - an already open file of movie data (file)
        Returns:
            None
        -------------------------------------------------------
        """
        print("{}|{}|{}|{}|{}"
              .format(self.title, self.year, self.director,
                      self.rating, self.genres_list),
              file=fv)
        return

    def key(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie key data.
        Use: key = movie.key()
        -------------------------------------------------------
        Returns:
            string - the formatted contents of movie key (str)
        -------------------------------------------------------
        """
        string = "{}, {}".format(self.title, self.year)
        return string

    def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a movie name.
        Use: h = hash(movie)
        -------------------------------------------------------
        Returns:
            returns
            value - the total of the characters in the name string
                multiplied by the year (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.title:
            value = value + ord(c)
        value *= self.year
        return value
