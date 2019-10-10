"""."""
import peewee
from peewee import MySQLDatabase
db = MySQLDatabase('simc', user='reisnobre', passwd='nit_admin')


class migration(peewee.Model):
    """."""

    class Meta:
        """."""

        database = db
