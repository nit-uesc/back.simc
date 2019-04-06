import peewee
import datetime

from database.migrations.departments import departments
from database.migrations.migration import migration


class researchers(migration):
    id = peewee.IntegerField(
            constraints=[peewee.SQL('AUTO_INCREMENT')],
            primary_key=True, unique=True
    )
    extracted = peewee.BooleanField(default=False)
    invalid = peewee.BooleanField(default=False)
    update_date = peewee.TextField(default=datetime.datetime.now)
    document = peewee.TextField()
    id_cnpq = peewee.TextField(null=True)
    code = peewee.TextField(null=True)
    department = peewee.ForeignKeyField(departments)
