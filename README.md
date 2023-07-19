# scr-data-analysis

> Collection of python scripts for analysis on the Smart Contracts in the Smart Contract Repository

## Getting Started

To get started you need to clone the repository, establish an environment file and create a virtual environment with the required pip packages.

```
$ git clone https://github.com/carl-egge/scr-data-analysis
$ cd scr-data-analysis
$ cp example.env .env
```

You maybe need to exchange the connection string in the .env file according to your needs.

### Virtual Environment

To run the scripts you need to create a virtual environment and install the necessary packages in it:

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

If you have trouble to install packages you might need to run pip upgrades first:

```
$ pip3 install --upgrade setuptools
$ pip3 install --upgrade pip
```
