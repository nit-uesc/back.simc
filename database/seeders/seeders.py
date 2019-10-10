"""."""
from database.seeders.departments import call_departments_seeder
from database.seeders.users import call_users_seeder


def call_seeders():
    """."""
    call_departments_seeder()
    call_users_seeder()

# import database.seeders.researchers
