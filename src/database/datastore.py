
class DataStore:
    
    def __init__(self) -> None:
        pass
    
    def get(self, resource_name: str, id: str) -> dict:
        pass
    
    def list(self, resource_name: str, sort: dict, filter: dict, pagination: dict) -> dict:
        pass
    
    def create(self, resource_name: str, data: dict) -> dict:
        pass
    
    def update(self, resource_name: str, id: str, data: dict) -> dict:
        pass
    
    def delete(self, resource_name: str, id: str) -> dict:
        pass
    
    def exists(self, resource_name: str, id: str) -> dict:
        pass