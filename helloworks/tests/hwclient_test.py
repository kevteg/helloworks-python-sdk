import pytest
import _io

def test_create_workflow_instance(fake_create_preview_instance, participants, hwclient):
    response = hwclient.create_workflow_instance("MECIfQ9POAngarAj", participants)
    assert response['steps'][0]['participant'] == participants['participant_QIxDNu']['full_name']


def test_preview_workflow_instance(fake_create_preview_instance, participants, hwclient):
    response = hwclient.preview_workflow_instance("MECIfQ9POAngarAj", participants)
    assert response['steps'][0]['participant'] == participants['participant_QIxDNu']['full_name']


def test_cancel_workflow_instance(fake_cancel_workflow_instance, hwclient):
    response = hwclient.cancel_workflow_instance("8iiSbkFMiCoqAnpG")
    assert response == {}


def test_get_workflow_instance(fake_get_workflow_instance, hwclient):
    workflow_instance_id = "8iiSbkFMiCoqAnpG"
    response = hwclient.get_workflow_instance(workflow_instance_id )
    assert workflow_instance_id == response['id']


def test_workflow_steps(fake_get_workflow_instance_steps, hwclient):
    response = hwclient.get_workflow_instance_steps("8iiSbkFMiCoqAnpG")
    assert 'participant' in response[0]


def test_authenticated_link_for_workflow_instance_step(fake_get_workflow_steps_authenticated_link, hwclient):
    response = hwclient.get_authenticated_link_for_workflow_instance_step("8iiSbkFMiCoqAnpG", "participant_QIxDNu_signer_step")
    assert 'url' in response


def test_document_link(fake_document_link, hwclient):
    response = hwclient.get_document_link("8iiSbkFMiCoqAnpG")
    assert 'http' in response


def test_workflow_instance_documents(fake_file_downloader, hwclient):
    response = hwclient.get_workflow_instance_documents("8iiSbkFMiCoqAnpG")
    assert response.status_code == 200


def test_workflow_instance_audit_trail(fake_file_downloader, hwclient):
    response = hwclient.get_workflow_instance_audit_trail("8iiSbkFMiCoqAnpG")
    assert response.status_code == 200


def test_workflow_instance_document(fake_file_downloader, hwclient):
    response = hwclient.get_workflow_instance_document("8iiSbkFMiCoqAnpG","Form_WnGEdO")
    assert response.status_code == 200


def test_save_setting_with_logo_file(fake_file_uploader, hwclient):
    f = _io.BytesIO(b'')
    response = hwclient.save_setting_with_logo_file(logo_file=f,
                                                    logo_hidden=False, 
                                                    logo_name='logo.png')
    assert 'white_label_id' in response


def test_save_setting_with_logo_file_wrong_name(fake_file_uploader, hwclient):
    f = _io.BytesIO(b'')
    try:
        response = hwclient.save_setting_with_logo_file(logo_file=f,
                                                        logo_hidden=False, 
                                                        logo_name='logo.pdf')
    except Exception as e:
        assert str(e) == "Wrong file extension, must be one of ['png', 'jpeg', 'jpg', 'gif']"
