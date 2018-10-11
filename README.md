## Nava Coding Challenge
This application processes a pair of files
that define the contents of the file and also the schema of
that file. It then POSTs the record to an API endpoint.


### Running the Code
1. Ensure that you have `python3` installed by typing in `python3 --version`. If `python3` is not found, follow along
with this guide: https://docs.python-guide.org/starting/install3/osx/
1. Run `pip3 install -r requirements.txt`
1. Run `python3 main.py [name of the file without extension]`.
For example, `python3 main.py booleanmeasures`

### Running the Tests
1. Run `python3 -m unittest discover`

### Assumptions
1. Handling API response errors is out of scope
1. Handling files that don't exist is out of scope