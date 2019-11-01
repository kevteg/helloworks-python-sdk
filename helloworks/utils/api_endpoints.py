
class ApiEndpoints(object):
    def __init__(self, version='v3'):
        self.version = version
        self.API_URL = 'https://api.helloworks.com'
        self.API_ENDPOINTS = {
            'v3': {
                'auth_token': 'token/{}',
                'create_workflow_instance': 'workflow_instances',
                'preview_workflow_instance': 'workflow_instances/preview',
                'cancel_workflow_instance': 'workflow_instances/{}/cancel',
                'get_workflow_instance': 'workflow_instances/{}',
                'get_workflow_instance_document': 'workflow_instances/{}/documents/{}',
                'get_workflow_instance_audit_trail': 'workflow_instances/{}/audit_trail',
                'get_workflow_instance_documents': 'workflow_instances/{}/documents',
                'get_workflow_instance_steps': 'workflow_instances/{}/steps',
                'get_document_link': 'workflow_instances/{}/document_link',
                'get_authenticated_link_for_workflow_instances_step': 'workflow_instances/{}/steps/{}/delegate_auth',
                'save_settings_with_logo_file': 'white_label/settings'
            }
        }

    def __generate_url(self, url):
        endpoint = f'{self.API_URL}/{self.version}/{self.API_ENDPOINTS[self.version][url]}'
        return endpoint

    def auth_token(self, api_key_id):
        return self.__generate_url('auth_token').format(api_key_id)

    def create_workflow_instance(self):
        return self.__generate_url('create_workflow_instance')

    def preview_workflow_instance(self):
        return self.__generate_url('preview_workflow_instance')

    def cancel_workflow_instance(self, workflow_instance_id):
        return self.__generate_url('cancel_workflow_instance').format(workflow_instance_id)

    def get_workflow_instance(self, workflow_instance_id):
        return self.__generate_url('get_workflow_instance').format(workflow_instance_id)

    def get_workflow_instance_document(self, workflow_instance_id, document_id):
        return self.__generate_url('get_workflow_instance_document').format(workflow_instance_id, document_id)

    def get_workflow_instance_audit_trail(self, workflow_instance_id):
        return self.__generate_url('get_workflow_instance_audit_trail').format(workflow_instance_id)

    def get_workflow_instance_documents(self, workflow_instance_id):
        return self.__generate_url('get_workflow_instance_documents').format(workflow_instance_id)

    def get_workflow_instance_steps(self, workflow_instance_id):
        return self.__generate_url('get_workflow_instance_steps').format(workflow_instance_id)

    def get_document_link(self, workflow_instance_id):
        return self.__generate_url('get_document_link').format(workflow_instance_id)

    def get_authenticated_link_for_workflow_instances_step(self, workflow_instance_id, step_id):
        return self.__generate_url('get_authenticated_link_for_workflow_instances_step').format(workflow_instance_id, step_id)

    def save_settings_with_logo_file(self):
        return self.__generate_url('save_settings_with_logo_file')
