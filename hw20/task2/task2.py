from typing import List, Set, Dict, Tuple, Optional

# For simple built-in types, just use the name of the type
a: int = 1
b: float = 1.0
c: bool = True
d: str = "test"
e: bytes = b"test"

# For collections, the type of the collection item is in brackets
# (Python 3.9+)
a1: list[int] = [1]
b1: set[int] = {6, 7}
print(a1)
print(b1)

# In Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
c1: List[int] = [1]
d1: Set[int] = {6, 7}
print(c1)
print(d1)


# Same as above, but with type comment syntax (Python 3.5 and earlier)
a2 = [1]  # type: List[int]
print(a2)

# For mappings, we need the types of both keys and values
b2: dict[str, float] = {"field": 2.0}  # Python 3.9+
c2: Dict[str, float] = {"field": 2.0}

# For tuples of fixed size, we specify the types of all the elements
d2: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+
a3: Tuple[int, str, float] = (3, "yes", 7.5)
print(d2)
print(a3)

# For tuples of variable size, we use one type and ellipsis
b3: tuple[int, ...] = (1, 2, 3)  # Python 3.9+
c3: Tuple[int, ...] = (1, 2, 3)

# Mypy understands a value can't be None in an if-statement
if d is not None:
    print(d.upper())
# If a value can never be None due to some invariants, use an assert
assert d is not None
print(d.upper())