import unittest
from src.type.user import User
from src.database import repo
import src.routers as router
import src.contracts as contracts


class TestReg(unittest.TestCase):
    def test_reg(self):
        test_user = User('user1', [])
        router.register(contracts.User(login='user1', password='user1'))
        self.assertTrue(test_user in repo.list())

    def test_reg_ext(self):
        test_user_2 = User('user2', [])
        router.register(contracts.User(login='user2', password='user2'))
        self.assertTrue(test_user_2 in repo.list())

    def test_reg_exists(self):
        admin = User('admin', [])
        self.assertEqual(admin, repo.get('admin'))


class TestLike(unittest.TestCase):
    def setUp(self):
        router.register(contracts.User(login='user1', password='user1'))
        router.register(contracts.User(login='user2', password='user2'))

    def test_simple_add(self):
        exp_res = User('user2', ['song1'])
        router.song_like(contracts.Song(login='user2', fav_song='song1'))
        self.assertEqual(exp_res, repo.get('user2'))

    def test_err(self):
        err_res = User('user1', ['song2'])
        router.song_like(contracts.Song(login='user1', fav_song='song1'))
        self.assertNotEqual(err_res, repo.get('user1'))

    def test_multi(self):
        exp_res = User('user2', ['song1', 'song2', 'song3'])
        router.song_like(contracts.Song(login='user2', fav_song='song1'))
        router.song_like(contracts.Song(login='user2', fav_song='song2'))
        router.song_like(contracts.Song(login='user2', fav_song='song3'))
        self.assertEqual(exp_res, repo.get('user2'))


# class TestRecsys(unittest.TestCase):
#     def setUp(self):
#         router.register(contracts.User(login='user1', password='user1'))
#         router.register(contracts.User(login='user2', password='user2'))
#         router.song_like(contracts.Song(login='user2', fav_song='song1'))
#         router.song_like(contracts.Song(login='user2', fav_song='song2'))
#         router.song_like(contracts.Song(login='user2', fav_song='song3'))

#     def test_len_recs(self):
#         self.assertEqual(len(router.get_recs('user2', 5)), 5)

#     def test_recsys(self):
#         user_songs = ['song1', 'song2', 'song3']
#         recs = router.get_recs('user2', 5)
#         self.assertEqual(len(set(user_songs) & set(recs)), 0)

#     def test_recsys_overflow(self):
#         lib_len = 10
#         user_songs_len = 3
#         recs = router.get_recs('user2', 15)
#         self.assertEqual(len(recs), (lib_len - user_songs_len))
