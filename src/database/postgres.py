from database.datastore import DataStore

class PostgresDataStore(DataStore):
    
    def __init__(self) -> None:
        super().__init__()