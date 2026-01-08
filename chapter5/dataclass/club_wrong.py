from dataclasses import dataclass, field
from pickle import FALSE

def test_create_list() -> list:
    return [1,2,3,4,5,6]


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)


s = ClubMember(name='1')
print(s)


@dataclass
class ClubMember1:
    name: str
    guest: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)
    
cm = ClubMember1(name='john',
                 guest=['Doe','Hue', 'Jan'])

print(cm)
print(cm.athlete)