class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.__class__.count += 1
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in self.__class__.genres:
            self.__class__.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in self.__class__.artists:
            self.__class__.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        if cls.genre not in cls.genre_count:
            cls.genre_count[cls.genre] = 1
        else:
            cls.genre_count[cls.genre] += 1

    @classmethod
    def add_to_artist_count(cls):
        if cls.artist not in cls.artist_count:
            cls.artist_count[cls.artist] = 1
        else:
            cls.artist_count[cls.artist] += 1

# Creating song instances
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
friends_in_low_places = Song("Friends in Low Places", "Garth Brooks", "Country")

# Accessing attributes
print(ninety_nine_problems.name)
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)

# Accessing class attributes
print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)

