from matchers import All, PlaysIn, And, HasAtLeast, HasFewerThan, Or, Not

class QueryBuilder:
    def __init__(self):
        self._current_matcher = All()

    def build(self):
        return self._current_matcher

    def playsIn(self, team):
        self._current_matcher = And(self._current_matcher, PlaysIn(team))
        return self

    def hasAtLeast(self, amount, amount_of_what):
        self._current_matcher = And(self._current_matcher, HasAtLeast(amount, amount_of_what))
        return self

    def hasFewerThan(self, amount, amount_of_what):
        self._current_matcher = And(self._current_matcher, HasFewerThan(amount, amount_of_what))
        return self

    def oneOf(self, first_condition, second_condition):
        self._current_matcher = Or(self._current_matcher, Or(first_condition, second_condition))
        return self