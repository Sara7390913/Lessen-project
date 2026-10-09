import re


def name_validator(name):
    if not isinstance(name, str) or not re.match(r"^[a-zA-Z\s]{3,50}$", name):
        raise ValueError("Invalid name")
    return name


def teacher_validator(teacher):
    if not isinstance(teacher, str) or not 5 <= len(teacher) <= 50:
        raise ValueError("Invalid teacher")
    return teacher


def code_validator(code):
    if not isinstance(code, str) or not re.match(r"^[a-zA-Z]{3}-[a-zA-z]{4}$", code):
        raise ValueError("Invalid code")
    return code

def unit_validator(unit):
    if unit not in [1, 2, 3, 5]:
        raise ValueError("Invalid unit")
    return unit
