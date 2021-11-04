import unittest
from statistics import Statistics, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_konstruktori_on_oikein(self):
        self.assertIsNotNone(self.statistics)
        self.assertIsNotNone(self.statistics._player_reader)
        self.assertIsNotNone(self.statistics._players)
        players = self.statistics._players
        self.assertAlmostEqual(len(players), 5)

    def test_pisteet_palautuu_oikein(self):
        players = self.statistics._players
        semenko = players[0]
        self.assertAlmostEqual(sort_by_points(semenko), 16)

    def test_olemassa_oleva_pelaaja_loytyy(self):
        semenko = self.statistics._players[0].name
        self.assertIsNotNone(self.statistics.search(semenko))

    def test_olematon_pelaaja_ei_loydy(self):
        self.assertIsNone(self.statistics.search("Rosberg"))

    def test_tiimi_ja_pelaajat_palautuvat_oikein(self):
        team = self.statistics.team("EDM")
        self.assertAlmostEqual(len(team), 3)

    def test_huippupelaajat_palautuu_oikein(self):
        top_scorers = self.statistics.top_scorers(2)
        self.assertAlmostEqual(len(top_scorers), 2)
