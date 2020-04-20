import logging
import _io
logger = logging.getLogger(__name__)


def _file_downloader(file_name, file):
    with open(file_name, "wb") as f:
        try:
            for chunk in file.iter_content(chunk_size=8192): 
                if chunk:
                    f.write(chunk)
            else:
                return True
        except:
            logger.error('Could not write file')
        return False


def _clean_dict(dictionary):
    clean_dict = {**dictionary}
    for key, value in dictionary.items():
        if not value:
            del clean_dict[key]
    return clean_dict


def _file_extension(file, name):
    '''
    This method returns the extension of a file, or an exception if the object
    is not a file or if it has a wrong extension
    '''

    if type(file) not in [_io.BufferedReader, _io.BytesIO]:
        raise Exception("Wrong object type")

    extensions = ['png', 'jpeg','jpg', 'gif']
    extension = 'png'
    name = getattr(file, 'name', name)

    if not name:
        raise Exception("For this file object you need to include the logo_name property")


    extension = name.split('.')[-1]

    if extension not in extensions:
        raise Exception(f"Wrong file extension, must be one of {extensions}")
    return extension
