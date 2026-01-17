import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    root = ET.Element("data")  # Root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # Sadə serialization: hamısını string kimi saxlayırıq
        child.text = str(value)
        # Optional: type info əlavə edə bilərsən
        child.set("type", type(value).__name__)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file back to a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        text = child.text
        type_attr = child.get("type", "str")

        # Type conversion
        if type_attr == "int":
            value = int(text)
        elif type_attr == "float":
            value = float(text)
        elif type_attr == "bool":
            value = text.lower() == "true"
        else:
            value = text  # default: string

        result[child.tag] = value

    return result


# --- Example Usage ---
if __name__ == "__main__":
    data = {
        "name": "Alice",
        "age": 30,
        "height": 1.65,
        "is_student": False
    }

    serialize_to_xml(data, "data.xml")
    loaded_data = deserialize_from_xml("data.xml")
    print(loaded_data)
