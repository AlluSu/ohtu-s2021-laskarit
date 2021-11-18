from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        # Korjataan joskus järkevämmäksi, nyt siis annettava 7 kirjainta ja 1 tai enemmän numeroa
        if not username or not password:
            raise UserInputError("Username and password are required")
        if not re.search("[a-z]{3,}", username) and re.search("[0-9a-zA-Z]{7,}[0-9]+", password):
            raise UserInputError("Username is too short, minimum length is 3")
        if re.search("[a-z]{3,}", username) and not re.search("[0-9a-zA-Z]{7,}[0-9]+", password):
            raise UserInputError("Password is too short, requirements are minimun length of 8 followed with one number")
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is taken")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
