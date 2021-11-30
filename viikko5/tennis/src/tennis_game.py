class TennisGame:
    MAX_SCORE = 4
    POINTS_IN_BEGINNING = 0
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = self.POINTS_IN_BEGINNING
        self.m_score2 = self.POINTS_IN_BEGINNING

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

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
        if result > 3 or result < 0:
            return result_dict[4]
        return result_dict[result]


    def get_score(self):
        score = ""
        temp_score = 0

        if self.is_tie(self.m_score1, self.m_score2):
            score = self.get_tie_results(self.m_score1)
        elif self.m_score1 >= self.MAX_SCORE or self.m_score2 >= self.MAX_SCORE:
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score