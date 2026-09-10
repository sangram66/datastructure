def explode(data, column):
    """
    Custom implementation of Spark's explode function.

    Args:
        data (list of dict): Input data, a list of dictionaries.
        column (str): The column name to explode.

    Returns:
        list of dict: Exploded data.
    """
    exploded_data = []

    for row in data:
        if column in row and isinstance(row[column], list):
            for value in row[column]:
                new_row = row.copy()
                new_row[column] = value
                exploded_data.append(new_row)
        else:
            exploded_data.append(row)

    return exploded_data

# Examples for can_make_string


# Examples for explode
data = [
    {"id": 1, "values": ["a", "b", "c"]},
    {"id": 2, "values": ["x", "y"]},
    {"id": 3, "values": []},
    {"id": 4, "values": "z"}  # Not a list
]

print(explode(data, "values"))