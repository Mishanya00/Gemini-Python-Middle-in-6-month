import json
import os
from random import randint
import time
import pickle

import orjson
import faker


fake = faker.Faker()


def get_file_data(filename):
    if os.path.exists(filename):
        print(f'Loading data from {filename}...')
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        print(f"Loaded data from {filename}. Length: {len(data)}")
        return data
    else:
        print(f'File {filename} not found. Generating new data...')

        fake = faker.Faker()

        data = [
            {
                'Name': fake.name(),
                'Age': randint(1, 1000),
            }
            for _ in range(100000)
        ]

        with open (filename, 'wb') as f:
            pickle.dump(data, f)

        print(f'Saved data to {filename}. Length: {len(data)}')

        return data


def timedelta(rounds=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Method `' + func.__name__ + '` benchmark started.')
            total_ms = 0

            for i in range(rounds):
                start_time = time.time()

                func(*args, **kwargs)

                finish_time = time.time()
                dt_ms = (finish_time - start_time) * 1000
                total_ms += dt_ms

            avg_dt_ms = total_ms / rounds
            print('Method `' + func.__name__ + f'`:')
            print(f'Average execution time: {avg_dt_ms} (ms)')
            print(f'Total time: {total_ms} (ms). Attempts: {rounds}')

        return wrapper
    return decorator


@timedelta(rounds=1000)
def builtin_json_benchmark(to_serialize):
    json.dumps(to_serialize)


@timedelta(rounds=1000)
def orjson_benchmark(to_serialize):
    orjson.dumps(to_serialize)


if __name__ == '__main__':
    target_filename = 'people_data.pkl'
    curr_file_dir = os.path.dirname(__file__)
    filename = curr_file_dir + '/' + target_filename

    people_registry = get_file_data(filename)

    # builtin_json_benchmark(people_registry)
    orjson_benchmark(people_registry)
