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

The ```requirement.txt``` file should be called and installed (once inside the main folder in the console path):

<img src="Images\pip_install_img.png" height=60% width=60%>

 
---

## Usage

Run the main ```app.py``` from the console:

<img src="Images\run_python_img.png" height=60% width=60%>

Then answer all the prompts you get and, when you are asked if you want to save your qualifying loans in a CSV file, confirm and check your options!

The App will show you a file with all the loans you qualify for:

<img src="Images\results_img.png" height=60% width=60%>

---

## Contributors

Feature developed by Lourdes Dominguez [(LinkedIn profile)](https://www.linkedin.com/in/lourdes-dominguez-bengoa-12333044/)

---

## License

Use only for academic purposes.
