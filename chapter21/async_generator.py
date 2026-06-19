import asyncio
from domainlib import multi_probe

names = 'python.org rust-lang.org golang.org no-lang.invalid'.split()

gen_found = (name async for name, found in multi_probe(names) if found)
print(gen_found)


async def start():
    async for name in gen_found:
        print(name)


if __name__ == '__main__':
    asyncio.run(start())
    
    """     <async_generator object <genexpr> at 0x1086fc580>
            python.org
            golang.org
            rust-lang.org
    """ 