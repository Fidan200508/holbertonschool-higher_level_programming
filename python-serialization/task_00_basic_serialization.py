#!/usr/bin/env python3
""" basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON file and deserialize
 the JSON file to recreate the Python Dictionary"""
import  json


def serialize_and_save_to_file(data, filename):
    def serialize(obj):
        if isinstance(obj, set):
            return {
                "__type__": "set",
                "elements": list(obj)
            }
        raise TypeError("Object type not serializable")

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, default=serialize)


def load_and_deserialize(filename):
    def deserialize(obj):
        if "__type__" in obj and obj["__type__"] == "set":
            return set(obj["elements"])
        return obj

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file, object_hook=deserialize)
