#!/usr/bin/python3
"""Serialize and deserialize a dictionary using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for element in root:
        data[element.tag] = element.text

    return data
