from typing import Dict, Any


class Migration:
    version = '003'

    def __init__(self, context: Dict[str, Any]) -> None:
        self.context = context
