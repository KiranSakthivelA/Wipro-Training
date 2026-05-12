import pytest

@pytest.fixture(scope='function', autouse=True)
# def setup():
#     print('Fixture')

def setup_teardown():
    print('Starts... ')
    yield

    print(' Ends !')
