# Term_Project

## Note for team mates 

- I took this template from this [article](https://khuyentran1401.github.io/reproducible-data-science/structure_project/introduction.html). This is only a template that I've skimmed over and has capabilities that we don't need, such as data versioning.
- I'll provide instructions on what to do to get your environment set up but I haven't tested it outside of my machine, so please complain on discord with a screenshot of the error

### On your end, do the following
- Have a package manager beforehand
    - MacOS: [brew](https://brew.sh/)
    - Windows: [scoop](https://scoop.sh/)
- Install [pipx](https://pipx.pypa.io/stable/installation/) via your respective package manager
    - MacOS: `brew install pipx`
    - Windows: `scoop install pipx`
- Install [poetry](https://python-poetry.org/docs/#installation) via pipx

#### Optional 
I use [asdf](https://asdf-vm.com/) to manage multiple versions of Python. I'm currently at 3.12.2

Install asdf if you want to

## Description

A REST API that returns the number of students and staff parked at Glen parking garage 

The value is obtained by an automatic license plate reader that compares the values being read with a database of license plates that are paired with either student or staff

License plates that are either incorrectly read or is neither a student or staff will count as an unknown
## Tools used in this project
* [hydra](https://hydra.cc/): Manage configuration files - [article](https://mathdatasimplified.com/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
* [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting

* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)


## Project Structure

```bash
.
├── config                      
│   ├── main.yaml                   # Main configuration file
│   ├── model                       # Configurations for training model
│   │   ├── model1.yaml             # First variation of parameters to train model
│   │   └── model2.yaml             # Second variation of parameters to train model
│   └── process                     # Configurations for processing data
│       ├── process1.yaml           # First variation of parameters to process data
│       └── process2.yaml           # Second variation of parameters to process data
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   └── raw                         # raw data
├── docs                            # documentation for your project
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── process.py                  # process data before training model
│   └── train_model.py              # train model
└── tests                           # store tests
    ├── __init__.py                 # make tests a Python module 
    ├── test_process.py             # test functions for process.py
    └── test_train_model.py         # test functions for train_model.py
```

## Set up the environment


1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Activate the virtual environment:
```bash
poetry shell
```
3. Install dependencies:
- To install all dependencies from pyproject.toml, run:
```bash
poetry install
```
- To install only production dependencies, run:
```bash
poetry install --only main
```
- To install a new package, run:
```bash
poetry add <package-name>
```


## View and alter configurations
To view the configurations associated with a Pythons script, run the following command:
```bash
python src/process.py --help
```
Output:
```yaml
process is powered by Hydra.

== Configuration groups ==
Compose your configuration from those groups (group=option)

model: model1, model2
process: process1, process2


== Config ==
Override anything in the config (foo.bar=value)

process:
  use_columns:
  - col1
  - col2
model:
  name: model1
data:
  raw: data/raw/sample.csv
  processed: data/processed/processed.csv
  final: data/final/final.csv
```

To alter the configurations associated with a Python script from the command line, run the following:
```bash
python src/process.py data.raw=sample2.csv
```

## Auto-generate API documentation

To auto-generate API document for your project, run:

```bash
make docs
```
