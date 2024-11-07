from datetime import datetime
from multiprocessing.pool import ThreadPool
import requests


def run_hello_world_request(number: int):
    print(f'{number} - Sending request {number}')
    requests.get('http://localhost:8000/hello-world')
    print(f' {number} - Request {number} completed')


if __name__ == '__main__':
    pool = ThreadPool(600)

    start = datetime.now()
    pool.map(run_hello_world_request, range(10000))

    pool.close()
    end = datetime.now()

    print(f'Total time: {(end - start).total_seconds()} seconds')