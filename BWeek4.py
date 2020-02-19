from medical import Patient
from sys import exit

"""
Author: Joseph Lawton-Curtis
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: February 13, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""



menu = """
1. Look up a patient by an ID number.
2. Add a new patient
3. Save patients
4. Load patients
5. Quit

Select by entering the corresponding number and hitting "Enter"
        """
patient_file_name = str(input("what is the files name? if no name specified the default will be 'default'"))
if patient_file_name == "": patient_file_name = "default"
print(patient_file_name)
try:
    if patient_file_name:
        Patient.load_patients(patient_file_name)
except FileNotFoundError:
    print("file not found, if this is the first time using this program do not worry")


def exit_program_or_save(exit_option):
    if patient_file_name:
        Patient.save_patients(patient_file_name)
    else:
        Patient.save_patients(input("What would you like to name the file?"))
    if exit_option:
        exit()
    pass


def search():
    pid = int(input("Patient ID"))
    print(Patient.get_patient(pid))


def add():
    name = input("input patient name")
    age = int(input("input patient age"))
    Patient(name, age)


def save_data():
    exit_program_or_save(False)


def load():
    Patient.load_patients(patient_file_name)


def exit_program():
    exit_program_or_save(True)


options = {1: search,
           2: add,
           3: save_data,
           4: load,
           5: exit_program
           }

x = int(input(menu))
while True:
    try:
        if x:
            options[x]()
    except Exception:
        print(Exception.__str__())
    x = int(input(menu))




