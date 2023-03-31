import pytest
from viewing_party.movie import Movie

def test_creating_movie_initializes_instance_variables():
    # Arrange / # Act
    movie_1 = Movie("The little mermaid","kids",5)

    # Assert
    assert movie_1.movie_name == "The little mermaid"
    assert movie_1.genre == "kids"
    assert movie_1.rating == 5

# def test_movie_watch_list():
#     #Arrange / Act
#     movie_1 = Movie("The little mermaid","kids",5)

#     #Assert
#     assert movie_1.watch_list == ["The little mermaid","kids", 5]