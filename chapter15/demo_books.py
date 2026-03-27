from books import BookDict
from typing import TYPE_CHECKING, TypedDict, reveal_type

def demo() -> None:
    book = BookDict(
        isbn='135123151231',
        title='Refactoring 2e',
        authors=['Martin Fowler', 'Kent Beck'],
        pagecount=448
    )
    authors = book['authors']
    if TYPE_CHECKING:
        reveal_type(authors)
        authors = 'Bob'
        book['weight'] = 4.2
        del book['title']

if __name__ == '__main__':
    demo()