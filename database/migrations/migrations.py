"""."""
from database.migrations.departments import departments
from database.migrations.researchers import researchers
from database.migrations.users import users


def call_migrations():
    """Run all migrations."""
    users.drop_table()
    users.create_table()

    researchers.drop_table()

    departments.drop_table()

    departments.create_table()
    researchers.create_table()

