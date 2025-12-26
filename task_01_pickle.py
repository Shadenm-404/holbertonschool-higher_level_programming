#!/usr/bin/python3
"""Module for serializing and deserializing CustomObject using pickle."""

import pickle


class CustomObject:
    """Custom object that can be serialized and deserialized."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (OSError, pickle.PickleError):
            return None
        return None
