"""명령행에서 이름을 받아 한 줄 인사말을 출력한다."""

import sys


def greet(name: str) -> str:
    """``Hello, <name>!`` 형식의 인사말을 반환한다."""
    return f"Hello, {name}!"


def main() -> int:
    """첫 번째 인수를 이름으로 받아 인사말을 출력하고 0을 반환한다."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    raise SystemExit(main())
