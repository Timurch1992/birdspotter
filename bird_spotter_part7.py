# === Stage 7: Фильтрация записей ===
# Project: BirdSpotter
from datetime import date


def filter_by_family(records, family):
    return [record for record in records if record.get("family") == family]


def filter_by_date_range(records, start_date, end_date):
    return [
        record
        for record in records
        if start_date <= record["date"] <= end_date
    ]


def filter_by_family_and_date_range(records, family, start_date, end_date):
    filtered_by_family = filter_by_family(records, family)
    return filter_by_date_range(filtered_by_family, start_date, end_date)


def filter_records(records, family=None, start_date=None, end_date=None):
    if family is not None:
        records = filter_by_family(records, family)
    if start_date is not None:
        records = filter_by_date_range(records, start_date, None)
    if end_date is not None:
        records = filter_by_date_range(records, None, end_date)
    return records


def unique_families(records):
    families = set(record.get("family") for record in records if record.get("family"))
    return sorted(families)


if __name__ == "__main__":
    sample_records = [
        {"id": 1, "species": "Синица", "family": "Вороньи", "count": 3, "date": date(2024, 3, 15)},
        {"id": 2, "species": "Дятел", "family": "Дятловые", "count": 1, "date": date(2024, 5, 20)},
        {"id": 3, "species": "Синица", "family": "Вороньи", "count": 5, "date": date(2024, 7, 10)},
        {"id": 4, "species": "Ласточка", "family": "Ласточковые", "count": 2, "date": date(2024, 8, 5)},
    ]

    print("Все семьи:", unique_families(sample_records))
    print("Всем вороньим:", filter_by_family(sample_records, "Вороньи"))
    print("За период:", filter_by_date_range(sample_records, date(2024, 3, 1), date(2024, 4, 30)))
    print("Фильтр по всем:", filter_records(sample_records, family="Вороньи", start_date=date(2024, 1, 1), end_date=date(2024, 12, 31)))
