# === Stage 11: Постраничный вывод ===
# Project: BirdSpotter
from math import ceil


def page_size(query, page):
    if page < 1:
        page = 1
    return max(1, min(100, page))


def build_pagination(total, page, page_size, max_size=100):
    if page < 1:
        page = 1
    total_pages = max(1, ceil(total / page_size))
    if page > total_pages:
        page = total_pages
    start = (page - 1) * page_size
    end = min(start + page_size, total)
    return {
        "current_page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages,
        "has_next": end < total,
        "has_prev": page > 1,
        "has_first": page > 1,
        "has_last": page < total_pages,
        "first_page": 1,
        "last_page": total_pages,
        "prev_page": page - 1 if page > 1 else None,
        "next_page": page + 1 if page < total_pages else None,
        "start_index": start,
        "end_index": end,
    }


def normalize_page_size(raw):
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return 1
    return max(1, min(100, value))


def apply_page_params(page_params, query):
    if not page_params:
        return query, 1
    page = normalize_page_size(page_params.get("page", 1))
    page_size = normalize_page_size(page_params.get("page_size", 10))
    query = query.page(page).per_page(page_size)
    return query, page_size


def page_info(page_params, total):
    if not page_params:
        return build_pagination(total, 1, 10)
    page = normalize_page_size(page_params.get("page", 1))
    page_size = normalize_page_size(page_params.get("page_size", 10))
    return build_pagination(total, page, page_size)
