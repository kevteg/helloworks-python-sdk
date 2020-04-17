import requests
import json


class HwRequest(object):

    def _process_request(self,
                         method,
                         url,
                         token,
                         data=None,
                         files=None):
        headers = {'Authorization': f'Bearer {token}'}
        request_method = getattr(requests, method)
        return request_method(url, json=data, headers=headers, files=files)

    def get(self, url, token, data=None):
        return self._process_request('get', url, token, data)

    def post(self, url, token, data=None, files=None):
        return self._process_request('post', url, token, data, files)

    def delete(self, url, token, data=None):
        return self._process_request('delete', url, token, data)

    def put(self, url, token, data=None):
        return self._process_request('put', url, token, data)
