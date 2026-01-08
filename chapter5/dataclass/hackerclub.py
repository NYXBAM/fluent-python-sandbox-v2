from dataclasses import dataclass
from club_wrong import ClubMember

@dataclass
class HackerClubMember(ClubMember):
    all_handlers = set()
    handle: str = ''
    
    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handlers:
            msg = f'Handle {self.handle} already taken!'
            raise ValueError(msg)
        cls.all_handlers.add(self.handle)
        

anna = HackerClubMember('Anna Ravenscroft', handle='AnnaRaven')
print(anna) # HackerClubMember(name='Anna Ravenscroft', guests=[], handle='AnnaRaven')

leo = HackerClubMember('Leo Rochael')
print(leo) # HackerClubMember(name='Leo Rochael', guests=[], handle='Leo')

# leo2 = HackerClubMember('Leo Smith', handle='Leo')
# print(leo2) # ValueError: Handle Leo already taken!

leo2 = HackerClubMember('Leo Smith', handle='Neo')
print(leo2) # HackerClubMember(name='Leo Smith', guests=[], handle='Neo')


print(HackerClubMember.all_handlers) # {'Leo', 'Neo', 'AnnaRaven'}
print(HackerClubMember.__doc__)  # HackerClubMember(name: str, guests: list = <factory>, handle: str = '')
