import pickle
import os

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nis_student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self,f)
        except Exception as ex:
            print(f"Error during serialization: {ex}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as ex:
            print(f"Error during deserialization: {ex}")
            return None
