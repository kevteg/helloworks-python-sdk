from .request import HwRequest
from .api_endpoints import ApiEndpoints
from time import time


class HwAccess(object):
    def __init__(self, api_key_id, API_KEY_VALUE):
        self.request = HwRequest()
        self.endpoints = ApiEndpoints()
        self.api_key_id = api_key_id
        self.API_KEY_VALUE = API_KEY_VALUE
        self.expires_at = 0
        self.jwt_token = None

    def get_jwt_token(self):
        '''
        Method to get the latest JWT token
        '''
        now = int(time())
        if self.jwt_token and self.expires_at > now:
            return self.jwt_token
        else:
            self.expires_at, self.jwt_token = self._get_jwt_token()
        return self.jwt_token

    def _get_jwt_token(self):
        auth_token_endpoint = self.endpoints.auth_token(self.api_key_id)
        response = self.request.get(auth_token_endpoint, self.API_KEY_VALUE)
        return self._process_response(response)

    def _process_response(self, response):
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('expires_at'), data.get('token')
        else:
            raise Exception(response.json().get('error', 'Internal error'))
