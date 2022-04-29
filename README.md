# Grandma Data

## This GitHub repo aims to serve as a yaml file "database" to store all grandma related data on telescopes and instruments, so they can be reused later on to feed proper databases (ex: loading the data from yaml files in SkyPortal)

### This repo is a work in progress, and will be updated regularly.

#### This repo comes with a set of tests to check if the data is correct or not based on multiple criterias:
- Each telescope must have a `name`, a `nickname`, a `diameter` and an `id` that allows instruments to be linked to it.
- The `id` of a telescope must be unique.
- The `diameter` of a telescope must be a positive number.
- Each instrument must have a `name`, a `type` and a `telescope_id` that allows it to be linked to a telescope.
- The `type` of an instrument must be a valid type. It can be either `imager`, `spectrograph` or `imaging spectrograph`. This list can be change in the future.

#### To run the test suite, you need to create a virtualenv with `virtualenv venv`. Then, you can activate it with `source venv/bin/activate`.
#### Then, you can run `py.test --disable-warnings tests/test_yaml.py`.
