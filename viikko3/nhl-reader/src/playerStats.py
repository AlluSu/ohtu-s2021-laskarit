from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def most_points(self, player):
        return player.assists + player.goals

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []
        for player in self.reader.get_players():
            if player.nationality == nationality:
                players_by_nationality.append(player)

        players_by_nationality.sort(reverse=True, key=self.most_points)

        return players_by_nationality

