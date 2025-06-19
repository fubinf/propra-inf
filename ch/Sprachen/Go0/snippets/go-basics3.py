
fake_csv = """name;grades
Alice;3.3,2.7,4.0,3.7
Bob;1.7,2.3,1.7,3.3
Charlie;4.0,3.7,3.7,4.0,1.7,2.3
David;2.3,5.7,2.7,3.0
Emma;1.7,1.3,2.3,2.0,2.7
Frank;2.3,2.7,1.3,2.3;14.11.2024
Grace;1.3,1.0,1.3,1.3
Henry;1.7,2.7,0.7,1.7,2.3
Isabel;2.7,2.0,3.7,2.0,2.7,3.0
Jack;4.0,4.0,3.3,4.0,3.7"""


def validate_grades(name: str, grades: list[float]):
    for grade in grades:
        if grade > 4.0 or grade < 1.0:
            raise RuntimeError(f"Invalid grades for {name}")


def validate_line(line: list[str], expected_length: int):
    if len(line) != expected_length:
        raise RuntimeError(f"Invalid line: {line}, {expected_length}")


def print_grade(name: str, grade: float):
    if grade <= 1.3:
        print(f"{name}: sehr gut")
    elif grade <= 2.3:
        print(f"{name}: gut")
    elif grade <= 3.3:
        print(f"{name}: befriedigend")
    else:
        print(f"{name}: ausreichend")


def validator():
    rows = fake_csv.split("\n")
    num_columns = len(rows[0].split(";"))
    values = {}

    for row in rows[1:]:
        stored_values = row.split(";")

        try:
            validate_line(stored_values, num_columns)
        except Exception as e:
            print(e)
            continue

        name, grades = stored_values[0], stored_values[1]
        stored_grades = grades.split(",")

        try:
            stored_converted_grades = [float(i) for i in stored_grades]
        except Exception as e:
            print(e)
            continue

        try:
            validate_grades(name, stored_converted_grades)
        except Exception as e:
            print(e)
            continue

        avg = round(sum(stored_converted_grades) / len(stored_converted_grades), 1)

        values[name] = avg

    for name, grade in values.items():
        print_grade(name, grade)


if __name__ == "__main__":
    validator()
