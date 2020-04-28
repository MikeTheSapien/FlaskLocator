# @MikeTheSapien
# accountant@leboucher.ph
# this file would hold a class for reading a .ini file for constant values: email recipient, email sender, email account password

from configparser import ConfigParser

def initial_config(_section=''):
    _filename = 'constants.ini'
    _parser = ConfigParser()
    _parser.read(_filename)

    data = {}
    if _parser.has_section(_section):
        _params = _parser.items(_section)
        for param in _params:
            data[param[0]] = param[1]
    
    else:
        raise Exception('Section {0} not found in the {1} file'.format(_section, _filename))

    return data
