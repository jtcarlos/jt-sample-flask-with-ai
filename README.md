# Sample Python Flask with AI

This repository serves a simple project code I submitted for my graded final project for the [Coursera](https://coursera.org/) course [Developing AI Applications with Python and Flask](https://www.coursera.org/learn/python-project-for-ai-application-development/).

This project demonstrates the usage of IBM's Watson NLP, and is a single page web app that allows the user to input a text / phrase and detects the inputted text's emotions.

**Note:** The API URL only works on IBM's laborator so serving it the `python server.py` command and trying it will not work. For results, see screenshots provided below.

## Running The Server

To run and host the sever, navigate to the root folder and run the following command

```
> pip install flask        # optional, assuming flask package is not installed
> pip install requests     # optional, assuming requests package is not installed

> python server.py
```

### Emotions From a Valid Text

The image below shows the emotion rating as well as the dominant emotion.
![Image showing the interface of the web app](https://drive.usercontent.google.com/download?id=13NQhJdblzzhzoHVDArPYltQjLC_FVuDV)

### Emotions From an Invalid Text

The image below shows the emotion rating from the invalid text
![Image showing the interface of the web app](https://drive.usercontent.google.com/download?id=1i55G8QZsdScsb9_KqnQZGNeAignKTAyS)

### Server.py Linting Rate

The image below shows the `PyLint`'s code rating
![Image showing the PyLint's rating](https://drive.usercontent.google.com/download?id=1HjIr8P3XHvAsRExqDY3zWB1WFBtFVSxp)

## Course Completion Badge and Certificate

- [Credly Badge](https://www.credly.com/badges/e1bdfa91-08ea-4a8d-80d7-56522870df0b/public_url)
- [Coursera Certificate](https://coursera.org/share/967592f61680365c08bd5d594e90c017)
