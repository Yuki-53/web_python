import pytest
from src.type.user import User
from src.database import repo
import src.routers as router
import src.contracts as contracts


# registration tests
def test_reg():
    test_user = User('user1', [])
    router.register(contracts.User(login='user1', password='user1'))
    assert test_user in repo.list()


def test_reg_ext():
    test_user_2 = User('user2', [])
    router.register(contracts.User(login='user2', password='user2'))
    assert test_user_2 in repo.list()


def test_reg_exists():
    admin = User('admin', [])
    assert admin == repo.get('admin')


# add_song tests
def test_simple_add():
    exp_res = User('user2', ['song1'])
    router.song_like(contracts.Song(login='user2', fav_song='song1'))
    assert exp_res == repo.get('user2')


def test_err():
    err_res = User('user1', ['song2'])
    exp_res = User('user1', ['song1'])
    router.song_like(contracts.Song(login='user1', fav_song='song1'))
    assert err_res != repo.get('user1')
    assert exp_res == repo.get('user1')


def test_multi():
    exp_res = User('user2', ['song1', 'song2', 'song3'])
    router.song_like(contracts.Song(login='user2', fav_song='song2'))
    router.song_like(contracts.Song(login='user2', fav_song='song3'))
    assert exp_res == repo.get('user2')


# recsys tests
def test_len_recs():
    assert len(router.get_recs('user2', 5)) == 5


def test_recsys():
    user_songs = ['song1', 'song2', 'song3']
    recs = router.get_recs('user2', 5)
    assert len(set(user_songs) & set(recs)) == 0


def test_recsys_overflow():
    lib_len = 10
    user_songs_len = 3
    recs = router.get_recs('user2', 15)
    assert len(recs) == lib_len - user_songs_len
