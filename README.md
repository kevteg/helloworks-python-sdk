

[![Maintainability](https://api.codeclimate.com/v1/badges/d0fdc2372d8384e6db9b/maintainability)](https://codeclimate.com/github/kevteg/helloworks-python-sdk/maintainability) [![CircleCI](https://circleci.com/gh/kevteg/helloworks-python-sdk.svg?style=svg)](https://circleci.com/gh/kevteg/helloworks-python-sdk)

# helloworks-python-sdk 🐍

Easily create and manage HelloWorks workflow instances. 🚀

## Installation

    pip install helloworks-python-sdk

## Initial setup

Go to your HelloWorks account and get your public key ID and your private key value

Remember to record the private key immediately and store it in a safe place. The private key value cannot be retrieved later, however keys can be generated at any time.

[See their docs](https://docs.helloworks.com/v3.3/reference#getting-started)
```
from helloworks import HwClient
client = HwClient(api_key_id, api_key_value)
```

- **Note**: Tokens will be refreshed and managed internally
- **Note**: Methods will return a dictionary of HW response

## Create a workflow instance
Method to create an instance of a Workflow to send out to a user:

```
workflow_id = 'IDs located in API request info'
# Participants is a dictionary of dictionaries
participants = {'participant_QIxDNu': {'type': 'email',
				       'value': 'kevteg05@gmail.com', 
				       'full_name': 'Kevin Hernandez'}}
# Merge fields is a dictionary of the available merge fields at Api request info
merge_fields = {'applicantName_f2GtnW': 'Kevin', 'jobTitle_WCUZlG': 'Test'}
response = client.create_workflow_instance(workflow_id, participants, merge_fields)
```

[See the full list of available fields](https://docs.helloworks.com/reference#create-workflow-instance)

## Preview a workflow instance
Method to create a preview instance of a Workflow to send out to a user:

```
workflow_id = 'IDs located in API request info'
# Participants is a dictionary of dictionaries
participants = {'participant_QIxDNu': {'type': 'email',
				       'value': 'kevteg05@gmail.com', 
				       'full_name': 'Kevin Hernandez'}}
# Merge fields is a dictionary of the available merge fields at Api request info
merge_fields = {'applicantName_f2GtnW': 'Kevin', 'jobTitle_WCUZlG': 'Test'}
response = client.create_workflow_instance(workflow_id, participants, merge_fields)
```

[See the full list of available fields](https://docs.helloworks.com/reference#preview-workflow-instance)
## Cancel a workflow instance
Cancel a Workflow Instance that is currently active
```
workflow_instance_id = 'ID returned by the creation of the workflow'
response = client.cancel_workflow_instance(workflow_instance_id)
```
[More info](https://docs.helloworks.com/reference#get-workflow-instance)

## Get a workflow instance
Retrieve information on a single Workflow Instance
```
workflow_instance_id = 'ID returned by the creation of the workflow'
response = client.get_workflow_instance(workflow_instance_id)
```
[More info](https://docs.helloworks.com/reference#get-workflow-instance)

## Get Workflow Instance Document [After workflow is completed]
Method to get a given document of a workflow instance

```
document_id = 'You can get the documents IDs after the workflow is finished (Using get_workflow_instance method'
workflow_instance_id = 'ID returned by the creation of the workflow'
request = client.get_workflow_instance_document(workflow_instance_id, document_id, get_request=True) 
```
**Note**: By default this method will return the request, so you can do any process you might need with it, if you want the file to download in your directory use get_request=False instead.

[More info](https://docs.helloworks.com/reference#get-workflow-instance-document)

## Get Workflow Instance Audit Trail [After workflow is completed]
Method to get the audit trail of a workflow instance

```
workflow_instance_id = 'ID returned by the creation of the workflow'
request = client.get_workflow_instance_audit_trail(workflow_instance_id, get_request=True) 
```
**Note**: By default this method will return the request, so you can do any process you might need with it, if you want the file to download in your directory use get_request=False instead.

[More info](https://docs.helloworks.com/reference#get-workflow-instance-audit-trail)

## Get Workflow Instance Documents [After workflow is completed]
 Method to get the documents, in a zip file, of a workflow instance

```
workflow_instance_id = 'ID returned by the creation of the workflow'
request = client.get_workflow_instance_documents(workflow_instance_id, get_request=True) 
```
**Note**: By default this method will return the request, so you can do any process you might need with it, if you want the file to download in your directory use get_request=False instead.

[More info](https://docs.helloworks.com/reference#get-workflow-instance-documents)

## Get Workflow Instance Steps

Method to get the specified workflow instance, the step id, the role that will be completing the step,
the signer's full name, and the unauthenticated url that can be used to start entering information.

```
workflow_instance_id = 'ID returned by the creation of the workflow'
response = client.get_workflow_instance_steps(workflow_instance_id) 
```

[More info](https://docs.helloworks.com/reference#get-workflow-instance-steps)

## Get Document Link

For the specified workflow instance, get the step id, the role that will be completing the step, the signer's full name, and the unauthenticated url that can be used to start entering information.

```
workflow_instance_id = 'ID returned by the creation of the workflow'
response = client.get_document_link(workflow_instance_id) 
```

[More info](https://docs.helloworks.com/reference#get-document-link)

## Get Authenticated Link for Workflow Instance's Step [Premium]

Method to get the authenticated link for a workflow instance step, to use it you need to have delegated authentication enabled and have launched this specific workflow instance with delegate authentication activated

```
workflow_instance_id = 'ID returned by the creation of the workflow'
step_id = 'You can get the step using the get_workflow_instance_steps method'
response = client.get_authenticated_link_for_workflow_instance_step(workflow_instance_id, step_id ) 
```
Note: This link is active for only 30 seconds 

[More info](https://docs.helloworks.com/reference#get-authenticated-link-for-workflow-instances-step)

## Save Settings with Logo File

NotImplemented _JustYet_ Error

### TODOs
- Create custom exceptions to improve error handling
- Manage responses as objects similar to what HelloSign SDK does
- Improve file management
- Save settings with logo file
