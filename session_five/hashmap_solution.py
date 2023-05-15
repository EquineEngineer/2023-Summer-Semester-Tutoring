from __future__ import annotations

from typing import MutableMapping, TypeVar, Hashable, Final, Mapping, Iterator


MAX_SIZE: Final[int] = 128

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


class HashMap(MutableMapping[K, V | None]):
    def __init__(self, init_data: Mapping[K, V] | None = None):
        self._keys: list[K | None] = [None] * MAX_SIZE
        self._values: list[V | None] = [None] * MAX_SIZE

        if init_data is not None:
            for key, value in init_data.items():
                self[key] = value

    def _internal_hash(self, key: K) -> int:
        return hash(key) % len(self._keys)

    def __getitem__(self, key: K) -> V | None:
        index = self._internal_hash(key)
        return self._values[index]

    def __setitem__(self, key: K, value: V | None) -> None:
        index = self._internal_hash(key)
        self._keys[index] = key
        self._values[index] = value

    def __delitem__(self, key: K) -> None:
        index = self._internal_hash(key)
        self._keys[index] = None
        self._values[index] = None

    def __iter__(self) -> Iterator[K]:
        return iter(key for key in self._keys if key is not None)

    def __len__(self) -> int:
        return len(self._keys)


def main() -> int:
    hashmap = HashMap[str, str]()
    # hashmap = {}

    hashmap["foo"] = "bar"
    hashmap["baz"] = "qux"

    print(hashmap["foo"])
    print(hashmap["baz"])

    del hashmap["foo"]

    print(hashmap.get("foo", None))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
