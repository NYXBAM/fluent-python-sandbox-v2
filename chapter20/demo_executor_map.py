from time import sleep, strftime
from concurrent import futures

def display(*args):
    message = ' '.join(str(arg) for arg in args)
    print(f"{strftime('[%H:%M:%S]')} {message}")
    
def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10

def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=5)
    results = executor.map(loiter, range(15))
    display('results:', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display(f'result {i}: {result}')
        
if __name__ == '__main__':
    main()