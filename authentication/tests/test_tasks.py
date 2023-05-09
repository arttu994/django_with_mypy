import pytest

from authentication.tasks import send_email


@pytest.mark.celery(broker_url="redis://localhost:6379")
def test_tasks_works():
    send_email("", "")
