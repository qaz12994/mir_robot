def move_to_position(X, Y, orientation):
    return [
        {
            "id": "x",
            "input_name": None,
            "value": X
        },
        {
            "id": "y",
            "input_name": None,
            "value": Y
        },
        {
            "id": "orientation",
            "input_name": None,
            "value": orientation
        },
        {
            "id": "retries",
            "input_name": None,
            "value": 10
        },
        {
            "id": "distance_threshold",
            "input_name": None,
            "value": 0.1
        }
    ]
