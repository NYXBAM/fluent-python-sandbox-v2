import asyncio
from http import HTTPStatus
from chapter21.flags2_asyncio import DownloadStatus, get_flag, save_flag
import httpx




async def get_country(client: httpx.AsyncClient, base_url: str, cc: str) -> str: 
    url = f'{base_url}/{cc}/metadata.json'.lower()
    resp = await client.get(url, timeout=3.1, follow_redirects=True)
    resp.raise_for_status()
    metadata = resp.json()
    return metadata['country']


async def download_one(client: httpx.AsyncClient,
                       cc: str,
                       base_url: str,
                       semaphore: asyncio.Semaphore,
                       verbose: bool) -> DownloadStatus:
    try:
        async with semaphore:
            image = await get_flag(client, base_url, cc)
        async with semaphore:
            country = await get_country(client, base_url, cc)
    except httpx.HTTPStatusError as exc:
        res = exc.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'Not found: {res.url}'
        else:
            raise
        
    else:
        filename = country.replace(' ', '_')
        await asyncio.to_thread(save_flag, image, f'{filename}.gif')
        status = DownloadStatus.OK
        msg = 'OK'
        
    if verbose and msg: 
        print(cc, msg)
    return status 

