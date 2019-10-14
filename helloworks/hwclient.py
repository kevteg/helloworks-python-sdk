from .utils import ApiEndpoints, HwRequest, HwAccess

class HwClient(object):

    def __init__(self, api_key_id, API_KEY_VALUE):
        self.request = HwRequest()
        self.endpoints = ApiEndpoints()
        self.access = HwAccess(api_key_id, API_KEY_VALUE)
        
    def create_workflow_instance(self,
                                 workflow_id,
                                 participants,
                                 merge_fields=None,
                                 callback_url=None,
                                 redirect_url=None,
                                 document_delivery=True,
                                 white_label_id=None,
                                 delegated_authentication=False,
                                 metadata=None,
                                 document_delivery_type=None):
        create_workflow_url = self.endpoints.create_workflow_instance()
        token = self.access.get_jwt_token()

        params = {
            'workflow_id': workflow_id,
            'participants': participants,
            'document_delivery': document_delivery,
            'delegated_authentication': delegated_authentication,
        }

        _non_default_params = {
            'merge_fields': merge_fields,
            'callback_url': callback_url,
            'redirect_url': redirect_url,
            'white_label_id': white_label_id,
            'metadata': metadata,
            'document_delivery_type': document_delivery_type,
        }

        non_default_params = self._clean_dict(_non_default_params)
        params.update(non_default_params)

        request = self.request.post(create_workflow_url, token, params)
        return request

    @staticmethod
    def _clean_dict(dictionary):
        clean_dict = {**dictionary}
        for key, value in dictionary.items():
            if not value:
                del clean_dict[key]
        return clean_dict

