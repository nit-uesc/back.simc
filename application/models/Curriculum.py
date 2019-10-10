"""."""
from models.Cnpq import Cnpq


class Curriculum:
    """."""

    def __init__(self, document):
        """."""
        self.__document = document
        self.__cnpq_id = None

    def download_xml(self):
        """."""
        return None
        # if updated get_curriculum_update_date is > than psql curriculum update_date
        # call the cnpq method
        # recieve the data, write the files on folder the public/xml files

        return None

    def download_thumb_150(self):
        """."""
        return None

    def download_thumb_70(self):
        """."""
        return None
