# === Stage 3: Хранилище в памяти ===
# Project: BirdSpotter
memory_store.py

from typing import Dict, List, Optional


class BirdSpecies:
    __slots__ = ("id", "name", "family", "rarity", "last_observation")

    def __init__(self, name: str, family: str, rarity: str,
                 last_observation: Optional[str] = None) -> None:
        self.id = None
        self.name = name
        self.family = family
        self.rarity = rarity
        self.last_observation = last_observation

    def __repr__(self) -> str:
        return f"BirdSpecies(id={self.id}, name={self.name!r}, family={self.family!r}, rarity={self.rarity!r})"


class InMemorySpeciesStore:
    def __init__(self) -> None:
        self._by_id: Dict[int, BirdSpecies] = {}
        self._counter = 0

    def add_species(self, name: str, family: str, rarity: str,
                    last_observation: Optional[str] = None) -> int:
        species = BirdSpecies(name, family, rarity, last_observation)
        species.id = self._counter
        self._counter += 1
        self._by_id[species.id] = species
        return species.id

    def get_species(self, species_id: int) -> Optional[BirdSpecies]:
        return self._by_id.get(species_id)

    def list_species(self) -> List[BirdSpecies]:
        return list(self._by_id.values())

    def __len__(self) -> int:
        return len(self._by_id)


if __name__ == "__main__":
    store = InMemorySpeciesStore()
    new_id = store.add_species("Дятел трёхполосый", "Dendropanuridae", "обычный", "2024-05-12")
    print(f"Добавлен вид с id={new_id}")
    fetched = store.get_species(new_id)
    print(f"Получен вид: {fetched}")
    print(f"Всего видов в хранилище: {len(store)}")
    for species in store.list_species():
        print(f"  id={species.id}, {species.name}, {species.family}, {species.rarity}")
    missing = store.get_species(9999)
    print(f"Попытка получить несуществующий id: {missing}")
