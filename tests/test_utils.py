import pytest
from app.utils import retry


def test_retry_success():
    @retry(attempts=3, delay=0)
    def success():
        return True

    assert success() is True


def test_retry_failure():
    counter = {"count": 0}

    @retry(attempts=3, delay=0)
    def fail():
        counter["count"] += 1
        raise Exception("Fail")

    with pytest.raises(Exception):
        fail()

    assert counter["count"] == 3
