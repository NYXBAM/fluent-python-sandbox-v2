from typing import Protocol, Any

class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    
class SupportsMul(Protocol):
    def __mul__(self, other: Any) -> Any: ...