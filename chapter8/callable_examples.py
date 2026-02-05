from collections.abc import Callable

def update(
    probe: Callable[[], float],
    display: Callable[[float], None]
) -> None:
    temperature = probe()
    display(temperature)
    
def probe_ok() -> int:
    return 42

def display_wrong(temperature: int) -> None:
    print(hex(temperature))
    
# update(probe_ok, display_wrong) # Mypy error: Argument 2 to "update" has incompatible type "Callable[[int], None]"; expected "Callable[[float], None]"

def display_ok(temperature: complex) -> None:
    print(temperature)
    
update(probe_ok, display_ok) # No mypy error