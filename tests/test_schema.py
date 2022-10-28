import jsonschema
import yaml
import json


def yaml_to_dict(file_path):
    """
    Open a config file and return a dictionary containing the configuration.
    Arguments
    ----------
        file_path : str
            path to the yaml file
    Returns
    ----------
        config : dict
            dictionary containing the date from the yaml file
    """

    with open(file_path, "r") as stream:
        try:
            file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return file


def json_to_dict(file_path):
    """
    Open a json file and return a dictionary containing the its data.
    Arguments
    ----------
        file_path : str
            path to the json file
    Returns
    ----------
        config : dict
            dictionary containing the date from the json file
    """

    with open(file_path, "r") as stream:
        try:
            file = json.load(stream)
        except json.JSONDecodeError as exc:
            print(exc)
    return file


telescope_schema = json_to_dict("./schemas/telescope_schema.json")
instrument_schema = json_to_dict("./schemas/instrument_schema.json")

telescopes = yaml_to_dict("./telescopes.yaml")
instruments = yaml_to_dict("./instruments.yaml")


def test_correct_yaml_format():
    """
    Test that the yaml files are correctly formatted.
    """
    assert isinstance(telescopes, list)
    assert isinstance(instruments, list)


def test_validate_telescope_schema():
    """
    Test that the yaml files are correctly formatted.
    """
    for telescope in telescopes:
        for k,v in telescope.items():
            if v == None:
                telescope[k] = ""
        jsonschema.validate(telescope, telescope_schema)


def test_validate_instrument_schema():
    """
    Test that the yaml files are correctly formatted.
    """
    for instrument in instruments:
        for k,v in instrument.items():
            if v == None:
                instrument[k] = ""
        jsonschema.validate(instrument, instrument_schema)
