def parse_salary(value):
    try:
        return int(value)
    except ValueError:
        return None