# === Stage 1: Каркас модуля ===
# Project: BirdSpotter
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Species:
    name: str
    family: str
    rarity: str
    last_seen: date


def make_demo_records() -> list[Species]:
    return [
        Species(name="Синица большая", family="Синицовые", rarity="Обычный", last_seen=date(2024, 5, 12)),
        Species(name="Дятел трёхпёрстый", family="Дятловые", rarity="Частый", last_seen=date(2024, 4, 3)),
        Species(name="Орлан-белохвост", family="Ястребиные совы", rarity="Редкий", last_seen=date(2024, 2, 20)),
    ]


def main() -> None:
    records = make_demo_records()
    print("BirdSpotter — дневник наблюдений за птицами")
    print("=" * 40)
    for record in records:
        print(f"{record.name} [{record.family}]")
        print(f"  Редкость: {record.rarity}")
        print(f"  Последнее наблюдение: {record.last_seen}")
        print()


if __name__ == "__main__":
    main()
