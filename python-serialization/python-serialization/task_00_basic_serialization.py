#!/usr/bin/python3
"""Basic serialization module for JSON data."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON from a file and return a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
