#TODO
#Custom exceptions to throw when HW returns an error


def get_exception_message(response):
    response = response.json()
    if type(response) == str:
        exc_msg = response
    else:
        exc_msg = response.get('error', 'internal error')
    return exc_msg
