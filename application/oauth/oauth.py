"""File for authorization."""
from flask_restful import reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token)
from application.models.Users import Users

parser = reqparse.RequestParser()


class oauth:
    """Oauth class responsible for validating requests."""

    def __init__(self, auth):
        """."""
        if not auth:
            raise Exception('Auth not defined')
        if not auth.username or not auth.password:
            raise Exception('Missing credentials')
        self._username = auth.username
        self._password = auth.password

    def validate(self):
        """."""
        try:
            """."""
            user = Users.get(Users.username == self._username)
        except Exception as e:
            raise Exception('User does not exist: MSG [{}]'.format(e))

        if Users.vefify_hash(self._password, user.password):
            access_token = create_access_token(identity=self._username)
            refresh_token = create_refresh_token(identity=self._username)
            return {
                'message': 'Logged as {}'.format(self._username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        return {'message': 'Wrong credentials'}
