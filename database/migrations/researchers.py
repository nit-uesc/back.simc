import peewee

from database.migrations.departments import departments
from database.migrations.migration import migration


class researchers(migration):
    id = peewee.IntegerField(
            constraints=[peewee.SQL('AUTO_INCREMENT')],
            primary_key=True, unique=True
    )
    id_cnpq = peewee.TextField()
    document = peewee.TextField()
    update_date = peewee.TextField()
    code = peewee.TextField()
    extracted = peewee.BooleanField()
    invalid = peewee.BooleanField()
    department = peewee.ForeignKeyField(departments)
