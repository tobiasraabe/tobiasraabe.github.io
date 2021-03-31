Title: How I write tests
Date: 2021-03-31
Tags: Python, Testing, Tests
Author: Tobias Raabe

Hi everybody,

I assume that all of you write tests for Python programs with
[pytest](https://pytest.org/). If you do not use pytest or if you do not even write
tests, you should check out the following links which are useful and provide some
examples and an overview of pytest's capabilities.

- [Effective Python Testing With Pytest - Real
  Python](https://realpython.com/pytest-python-testing/)
- [Customizing your pytest suite (Part 1) - Raphael
  Pierzina](https://raphael.codes/blog/customizing-your-pytest-test-suite-part-1/)
- [Customizing your pytest suite (Part 2) - Raphael
  Pierzina](https://raphael.codes/blog/customizing-your-pytest-test-suite-part-2/)

Maybe you should also have heard about test driven development (TDD), but I have little
experience with it myself. If you have a great resource for beginners, send it my way
and I can include it here.

What I did not find in these guides is a combination of patterns I use fairly often to
write tests. Hopefully, it is useful for you as well. Let's go!

### The function

First, here is the function we are going to test. The function takes any number of paths
and tries to find the longest parent path common to all paths.

```python
def find_common_ancestor(*paths: Union[str, Path]) -> Path:
    """Find a common ancestor of many paths."""
    paths = [path if isinstance(path, PurePath) else Path(path) for path in paths]

    for path in paths:
        if not path.is_absolute():
            raise ValueError(
                f"Cannot find common ancestor for relative paths. {path} is relative."
            )

    common_parents = set.intersection(*[set(path.parents) for path in paths])

    if len(common_parents) == 0:
        raise ValueError("Paths have no common ancestor.")
    else:
        longest_parent = sorted(common_parents, key=lambda x: len(x.parts))[-1]

    return longest_parent
```

Here is an example:

```pycon
>>> find_common_ancestor("C:\\Users\\Tobias", "C:\\Users\\Tobi")
WindowsPath('C:/Users')
```

The function returns errors if ...

- one of the paths is relative.
- the paths do not have a common ancestor.


### The test function

I will first show you the test function and, then, comment on some details.

```python
from contextlib import ExitStack as does_not_raise  # noqa: N813
from pathlib import Path
from pathlib import PurePosixPath
from pathlib import PureWindowsPath

import pytest


@pytest.mark.unit
@pytest.mark.parametrize(
    "path_1, path_2, expectation, expected",
    [
        pytest.param(
            PurePosixPath("relative_1"),
            PurePosixPath("/home/relative_2"),
            pytest.raises(
                ValueError, match="Cannot find common ancestor for relative paths."
            ),
            None,
            id="test path 1 is relative",
        ),
        pytest.param(
            PureWindowsPath("C:/home/relative_1"),
            PureWindowsPath("relative_2"),
            pytest.raises(
                ValueError, match="Cannot find common ancestor for relative paths."
            ),
            None,
            id="test path 2 is relative",
        ),
        pytest.param(
            PurePosixPath("/home/user/folder_a"),
            PurePosixPath("/home/user/folder_b/sub_folder"),
            does_not_raise(),
            PurePosixPath("/home/user"),
            id="normal behavior with UNIX paths",
        ),
        pytest.param(
            PureWindowsPath("C:\\home\\user\\folder_a"),
            PureWindowsPath("C:\\home\\user\\folder_b\\sub_folder"),
            does_not_raise(),
            PureWindowsPath("C:\\home\\user"),
            id="normal behavior with Windows paths",
        ),
        pytest.param(
            PureWindowsPath("C:\\home\\user\\folder_a"),
            PureWindowsPath("D:\\home\\user\\folder_b\\sub_folder"),
            pytest.raises(ValueError, match="Paths have no common ancestor."),
            None,
            id="no common ancestor",
        ),
    ],
)
def test_find_common_ancestor(path_1, path_2, expectation, expected):
    with expectation:
        result = find_common_ancestor(path_1, path_2)
        assert result == expected
```

- Use ``pytest.mark.parametrize`` to minimize the test code and to make adding more
  tests easier.

- Use ``pytest.param`` to wrap each iteration. It allows to add the ``id`` parameter to
  each iteration. Use the id to document the specific test case. With many test cases,
  you will quickly forget the purpose of each single test.

- The third argument of the parametrization, ``expectation``, can be used to assert that
  the tested function throws an exception. In case no exception is thrown, use
  ``does_not_raise()``.

- If you expect an exception, you can pick an arbitrary object as the ``expected``
  output.


### Conclusion

I hope you enjoyed this tutorial. Feel free to send me any feedback.

*PS: When I started writing this guide, I discovered this
[function](https://docs.python.org/3/library/os.path.html#os.path.commonpath). Maybe I
do not need my implementation plus the tests*.
