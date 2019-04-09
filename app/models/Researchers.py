from database.migrations.researchers import researchers


class Researchers(researchers):

    @staticmethod
    def all():
        return Researchers.select().dicts()
