"""Class used to define the user table."""
import peewee

from database.migrations.migration import migration


class users(migration):
    """User class."""

    id = peewee.IntegerField(
        constraints=[peewee.SQL('AUTO_INCREMENT')],
        primary_key=True, unique=True
    )
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
