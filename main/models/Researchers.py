from database.migrations.researchers import researchers


class Researchers(researchers):
    def get():
        return 'a'
