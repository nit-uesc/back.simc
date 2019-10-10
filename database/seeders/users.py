"""Doc."""
from application.models.User import User


def call_users_seeder():
    """Populate database with users."""
    try:
        User.create(username='admin', password=User.generate_hash('nit_admin'))
    except Exception as e:
        raise e
