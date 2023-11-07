import re

my_string = "Place of delivery of goods or place of performance of work or provision of services: 82172, Ukraine, Lviv Region, Stebnyk, str. Doroshenko, 1 Deadline for delivery of goods, performance of works or provision of services: 31.12.2023"

if __name__ == '__main__':
    match = re.search(r': (\d+), (.*?), (.*?), (.*?), (.*?), (.*?): (\d{2}.\d{2}.\d{4})', my_string)
    data = {
            'country': match.group(2),
            'region': match.group(3),
            'city': match.group(4),
            'postal': match.group(1),
            'address': match.group(5),
            'deadline': match.group(7),
        }
    print(data)