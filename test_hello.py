from hello import greet


def test_default_greeting():
    assert greet() == "Hello, MLOps Student! Your MLOps pipeline is working."


def test_custom_greeting():
    assert greet("Shreya") == "Hello, Shreya! Your MLOps pipeline is working."
