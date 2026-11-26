# === Stage 12: Быстрые фильтры ===
# Project: BirdSpotter
from __future__ import annotations

import datetime


def _now() -> datetime.datetime:
    return datetime.datetime.now()


def _start_of(day: datetime.datetime) -> datetime.datetime:
    return day.replace(hour=0, minute=0, second=0, microsecond=0)


def is_today(observation: datetime.datetime) -> bool:
    return _start_of(observation) == _start_of(_now())


def is_this_week(observation: datetime.datetime) -> bool:
    week_start = _start_of(_now() - datetime.timedelta(days=_now().weekday()))
    return week_start <= observation < _start_of(_now() + datetime.timedelta(days=(7 - _now().weekday())))


def is_overdue(observation: datetime.datetime) -> bool:
    return observation < _start_of(_now())


def filter_observations(observations, *, today=False, this_week=False, overdue=False) -> list:
    result = []
    for observation in observations:
        if today and not is_today(observation):
            continue
        if this_week and not is_this_week(observation):
            continue
        if overdue and not is_overdue(observation):
            continue
        result.append(observation)
    return result


def filter_observations_by_date_range(observations, start, end) -> list:
    return [observation for observation in observations if start <= observation <= end]
