from viewing_party.movie import Movie

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.watchlist = []

    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)

    # def watch_list(self, movie):
    #     if movie not in self.movie_name:
    #         self.movie_name.append(movie)

    def add_movie_to_watch_list(self, new_movie):
        if new_movie not in self.watchlist:
            self.watchlist.append(new_movie)