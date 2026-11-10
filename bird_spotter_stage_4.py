# === Stage 4: Связанная сущность ===
# Project: BirdSpotter
from datetime import date
from uuid import uuid4


class Observation:
    def __init__(self, species_id, count, location, season, observed_on=None):
        self.id = uuid4()
        self.species_id = species_id
        self.count = count
        self.location = location
        self.season = season
        self.observed_on = observed_on or date.today()

    def __repr__(self):
        return (
            f"Observation(id={self.id}, species_id={self.species_id}, "
            f"count={self.count}, location={self.location}, "
            f"season={self.season}, observed_on={self.observed_on})"
        )


class Observer:
    def __init__(self):
        self.observations = []

    def add_observation(self, species_id, count, location, season, observed_on=None):
        observation = Observation(
            species_id=species_id,
            count=count,
            location=location,
            season=season,
            observed_on=observed_on,
        )
        self.observations.append(observation)
        return observation

    def get_observations(self, species_id=None):
        if species_id is None:
            return list(self.observations)
        return [o for o in self.observations if o.species_id == species_id]

    def count_species(self, species_id):
        return len(self.get_observations(species_id))
