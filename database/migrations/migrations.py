from database.migrations.departments import departments
from database.migrations.researchers import researchers

researchers.drop_table()

departments.drop_table()

departments.create_table()
researchers.create_table()
