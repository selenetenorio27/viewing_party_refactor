from viewing_party.movie import Movie

class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []



    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)

    def watch_list(self, movie):
        if movie not in self.movie_name:
            self.movie_name.append(movie)