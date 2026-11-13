# === Stage 6: Генерация идентификаторов ===
# Project: BirdSpotter
PREFIX = "bsp"
_RESERVED = {"id", "name"}


def generate_id(prefix: str = PREFIX, counter: list[int] | None = None) -> str:
    counter = counter if counter is not None else [0]
    while True:
        candidate = f"{prefix}-{counter[0]}"
        counter[0] += 1
        if candidate not in _RESERVED:
            return candidate


def is_unique(candidate: str, reserved: set[str] | None = None) -> bool:
    reserved = reserved if reserved is not None else _RESERVED
    return candidate not in reserved


class IdentifierRegistry:
    def __init__(self, prefix: str = PREFIX):
        self.prefix = prefix
        self._used: set[str] = set(_RESERVED)
        self._counter = 0

    def make(self) -> str:
        while not is_unique(self.generate_id(self.prefix, [self._counter]), self._used):
            self._counter += 1
        self._used.add(self.generate_id(self.prefix, [self._counter]))
        return self.generate_id(self.prefix, [self._counter])

    def contains(self, value: str) -> bool:
        return value in self._used

    def __len__(self) -> int:
        return len(self._used)
