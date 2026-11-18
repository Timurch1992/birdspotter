# === Stage 8: Сортировка записей ===
# Project: BirdSpotter
from datetime import date


def sort_by_name(records, reverse=False):
    return sorted(
        records,
        key=lambda record: record["name"].lower(),
        reverse=reverse,
    )


def sort_by_created_at(records, reverse=False):
    return sorted(
        records,
        key=lambda record: record["created_at"],
        reverse=reverse,
    )


def sort_by_name_then_created(records, reverse=False):
    return sorted(
        records,
        key=lambda record: (record["created_at"], record["name"].lower()),
        reverse=reverse,
    )
