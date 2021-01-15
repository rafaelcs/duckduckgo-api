# duckduckgo-api

### Prerequisites

1. [Python 3](https://www.python.org/downloads/)

## Quick start

### Install and create a virtual environment

Install [virtualenv](https://virtualenv.pypa.io/en/latest/index.html):

```sh
python3 -m pip install virtualenv
```

Create the virtual environment:

```sh
virtualenv -p python3.7 env
```

Activate the virtual environment:

```sh
. env/bin/activate
```

### Install the project dependencies:

```sh
pip install -r requirements.txt
```

### Run automated tests:

```sh
pytest -s tests
```