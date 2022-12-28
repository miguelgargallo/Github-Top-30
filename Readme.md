# GitHub Top 30

<img width="640" alt="2022-12-28-01-51-12-GitHub Top-30 by-miguelgargallo" src="https://user-images.githubusercontent.com/5947268/209740989-8a32dafa-0c92-4e07-b567-99832539a9ef.png">

- [This thumbnail was made by miguelgargallo's project: YouTube Thumbnail Maker](https://github.com/miguelgargallo/Youtube-Thumbnail-Maker)

## Index

Introduction

- [GitHub Top 30](#github-top-30)
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
- [Top 30 Most Starred Projects on GitHub](#top-30-most-starred-projects-on-github)

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

# Top 30 Most Starred Projects on GitHub

1. [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) - 358662 stars
2. [996.ICU](https://github.com/996icu/996.ICU) - 264668 stars
3. [free-programming-books](https://github.com/EbookFoundation/free-programming-books) - 259356 stars
4. [coding-interview-university](https://github.com/jwasham/coding-interview-university) - 241856 stars
5. [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) - 222602 stars
6. [public-apis](https://github.com/public-apis/public-apis) - 222065 stars
7. [system-design-primer](https://github.com/donnemartin/system-design-primer) - 206584 stars
8. [vue](https://github.com/vuejs/vue) - 201444 stars
9. [react](https://github.com/facebook/react) - 199667 stars
10. [tensorflow](https://github.com/tensorflow/tensorflow) - 169976 stars
11. [You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) - 162690 stars
12. [bootstrap](https://github.com/twbs/bootstrap) - 160992 stars
13. [CS-Notes](https://github.com/CyC2018/CS-Notes) - 160121 stars
14. [javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) - 157722 stars
15. [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) - 153656 stars
16. [awesome-python](https://github.com/vinta/awesome-python) - 150945 stars
17. [Python](https://github.com/TheAlgorithms/Python) - 150379 stars
18. [flutter](https://github.com/flutter/flutter) - 147808 stars
19. [linux](https://github.com/torvalds/linux) - 143595 stars
20. [gitignore](https://github.com/github/gitignore) - 142179 stars
21. [vscode](https://github.com/microsoft/vscode) - 140758 stars
22. [javascript](https://github.com/airbnb/javascript) - 129994 stars
23. [computer-science](https://github.com/ossu/computer-science) - 129831 stars
24. [Python-100-Days](https://github.com/jackfrued/Python-100-Days) - 129059 stars
25. [the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) - 123274 stars
26. [youtube-dl](https://github.com/ytdl-org/youtube-dl) - 116051 stars
27. [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - 113185 stars
28. [fucking-algorithm](https://github.com/labuladong/fucking-algorithm) - 112834 stars
29. [go](https://github.com/golang/go) - 107096 stars
30. [react-native](https://github.com/facebook/react-native) - 106680 stars


- [This thumbnail was made by miguelgargallo's project: YouTube Thumbnail Maker](https://github.com/miguelgargallo/Youtube-Thumbnail-Maker)

2022 © All rights reserved. Pylar AI creative ML License. Pencil Works LLC.
