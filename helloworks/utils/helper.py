
def _file_downloader(file_name, file):
    with open(file_name, "wb") as f:
        for chunk in file.iter_content(chunk_size=8192): 
            if chunk:
                f.write(chunk)
        else:
            return True

def _clean_dict(dictionary):
    clean_dict = {**dictionary}
    for key, value in dictionary.items():
        if not value:
            del clean_dict[key]
    return clean_dict
