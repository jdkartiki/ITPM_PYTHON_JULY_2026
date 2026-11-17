def validate_age(age):
    if age<0 or age>120:
        raise ValueError("Invalid Age ")


def validate_date(date_str):
    from datetime import datetime
    try:
        datetime.strptime(date_str,"%Y-%m-%d")
    except ValueError:
        ("Date Must be in YYYY-MM-DD Format ")