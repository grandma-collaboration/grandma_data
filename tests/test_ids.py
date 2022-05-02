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
            file = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return file


telescopes = yaml_to_dict("./telescopes.yaml")
instruments = yaml_to_dict("./instruments.yaml")


def test_unique_telescope_ids():
    """
    Test that the telescope ids are unique.
    """
    ids = [telescope["=id"] for telescope in telescopes]
    assert len(ids) == len(set(ids))


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
