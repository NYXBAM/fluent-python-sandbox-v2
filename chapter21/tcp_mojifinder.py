import asyncio
from asyncio.trsock import TransportSocket
import functools
import sys
from typing import cast
from charindex import InvertedIndex


async def supervisor(index: InvertedIndex, host: str, port: int) -> None:
    server = await asyncio.start_server(
        functools.partial(finder, index),
        host, port
    )
    socket_list = cast(tuple[TransportSocket, ...], server.sockets)
    addr = socket_list[0].getsockname()
    print(f'Serving on {addr}. Hit CTRL-C to stop')
    await server.serve_forever()
    
    
def main(host: str = '127.0.0.1', port_arg: str = '2323'):
    port = int(port_arg)
    print('Building index.')
    index = InvertedIndex()
    try: 
        asyncio.run(supervisor(index, host, port))
    except KeyboardInterrupt:
        print('\nServer shut down')
        
        
if __name__ == '__main__':
    main(*sys.argv[1::])