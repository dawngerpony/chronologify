from chronologify import app


def test_hello_world():
    result = app.hello_world()
    assert "Hell, World" in result
