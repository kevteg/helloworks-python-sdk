import pytest
from helloworks import HwClient
import json

post_create_preview_workflow_payload = {
    'data': {
         'id': '8iiSbkFMiCoqAnpG',
         'mode': 'test',
         'steps': [{'participant': 'Kevin Hernandez',
                    'role': 'Candidate',
                    'step': 'participant_QIxDNu_signer_step',
                    'url': 'https://app.helloworks.com/entry/view_instance/T5kezKNj2DOU9Dl1'}]
    }
}

get_authenticated_link_payload = {
    'data': {
        "url": "https://app.helloworks.com/authenticated-url"
    }
}


get_document_link_payload = {
    'data': "https://app.helloworks.com/files-url"
}


def get_workflow(webhook_instance_id):
    response = {
        'data': {
            'audit_trail_hash': 'bbc19870ae6789c9eb36134a617135d790d8f4ff8396593641f8d48536a443f8',
            'data': {
                'Form_WnGEdO': {
                    'field_6Updlr': 'OTJltH6tCinDU2UV',
                    'field_ROPEte': 'Kevin'
                }
            },
            'document_hashes': {
                'Form_WnGEdO': 'd874a13fb2f5823936694a1bc0230519a8f4033fd79af099953c1fb9643f5702',
                'Form_WnGEdO.field_6Updlr': '2b5da64850038beb03b62094dd33596d4cb0e3640cc78cf0379c3a37459440fb'
            },
            'id': webhook_instance_id,
            'mode': 'test',
            'status': 'completed',
            'workflow_id': 'MECIfQ9POAngarAj'
        }
    }
    return response


get_workflow_step = {
    'data': [{
        'participant': 'Kevin Hernandez',
        'role': 'Candidate',
        'step': 'participant_QIxDNu_signer_step',
        'url': 'https://app.helloworks.com/entry/view_instance/GzkJVC8VggOelpOr'}]
}


def get_response(payload):
    class Data:
        status_code = 200
        text = json.dumps(payload)

        def json(self):
            return payload
    return Data()


@pytest.fixture
def participants():
    return {
        "participant_QIxDNu": {
            "type": "email",
            "value": "user@test.com",
            "full_name": "Kevin Hernandez"
        }
    }


@pytest.fixture
def fake_method(monkeypatch):
    def _(function, payload):
        def method(*args, **kwargs):
            return get_response(payload)

        monkeypatch.setattr(function, method)
    return _


@pytest.fixture
def fake_create_preview_instance(fake_method):
    fake_method('requests.post', post_create_preview_workflow_payload)


@pytest.fixture
def fake_cancel_workflow_instance(fake_method):
    fake_method('requests.put', {})


@pytest.fixture
def fake_get_workflow_instance(monkeypatch):
    def fake_method(url, **kwargs):
        workflow_instance_id = url.split('/')[-1]
        return get_response(get_workflow(workflow_instance_id))

    monkeypatch.setattr('requests.get', fake_method)


@pytest.fixture
def fake_get_workflow_instance_steps(fake_method):
    fake_method('requests.get', get_workflow_step)


@pytest.fixture
def fake_get_workflow_steps_authenticated_link(fake_method):
    fake_method('requests.get', get_authenticated_link_payload)


@pytest.fixture
def fake_document_link(monkeypatch):
    fake_method('requests.get', get_document_link_payload)


@pytest.fixture
def fake_auth(monkeypatch):
    def fake_get_jwt_token(*args):
        return 0, 'jwt_token'

    monkeypatch.setattr('helloworks.utils.access.HwAccess._get_jwt_token', fake_get_jwt_token)


@pytest.fixture
def hwclient(fake_auth):
    return HwClient("api_key_id", "API_KEY_VALUE")


@pytest.fixture
def fake_file_downloader(fake_method, monkeypatch):
    def fake_file_method(*args):
        return True

    fake_method('requests.get', {})
    monkeypatch.setattr('helloworks.utils.helper._file_downloader', fake_file_method)
