# imports
import pickle

# classes
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

class Patient:

    _next_id = 1
    _all_patients = {}

    def __init__(self, name, age):
        self.procedures = []
        self.patient_id = self._next_id
        Patient._next_id += 1
        self.patient_name = name
        self.patient_age = age
        Patient._all_patients[self.patient_id] = self

    def add_procedure(self, name):
        self.procedures.append(name)
        pass

    @classmethod
    def get_patient(cls, patient_id):
        return cls._all_patients[patient_id]

    @classmethod
    def delete_patient(cls, patient_id):
        if len(cls._all_patients) > 0:
            del cls._all_patients[patient_id]
        else:
            print("no patients")
        pass

    @classmethod
    def save_patients(cls, file_name = "Enter the name of the file here:"):
        pickle.dump(cls._all_patients, open(file_name, "wb"))

    @classmethod
    def load_patients(cls, file_name = "Enter the name of the file here:"):
        cls._all_patients = pickle.load(open(file_name, "rb"))


class Procedure:
    _next_pid = 1
    _all_Pids = {}

    def __init__(self, name, price):
        self.procedure_name = name
        self.procedure_price = price
        self.procedure_id = Procedure._next_pid
        Procedure._next_pid += 1
        Procedure._all_pids[self.procedure_id] = self
