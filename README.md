Zip function in reverse.
------------------------

Python implementation of built-in `zip` (i.e. slow). You should probably be looking into numpy arrays, or pandas.

```python
unzip(items: Iterable, cls: Callable = list, ocls: Callable = tuple) -> Iterable:
```

Install pip (`sudo apt install python3-pip` on debian), clone the repository and install the package locally (and probably inside your virtual environment).

```bash
git clone https://github.com/Trasp/python-unzip.git
cd python-unzip
pip3 install .
```

To use list cointainers, simply import unzip.unzip and run `unzip(zipped)`.

```python
from unzip import unzip

unzip(zip(["a","b","c"],[1,2,3])) == (["a","b","c"],[1,2,3])
```

To use deques, or other any container sporting append, pass a factory function.

```python
from collections import deque

unzip([("a",1),("b",2)], deque, list) == [deque(["a","b"]),deque([1,2])]
```
