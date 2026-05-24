
import asyncio
import itertools
import spinner_async_nap

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char}{msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')
  
async def slow() -> int:
    # await asyncio.sleep(3)
    large_prime = 5_000_111_000_222_021
    result = await spinner_async_nap.is_prime(large_prime)
    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')
    

async def supervisor() -> int: 
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel()
    return result

if __name__ == '__main__':
    main()