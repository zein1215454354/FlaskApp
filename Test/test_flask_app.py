
import unittest
from FlaskApp import app 

class TestFlaskScript(unittest.TestCase):


    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'


if __name__ == '__main__':
    unittest.main()