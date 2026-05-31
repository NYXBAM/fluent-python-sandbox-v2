from concurrent import futures

from flags_threadpool import download_one
from flags import main
import time 


is_process = True  # Switch to threading or proc

def download_many(cc_list: list[str]) -> int: 
    # cc_list = cc_list[:5]
    executor_cls = futures.ProcessPoolExecutor if is_process else futures.ThreadPoolExecutor
    with executor_cls(max_workers=8) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')
            
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            print(f'{future} result: {res!r}')

    return count 



if __name__ == '__main__':
    main(download_many)