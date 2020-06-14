from typing import Dict, Any


class Migration:
    version = '001'

    def __init__(self, context: Dict[str, Any]) -> None:
        self.context = context
        self.connection = context['connection']
        self.schema = context['schema']

    def schema_up(self) -> None:
        self.connection.execute(
            f"CREATE TABLE IF NOT EXISTS {self.schema}.employees("
            "id serial PRIMARY KEY, "
            "name VARCHAR(255), "
            "age INT)")
