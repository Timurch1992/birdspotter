# === Stage 10: Группировка ===
# Project: BirdSpotter
from collections import Counter


def group_by_family(birds):
    """Группирует список видов по семейству. Возвращает словарь
    {семейство: [виды]}."""
    families = {}
    for bird in birds:
        family = bird.get("family")
        families.setdefault(family, []).append(bird)
    return families


def count_by_family(birds):
    """Группирует виды по семейству и подсчитывает количество в каждой
    группе. Возвращает словарь {семейство: количество}."""
    families = group_by_family(birds)
    return {family: len(group) for family, group in families.items()}


def top_families(birds, limit=5):
    """Возвращает список кортежей (семейство, количество) отсортированный
    по убыванию числа видов, ограниченный длиной limit."""
    return sorted(
        count_by_family(birds).items(),
        key=lambda item: item[1],
        reverse=True,
    )[:limit]


def sample():
    birds = [
        {"name": "Синица", "family": "Синицевые", "rarity": "Знакомый", "last_seen": "2024-01-05"},
        {"name": "Дятел", "family": "Дятловые", "rarity": "Знакомый", "last_seen": "2024-01-04"},
        {"name": "Воробей", "family": "Воробьиные", "rarity": "Знакомый", "last_seen": "2024-01-03"},
        {"name": "Синица", "family": "Синицевые", "rarity": "Знакомый", "last_seen": "2024-01-02"},
        {"name": "Дятел", "family": "Дятловые", "rarity": "Знакомый", "last_seen": "2024-01-01"},
        {"name": "Сорока", "family": "Воробьиные", "rarity": "Знакомый", "last_seen": "2024-01-06"},
    ]
    return birds


if __name__ == "__main__":
    birds = sample()
    print("Группы по семейству:")
    for family, group in group_by_family(birds).items():
        print(f"  {family}: {len(group)} видов")

    print("\nТоп-5 семейств по численности:")
    for family, count in top_families(birds):
        print(f"  {family}: {count}")
