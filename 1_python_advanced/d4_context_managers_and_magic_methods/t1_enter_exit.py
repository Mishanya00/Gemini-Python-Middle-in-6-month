class MockDatabaseSession:
    def __enter__(self):
        print('Starting transaction...')
        return {'amount': 110.99}

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type, '|', exc_val, '|', exc_tb)
            print('Rollback')
            # Test of __exit__ capabilities
            if exc_type is ConnectionError:
                print('Connection error detected')

        print('Commit')
        return True


print('-----------------------------')

a = MockDatabaseSession()
with a as obj:
    print('Division by zero try start')
    b = 1 / 0
    print('Division by zero try finish')

print('-----------------------------')

a = MockDatabaseSession()
with a as obj:
    print('No errors raise here')

print('-----------------------------')

a = MockDatabaseSession()
with a:
    raise ConnectionError

print('-----------------------------')