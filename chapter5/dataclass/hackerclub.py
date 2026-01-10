from dataclasses import InitVar, dataclass
from email.errors import NonPrintableDefect
from types import NoneType
from typing import ClassVar
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


# @dataclass
# class C:
#     i: int
#     j: int = None 
#     database: InitVar[DatabaseType] = None
    
#     def __post__ini__(self, database):
#         if self.j is None and database is not None:
#             self.j = database.lookup('j')
        
        
# c = C(10, database=my_database)


# Example how to use ClassVar and InitVar
# This my own example, not from the book

@dataclass
class Hacker:
    used_handles: ClassVar[set[str]] = set()
    name: str
    handle: str = ""
    
    secret_code: InitVar[str] = None
    
    def __post_init__(self, secret_code):
        if secret_code != '1234':
            raise ValueError("Invalid secret code")
        
        if self.handle:
            self.handle = self.name.lower().replace(" ", "_")
            
        if self.handle in Hacker.used_handles:
            raise ValueError(f"Handle {self.handle} already taken!")
        
        Hacker.used_handles.add(self.handle)
         
        
h1 = Hacker(name="John", secret_code='1234')
# print(h1) #Hacker(name='John', handle='')
# h2 = Hacker(name="Jane", handle='j', secret_code='12') # ValueError: Invalid secret code