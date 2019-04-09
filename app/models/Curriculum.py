from models.Cnpq import Cnpq 

class Curriculum(cpf):
    def __init__(self):
        self.__cpf = cpf
        self.__cnpq_id = None

    def download_xml(self):
        # if updated get_curriculum_update_date is > than psql curriculum update_date
        # call the cnpq method
        # recieve the data, write the files on folder the public/xml files

        return None
    def download_thumb_150(self):
        return None
    def download_thumb_70(self):
        return None
