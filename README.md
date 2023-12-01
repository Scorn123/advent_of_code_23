# Advent of code 2023

## Purpose

My personal solution to the [Advent of Code 2023](https://adventofcode.com/).  

## Deployments

Copy the input to the `input` folder and name the file `input_day_<DAY>`.

### Set Up Python Venv

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run script

```bash
python3 scrips/day_<DAY>.py
```

# Folder Structure
```
advent_of_code_23/
    ├── input/                            Folder with the inputs for the AOC
        └── input_day_<DAY>               Input for the specific day
    ├── scripts/                          For the daily scripts
    ├── src/                              Source for the Python Classes used in the Scripts
    ├── tests/                            Pytest Unit Tests
        └── testdata/                     Files for executing and checking the unit tests
    └── requirements.txt                  Python requirement list.
```
