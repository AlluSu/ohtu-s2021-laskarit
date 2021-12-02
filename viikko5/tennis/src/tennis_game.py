class TennisGame:
    MAX_SCORE = 4
    POINTS_IN_BEGINNING = 0
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = self.POINTS_IN_BEGINNING
        self.player2_score = self.POINTS_IN_BEGINNING

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def is_tie(self, player1_score, player2_score):
        return player1_score == player2_score

    def get_tie_results(self, result):
        result_dict = {
            0:"Love-All",
            1:"Fifteen-All",
            2:"Thirty-All",
            3:"Forty-All",
            4:"Deuce"
        }
        if result > self.MAX_SCORE-1:
            return result_dict[self.MAX_SCORE]
        return result_dict[result]

    def determine_winner_or_advantage(self, difference):
        # tätä voisi ehkä vielä refaktoroida jotenkin (?)
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def either_player_has_max_score_or_more(self, player1_score, player2_score):
        return self.player1_score >= self.MAX_SCORE or self.player2_score >= self.MAX_SCORE

    def game_determines_score(self, player1_score, player2_score):
        score = ""
        temp_score = 0
        temp_score_dict = {
            0:score + "Love",
            1:score + "Fifteen",
            2:score + "Thirty",
            3:score + "Forty"
        }
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score
            score += temp_score_dict[temp_score]
        return score

    def get_score(self):
        score = ""

        if self.is_tie(self.player1_score, self.player2_score):
            score = self.get_tie_results(self.player1_score)
        elif self.either_player_has_max_score_or_more(self.player1_score, self.player2_score):
            difference = self.player1_score - self.player2_score
            score = self.determine_winner_or_advantage(difference)
        else:
            score = self.game_determines_score(self.player1_score, self.player2_score)

        return score
