# === Stage 5: Связи между сущностями ===
# Project: BirdSpotter
from datetime import date


class BirdSpotter:
    """Модуль: получение всех наблюдений для вида и проверка целостности связи."""

    def __init__(self, species, observations):
        self._species = species
        self._observations = observations

    def get_all(self, species_id):
        return [
            obs for obs in self._observations
            if obs["species_id"] == species_id
        ]

    def count(self, species_id):
        return len(self.get_all(species_id))

    def check_integrity(self, species_id):
        observed = self.get_all(species_id)
        last_seen = None
        for obs in observed:
            date_seen = obs.get("date")
            if date_seen and (last_seen is None or date_seen > last_seen):
                last_seen = date_seen
        return (
            observed
            and species_id in self._species
            and last_seen is not None
        )
