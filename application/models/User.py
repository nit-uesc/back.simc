"""Doc."""
from database.migrations.users import users
from passlib.hash import pbkdf2_sha256 as sha256


class User(users):
    """User class."""

    @staticmethod
    def all():
        """Return all users."""
        return User.select().dicts()

    @staticmethod
    def generate_hash(password):
        """Generate hash to be used password."""
        return sha256.hash(password)

    @staticmethod
    def vefify_hash(password, hash):
        """Verify if the hash is valid."""
        return sha256.verify(password, hash)
