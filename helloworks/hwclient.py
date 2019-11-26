from .utils import ApiEndpoints, HwRequest, HwAccess, _file_downloader, _clean_dict 
from .utils.exceptions import get_exception_message

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
        """
            Method to create an instance of a Workflow to send out to a user.
        """
        create_workflow_url = self.endpoints.create_workflow_instance()
        dict_response = self._post_workflow_instance(create_workflow_url,
                                            workflow_id=workflow_id,
                                            participants=participants,
                                            merge_fields=merge_fields,
                                            callback_url=callback_url,
                                            redirect_url=redirect_url,
                                            document_delivery=document_delivery,
                                            white_label_id=white_label_id,
                                            delegated_authentication=delegated_authentication,
                                            metadata=metadata,
                                            document_delivery_type=document_delivery_type)

        return dict_response


    def preview_workflow_instance(self,
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
        """
            Method to create a preview instance of a Workflow to send out to a user.
        """
        preview_workflow_url = self.endpoints.preview_workflow_instance()
        dict_response = self._post_workflow_instance(preview_workflow_url,
                                            workflow_id=workflow_id,
                                            participants=participants,
                                            merge_fields=merge_fields,
                                            callback_url=callback_url,
                                            redirect_url=redirect_url,
                                            document_delivery=document_delivery,
                                            white_label_id=white_label_id,
                                            delegated_authentication=delegated_authentication,
                                            metadata=metadata,
                                            document_delivery_type=document_delivery_type)
        return dict_response

    def cancel_workflow_instance(self, workflow_instance_id):
        """
            Method to cancel a Workflow Instance that is currently active
        """
        cancel_workflow_url = self.endpoints.cancel_workflow_instance(workflow_instance_id)
        token = self.access.get_jwt_token()
        response = self.request.put(cancel_workflow_url, token)
        if response.status_code != 200:
            exc_msg = get_exception_message(response)
            raise Exception(exc_msg)
        return response.json()

    def get_workflow_instance(self, workflow_instance_id):
        """
            Method to retrieve information on a single Workflow Instance
        """
        get_workflow_url = self.endpoints.get_workflow_instance(workflow_instance_id)
        token = self.access.get_jwt_token()
        response = self.request.get(get_workflow_url, token)
        if response.status_code != 200:
            exc_msg = get_exception_message(response)
            raise Exception(exc_msg)
        return response.json().get('data')

    def get_workflow_instance_document(self, workflow_instance_id, document_id, get_request=True):
        """
            Method to get a given document of a workflow instance
            If get_request is set to true it will return the request instead of writing the file
        """
        get_workflow_document_url = self.endpoints.get_workflow_instance_document(workflow_instance_id, document_id)
        return self._file_endpoints(get_workflow_document_url, f'{document_id}.pdf', get_request)


    def get_workflow_instance_audit_trail(self, workflow_instance_id, get_request=True):
        """
            Method to get the audit trail of a workflow instance
            If get_request is set to true it will return the request instead of writing the file
        """
        get_workflow_audit_trail_url = self.endpoints.get_workflow_instance_audit_trail(workflow_instance_id)
        return self._file_endpoints(get_workflow_audit_trail_url, f'{workflow_instance_id}-audit-trail.pdf', get_request)

    def get_workflow_instance_documents(self, workflow_instance_id, get_request=True):
        """
            Method to get the documents of a workflow instance
            If get_request is set to true it will return the request instead of writing the file
        """
        get_workflow_documents_url = self.endpoints.get_workflow_instance_documents(workflow_instance_id)
        return self._file_endpoints(get_workflow_documents_url, f'{workflow_instance_id}-files.zip', get_request)

    def get_workflow_instance_steps(self, workflow_instance_id):

        """
            Method to get the specified workflow instance, the step id, the role that will be completing the step,
            the signer's full name, and the unauthenticated url that can be used to start entering information.
        """

        get_workflow_instance_steps_url = self.endpoints.get_workflow_instance_steps(workflow_instance_id)
        token = self.access.get_jwt_token()
        response = self.request.get(get_workflow_instance_steps_url, token)
        if response.status_code != 200:
            exc_msg = get_exception_message(response)
            raise Exception(exc_msg)
        return response.json().get('data')

    def get_document_link(self, workflow_instance_id):
        """
            For the specified workflow instance, get the step id, the role that will be completing the step,
            the signer's full name, and the unauthenticated url that can be used to start entering information.
        """

        get_document_link = self.endpoints.get_document_link(workflow_instance_id)
        token = self.access.get_jwt_token()
        response = self.request.get(get_document_link, token)
        if response.status_code != 200:
            exc_msg = get_exception_message(response)
            raise Exception(exc_msg)
        return response.json().get('data')

    def get_authenticated_link_for_workflow_instance_step(self, workflow_instance_id, step_id):
        """
            Method to get the authenticated link for a workflow instance step
        """
        get_authentiated_link_for_workflow_instances_step_url = self.endpoints.get_authenticated_link_for_workflow_instances_step(workflow_instance_id, step_id)
        token = self.access.get_jwt_token()
        response = self.request.get(get_authentiated_link_for_workflow_instances_step_url, token)
        if response.status_code != 200:
            exc_msg = get_exception_message(response)
            raise Exception(exc_msg)
        return response.json().get('data')

    def save_setting_with_logo_file(self, **kwars):
        raise NotImplementedError('This method has not been implemented yet')

    def _file_endpoints(self, endpoint, file_name, get_request):
        token = self.access.get_jwt_token()
        request = self.request.get(endpoint, token)
        if get_request:
            return request
        return _file_downloader(file_name, request)

    def _post_workflow_instance(self, endpoint, **params):
        token = self.access.get_jwt_token()
        params = _clean_dict(params)

        response = self.request.post(endpoint, token, params)
        if response.status_code != 200:
            exc_msg = get_exception_message(response)
            raise Exception(exc_msg)
        return response.json().get('data')
