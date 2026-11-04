# === Stage 2: Проверка полей ===
# Project: BirdSpotter
from datetime import date


class BirdDataError(ValueError):
    pass


def normalize_species_name(raw: str) -> str:
    parts = raw.strip().split()
    return " ".join(part.capitalize() for part in parts)


def normalize_family(raw: str) -> str:
    return raw.strip().capitalize()


def normalize_rarity(raw: str) -> str:
    mapping = {
        "очень редкий": "очень редкий",
        "редкий": "редкий",
        "необычный": "необычный",
        "обычный": "обычный",
        "частый": "частый",
        "очень частый": "очень частый",
    }
    normalized = raw.strip().lower()
    if normalized not in mapping:
        raise BirdDataError(
            "Редкость должна быть одной из: очень редкий, редкий, "
            "необычный, обычный, частый, очень частый"
        )
    return mapping[normalized]


def normalize_last_observation(raw: str) -> date:
    raw = raw.strip()
    if not raw:
        raise BirdDataError("Последнее наблюдение не может быть пустым")
    try:
        return date.fromisoformat(raw[:10])
    except ValueError:
        raise BirdDataError(
            "Последнее наблюдение должно быть в формате ГГГГ-ММ-ДД"
        )


def validate_name(raw: str) -> str:
    if not raw:
        raise BirdDataError("Название вида обязательно")
    if len(raw.strip()) < 2:
        raise BirdDataError("Название вида слишком короткое")
    return normalize_species_name(raw)


def validate_family(raw: str) -> str:
    if not raw:
        raise BirdDataError("Семейство обязательно")
    if len(raw.strip()) < 2:
        raise BirdDataError("Семейство слишком короткое")
    return normalize_family(raw)


def validate_rarity(raw: str) -> str:
    return normalize_rarity(raw)


def validate_last_observation(raw: str) -> date:
    return normalize_last_observation(raw)


def validate_species(raw: dict) -> dict:
    species = dict(raw)
    species["name"] = validate_name(raw.get("name", ""))
    species["family"] = validate_family(raw.get("family", ""))
    species["rarity"] = validate_rarity(raw.get("rarity", ""))
    species["last_observation"] = validate_last_observation(
        raw.get("last_observation", "")
    )
    return species
