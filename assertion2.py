import pytest

import pytest


def f():
    #raise SystemError(1)
    raise SystemExit(1)



def test_mytest():
    with pytest.raises(SystemExit):
        f()

test_mytest()