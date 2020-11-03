from dataclasses import dataclass


@dataclass
class Foo:
    greeting: str = "Hello"

    def greet(self, name: str) -> str:
        return f"{self.greeting}, {name}!"


if __name__ == '__main__':
    my_name: str = "Teodor"
    foo: Foo = Foo()
    greeting: str = foo.greet(my_name)
    print(greeting)
