import requests
import json


class HwRequest(object):

    def _process_request(self, method, url, token, data=None, stream=False, def_headers={}):
        headers = {'Authorization': f'Bearer {token}', **def_headers}
        request_method = getattr(requests, method)
        return request_method(url, json=data, headers=headers, stream=stream)

    def get(self, url, token, data=None, stream=False):
        return self._process_request('get', url, token, data, stream)

    def post(self, url, token, data=None):
        headers = {'Content-Type': 'application/json'}
        return self._process_request('post', url, token, data, headers)

    def delete(self, url, token, data=None):
        return self._process_request('delete', url, token, data)

    def put(self, url, token, data=None):
        return self._process_request('put', url, token, data)
