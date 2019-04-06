import peewee

from database.migrations.migration import migration


class departments(migration):
    code = peewee.TextField()
    name = peewee.TextField()
