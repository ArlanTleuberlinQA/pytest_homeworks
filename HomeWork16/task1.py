import json
import argparse
import xml.etree.ElementTree as ET


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def convert_to_xml(self):
        root = ET.Element("Human")
        for key, value in self.__dict__.items():
            ET.SubElement(root, key).text = str(value)
        return ET.tostring(root, encoding="unicode")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Конвертація екземпляра Human в JSON або XML")
    parser.add_argument("format", choices=["json", "xml"], help="Виберіть формат виводу (json/xml)")
    parser.add_argument("output_file", help="Ім'я файлу для збереження результату")

    args = parser.parse_args()

    human = Human("Ivan Petrovich", 35, "male", 1988)

    if args.format == "json":
        json_data = human.convert_to_json()
        with open(args.output_file, "w") as f:
            f.write(json_data)
    elif args.format == "xml":
        xml_data = human.convert_to_xml()
        with open(args.output_file, "w") as f:
            f.write(xml_data)
