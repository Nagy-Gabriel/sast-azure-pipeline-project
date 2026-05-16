from app.vulnerable_app import ping_host


def test_ping_host_exists():
    assert callable(ping_host)