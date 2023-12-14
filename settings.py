TEMPLATE_FOLDER = '../../templates'
PORT = 5000
DEBUG = False
TEST = True
DATABASE_URL = 'sqlite:///log.db'
SECRET_KEY = 'key'
API_URL = 'http://example.com/'
DUMMY_SUCCESS_RESPONSE_JSON = {
     "success": True,
     "message": "success",
     "estimated_data": {
         "class": 3,
         "confidence": 0.8683
     }
}
DUMMY_FAILURE_RESPONSE_JSON = {
     "success": False,
     "message": "Error:E50012",
     "estimated_data": {}
}

