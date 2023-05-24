INITIAL_SIZE = 128


class HashMapError(ValueError):
    """
    Custom error class for HashMap
    """

    ...


class HashMap:
    def __init__(self):
        """
        Initialize an empty hash map

        We will use a list of keys and a list of values
        to store the data.

        >>> h = HashMap()
        >>> h
        {}

        >>> h["foo"] = "bar"
        >>> h["foo"]
        'bar'
        """
        self._keys = set()
        self._values = [None] * INITIAL_SIZE

    def _hash(self, key):
        """
        Internal hash function
        """
        return hash(key) % INITIAL_SIZE

    def __getitem__(self, key):
        """
        Implement the `[]` operator to get the value
        associated with a key.

        >>> h = HashMap()
        >>> h["foo"] = "bar"
        >>> h["foo"]
        'bar'
        """
        key_hash = self._hash(key)
        value = self._values[key_hash]

        if value is None:
            raise HashMapError("Key is not present in the map")

        return value

    def __setitem__(self, key, value):
        """
        Implement the `[]=` operator to set the value

        >>> h = HashMap()
        >>> h["foo"] = "bar"
        >>> h["foo"]
        'bar'
        """
        key_hash = self._hash(key)
        self._values[key_hash] = value
        self._keys.add(key)

    def __delitem__(self, key):
        """
        Implement the `del` operator to remove a key

        >>> h = HashMap()
        >>> h["foo"] = "bar"
        >>> h["foo"]
        'bar'
        """
        key_hash = self._hash(key)
        del self._values[key_hash]
        self._keys.remove(key)

    def __iter__(self):
        """
        Implement the `iter` method to return an iterator
        over the keys of the hashmap

        >>> h = HashMap()
        >>> h["foo"] = "bar"
        >>> h["foo"]
        'bar'
        """
        return iter(self._keys)

    def __len__(self):
        """
        Implement the `len` method to return the number of keys
        in the hashmap

        >>> h = HashMap()
        >>> h["foo"] = "bar"
        >>> h["foo"]
        'bar'
        """
        return len(self._keys)
