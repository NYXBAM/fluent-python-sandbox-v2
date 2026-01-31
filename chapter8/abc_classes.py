from collections.abc import Mapping


def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    '''Here we use Mapping instead of dict to allow more general types'''
    ...
    
def name2hex(name: str, color_map: dict[str, int]) -> str:
    '''Here we use dict which is more specific than Mapping'''
    ...