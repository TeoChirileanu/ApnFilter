from unittest import TestCase

from main import Foo


class TestFoo(TestCase):
    def test_greet(self):
        # Arrange
        name = "Teodor"
        expected_greeting: str = f"Hello, {name}!"

        # Act
        foo: Foo = Foo()
        actual_greeting = foo.greet(name)

        # Assert
        self.assertEqual(expected_greeting, actual_greeting)
