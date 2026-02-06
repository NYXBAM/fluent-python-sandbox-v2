from typing import Optional

def tag(
    name: str,
    /,
    *content: str,
    class_: Optional[str] = None,
    **attrs: str,
) -> str:
    return 'str'  # return here to avoid mypy error: "Missing return statement" because the function is not fully implemented yet
