# GitHub Top 30 (2022)

<img width="640" alt="2022-12-28-01-51-12-GitHub Top-30 by-miguelgargallo" src="https://user-images.githubusercontent.com/5947268/209740989-8a32dafa-0c92-4e07-b567-99832539a9ef.png">

- [This thumbnail was made by miguelgargallo's project: YouTube Thumbnail Maker](https://github.com/miguelgargallo/Youtube-Thumbnail-Maker)

## Index

Introduction

- [GitHub Top 30 (2022)](#github-top-30-2022)
  - [Index](#index)
- [GitHub Top 30 Project Finder](#github-top-30-project-finder)
  - [Overview of the project](#overview-of-the-project)
  - [Purpose of the tool](#purpose-of-the-tool)
  - [Description of how the tool finds the top 30 most starred projects](#description-of-how-the-tool-finds-the-top-30-most-starred-projects)
  - [Explanation of how the results are written to a file](#explanation-of-how-the-results-are-written-to-a-file)
  - [How to Use the Tool](#how-to-use-the-tool)
    - [Make sure you have Python and pip installed](#make-sure-you-have-python-and-pip-installed)
    - [Clone or download the project to your local machine](#clone-or-download-the-project-to-your-local-machine)
    - [Run the play.sh script to install dependencies and run the tool](#run-the-playsh-script-to-install-dependencies-and-run-the-tool)
  - [Resources](#resources)
    - [GitHub API documentation](#github-api-documentation)
    - [Python documentation](#python-documentation)
    - [pip documentation](#pip-documentation)
  - [Description of the programming language and modules used in the tool](#description-of-the-programming-language-and-modules-used-in-the-tool)
  - [Explanation of the file format used to write the results](#explanation-of-the-file-format-used-to-write-the-results)

# GitHub Top 30 Project Finder

## Overview of the project

Welcome to the GitHub Top 30 Project Finder! This project provides a tool for finding the top 30 most starred projects on GitHub.

## Purpose of the tool

The purpose of the tool is to provide developers with a way to easily find the most popular projects on GitHub. It uses the GitHub API to send a request for the top 30 most starred projects, and then parses the JSON data from the response to create a list of the top 30 projects. The results are written to a file called top30.md.

## Description of how the tool finds the top 30 most starred projects

The tool uses the requests module to send a GET request to the GitHub API. The API endpoint used in the request is:

```
https://api.github.com/search/repositories?q=stars:%3E1&sort=stars&order=desc
```

The requests.get function sends the request and stores the response in a variable. The response.json function is used to parse the JSON data from the response.

## Explanation of how the results are written to a file

The results are written to a file called top30.md in Markdown format using the f string format. The file is opened for writing using the with open('top30.md', 'w') as f: syntax. The f string format is used to write the results to the file. The results are written in the following format:

## How to Use the Tool

### Make sure you have Python and pip installed

To use the tool, you must have Python and pip installed on your local machine. You can check if you have Python installed by running the command:

```
python --version
```

If you do not have Python installed, you can download it from the [Python website](https://www.python.org/downloads/).

### Clone or download the project to your local machine

To use the tool, you must first clone or download the project to your local machine. You can do this by clicking the green "Code" button at the top right of the page and then clicking "Download ZIP". You can also clone the project using the command:

```
git clone https://github.com/miguelgargallo/github-top-30
```

### Run the play.sh script to install dependencies and run the tool

To run the tool, you must first install the dependencies. You can do this by running the play.sh script. You can do this by running the command:

```bash
./play.sh
```

## Resources

### GitHub API documentation

You can find the GitHub API documentation [here](https://docs.github.com/en/rest).

### Python documentation

You can find the Python documentation [here](https://docs.python.org/3/).

### pip documentation

You can find the pip documentation [here](https://pip.pypa.io/en/stable/).

## Description of the programming language and modules used in the tool

The tool is written in Python. The requests module is used to send the GET request to the GitHub API. The json module is used to parse the JSON data from the response.

## Explanation of the file format used to write the results

The results are written to a file called top30.md in Markdown format using the f string format. The file is opened for writing using the with open('top30.md', 'w') as f: syntax. The f string format is used to write the results to the file. The results are written in the following format:

<img width="640" alt="2022-12-28-01-50-52-GitHub Top-30 by-miguelgargallo" src="https://user-images.githubusercontent.com/5947268/209740995-9211597f-f74b-4591-ac30-e6eea32be431.png">

- [This thumbnail was made by miguelgargallo's project: YouTube Thumbnail Maker](https://github.com/miguelgargallo/Youtube-Thumbnail-Maker)

2022 (c) All Rights Reserved. Pylar AI creative ML License.
