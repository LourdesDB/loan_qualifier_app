# Project Title

This project adds a new feature to the loan analyzer App that prompts the user to save qualifying loans as a new CSV file.

The user inserts some personal financial data for the App to find a list of loans that qualify for them. Required user's inputs:

* Credit score
* Total monthly income
* Desired loan amount
* Home value

The App then provides a list of loans that may qualify for them, and provides the option to save that list in a CSV file.

---

## Technologies

The whole project is implemented in Python, and the necessary libraries are ready to import on the ```requirement.txt``` file. In this case:

* ```fire==0.3.1```
* ```questionary==1.5.2```
* ```pytest==5.4.2```

Also, the ```csv``` library and ```pathlib``` from the ```Path``` library.

The main ```app.py``` file, depends on the functions contained in all the .py files contained in the folders 'filters' and 'utils', so they should also be imported properly.

---

## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.

---

## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.

---

## Contributors

In this section, list all the people who contribute to this project. You might want recruiters or potential collaborators to reach you, so include your contact email and, optionally, your LinkedIn or Twitter profile.

---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.
