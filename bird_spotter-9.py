# === Stage 9: Текстовый поиск ===
# Project: BirdSpotter
def highlight_species(text, species, highlight_char='*'):
    """Подсвечивает вхождение текста вида в строке без учёта регистра."""
    if not species:
        return text
    pattern = re.compile(re.escape(species), re.IGNORECASE)
    return pattern.sub(lambda match: highlight_char * len(match.group()), text)


def find_species(observation_records, species_filter):
    """Возвращает наблюдения, содержащие species_filter в поле «вид»,
    с подсветкой совпадений в строке вывода."""
    filtered = []
    for record in observation_records:
        species_name = record.get('species')
        if species_filter and species_filter.lower() not in (species_name or '').lower():
            continue
        record['display_species'] = highlight_species(species_name, species_filter)
        filtered.append(record)
    return filtered


def print_species_report(records, species_filter):
    """Формирует строку отчёта с подсветкой совпадений по виду."""
    lines = []
    for record in find_species(records, species_filter):
        line = "Наблюдение: {species} ({family}) — {location}, {count} шт., {season}".format(
            species=record.get('display_species', record.get('species')),
            family=record.get('family', ''),
            location=record.get('location', ''),
            count=record.get('count', ''),
            season=record.get('season', ''),
        )
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    sample_records = [
        {'species': 'Синица большая', 'family': 'Синицовые', 'location': 'Парк', 'count': 3, 'season': 'Весна'},
        {'species': 'Дятел трёхпалый', 'family': 'Дятловые', 'location': 'Лес', 'count': 1, 'season': 'Лето'},
        {'species': 'Воробей домовый', 'family': 'Воробьиные', 'location': 'Сад', 'count': 5, 'season': 'Осень'},
    ]
    query = 'дят'
    print(print_species_report(sample_records, query))
