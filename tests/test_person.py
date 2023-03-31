from viewing_party.person import Person

import pytest

def test_creating_person_initializes_instance_variables():
    # Arrange / Act
    kendall = Person("Kendall")

    # Assert
    assert kendall.name == "Kendall"
    assert kendall.friends == []
    assert kendall.watchlist == []

def test_adding_friend_multiple_times_does_not_create_duplicate():
    # Arrange
    kendall = Person("Kendall")
    simon = Person("Simon")

    # Act
    kendall.add_friend(simon)
    kendall.add_friend(simon)

    # Assert
    assert kendall.friends == [simon]

def test_adding_movie_to_watchlist():
    #Arrange
    kendall = Person("Kendall")
    new_movie = ("The Cinderella")

    # Act
    kendall.add_movie_to_watch_list(new_movie)

    #Assert
    assert kendall.watchlist == ["The Cinderella"]
