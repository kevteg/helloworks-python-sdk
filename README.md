[![Maintainability](https://api.codeclimate.com/v1/badges/d0fdc2372d8384e6db9b/maintainability)](https://codeclimate.com/github/kevteg/helloworks-python-sdk/maintainability) [![CircleCI](https://circleci.com/gh/kevteg/helloworks-python-sdk.svg?style=svg)](https://circleci.com/gh/kevteg/helloworks-python-sdk)

# helloworks-python-sdk 🐍

Easily create and manage HelloWorks workflow instances. 🚀

## Installation

    pip install helloworks-python-sdk

## Usage

Go to your HelloWorks account and get your public key ID and your private key value

Remember to record the private key immediately and store it in a safe place. The private key value cannot be retrieved later, however keys can be generated at any time.

[See their docs](https://docs.helloworks.com/v3.3/reference#getting-started)

from helloworks import HwClient
client = HwClient(api_key_id, api_key_value)

### TODOs
- Create custom exceptions to improve error handling
- Manage responses as objects similar to what HelloSign SDK does
