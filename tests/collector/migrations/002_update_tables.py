from typing import Dict, Any


class Migration:
    version = '002'

    def __init__(self, context: Dict[str, Any]) -> None:
        self.context = context
