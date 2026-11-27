# === Stage 13: Поиск дубликатов ===
# Project: BirdSpotter
import difflib


def normalize_species(name):
    return (
        name.strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace(".", "_")
    )


def normalize_family(family):
    return family.strip().lower() if family else ""


def normalize_rarity(rarity):
    return str(rarity).strip().lower() if rarity is not None else ""


def normalize_last_seen(value):
    if value is None:
        return ""
    return str(value).strip()


def normalize_observation(observation):
    return (
        normalize_species(observation.get("name"))
        + "|"
        + normalize_family(observation.get("family"))
        + "|"
        + normalize_rarity(observation.get("rarity"))
        + "|"
        + normalize_last_seen(observation.get("last_seen"))
    )


def is_duplicate(candidate, candidates, limit_ratio=0.8):
    candidate_key = normalize_observation(candidate)
    if not candidate_key:
        return False

    for other in candidates:
        other_key = normalize_observation(other)
        if other_key and difflib.SequenceMatcher(None, candidate_key, other_key).ratio() >= limit_ratio:
            return True

    return False


def find_duplicates(records, limit_ratio=0.8):
    seen = []
    duplicates = []
    for record in records:
        if is_duplicate(record, seen, limit_ratio):
            duplicates.append(record)
        else:
            seen.append(record)
    return duplicates


if __name__ == "__main__":
    sample = [
        {"name": "Большая синица", "family": "Синицовые", "rarity": "Обычная", "last_seen": "2024-05-01"},
        {"name": "большая синица", "family": "синицовые", "rarity": "обычная", "last_seen": "2024-06-15"},
        {"name": "Воробей домовый", "family": "Врановые", "rarity": "Обычная", "last_seen": "2024-07-01"},
        {"name": "Воробей Домовый", "family": "Врановые", "rarity": "Обычная", "last_seen": "2024-07-10"},
        {"name": "Снегирь", "family": "Снегиревые", "rarity": "Редкая", "last_seen": "2024-08-01"},
        {"name": "Снегирь", "family": "Снегиревые", "rarity": "Редкая", "last_seen": "2024-09-01"},
    ]
    print(find_duplicates(sample))
