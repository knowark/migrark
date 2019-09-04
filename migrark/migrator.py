from .versioner import Versioner
from .collector import Collector


class Migrator:

    def __init__(self, versioner: Versioner,  collector: Collector) -> None:
        self.versioner = versioner
        self.collector = collector

    def migrate(self):
        migrations = self.collector.retrieve()
        version = self.versioner.current_version

        for migration in migrations:
            if migration.version > version:
                migration.schema_up()
