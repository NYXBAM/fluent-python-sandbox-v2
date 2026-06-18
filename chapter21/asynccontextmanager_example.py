import asyncio
from contextlib import asynccontextmanager
from multiprocessing import process


@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(
        None, download_webpage, url
    )
    yield data 
    await loop.run_in_executor(None, update_stats, url)
    
    async with web_page('google.com') as data: 
        process(data)