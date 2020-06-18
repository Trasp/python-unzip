Zip function in reverse.
------------------------

```python
unzip(items: Iterable, cls: Callable = list, ocls: Callable = tuple) -> Iterable:
```

To use list cointainers, simply run `unzip(zipped)`, as

```python
from unzip import unzip

unzip(zip(["a","b","c"],[1,2,3])) == (["a","b","c"],[1,2,3])
```

To use deques, or other any container sporting append, pass a factory function.

```python
from collections import deque

unzip([("a",1),("b",2)], deque, list) == [deque(["a","b"]),deque([1,2])]
```
