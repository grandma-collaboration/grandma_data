import yaml
import os
import sys


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
            conf = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return conf


telescopes = yaml_to_dict("./telescopes.yaml")

instruments = yaml_to_dict("./instruments.yaml")


def test_correct_yaml_format():
    """
    Test that the yaml files are correctly formatted.
    """
    assert isinstance(telescopes, list)
    assert isinstance(instruments, list)


def test_telescope_has_required_fields():
    # a telescope must has a name, nickname and diameter, and an id as well
    for telescope in telescopes:
        # verify that the fields exist
        assert "name" in telescope
        assert "nickname" in telescope
        assert "diameter" in telescope
        assert "=id" in telescope
        # verify that the field are of the correct type
        assert isinstance(telescope["name"], str)
        assert isinstance(telescope["nickname"], str)
        assert isinstance(telescope["diameter"], float)
        assert isinstance(telescope["=id"], str)
        # verify that the fields are not empty
        assert telescope["name"] != ""
        assert telescope["nickname"] != ""
        assert telescope["diameter"] != 0.0
        assert telescope["=id"] != ""


def test_unique_telescope_ids():
    """
    Test that the telescope ids are unique.
    """
    ids = [telescope["=id"] for telescope in telescopes]
    assert len(ids) == len(set(ids))


def test_instrument_has_required_fields():
    # an instrument must has a name, a type and a telescope id
    # type can be : imager, spectrograph, or imaging spectrograph
    types = ["imager", "spectrograph", "imaging spectrograph"]
    for instrument in instruments:
        # verify that the fields exist
        assert "name" in instrument
        assert "type" in instrument
        assert "telescope_id" in instrument
        # verify that the field are of the correct type
        assert isinstance(instrument["name"], str)
        assert isinstance(instrument["type"], str)
        assert isinstance(instrument["telescope_id"], str)
        # verify that the fields are not empty
        assert instrument["name"] != ""
        assert instrument["type"] in types
        assert instrument["telescope_id"] != ""


def test_correct_telescope_ids_in_instruments():
    """
    Test that the telescope ids in the instruments.yaml file match the ids in the telescopes.yaml file.
    """
    for instrument in instruments:
        # check if the telescope id of that instrument is in the telescopes.yaml file
        if any(
            telescope["=id"] == instrument["telescope_id"][1:]
            for telescope in telescopes
        ):
            assert True
        else:
            print(
                "Instrument {} has an invalid telescope id.".format(instrument["name"])
            )
            assert False

        # check if only one telescope has the id
        if (
            len(
                list(
                    filter(
                        lambda x: x["=id"] == instrument["telescope_id"][1:], telescopes
                    )
                )
            )
            == 1
        ):
            assert True
        else:
            print(
                "More than one telescope has the id {}.".format(
                    instrument["telescope_id"][:1]
                )
            )
            assert False
