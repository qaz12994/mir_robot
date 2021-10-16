from Robot.Factory.BodyBuilder import ModifyClipboard, TabPrinter

api = {
    'ObjectName': 'GetStatus',
    'keys': [
        'battery_percentage',
        'battery_time_remaining',
        'distance_to_next_target',
        'errors',
        'footprint',
        'hook_status',
        'map_id',
        'mission_queue_id',
        'mission_queue_url',
        'mission_text',
        'mode_id',
        'mode_text',
        'moved',
        'position',
        'robot_model',
        'robot_name',
        'serial_number',
        'session_id',
        'state_id',
        'state_text',
        'unloaded_map_changes',
        'uptime',
        'user_prompt',
        'velocity'
    ]
}


if __name__ == '__main__':
    keys = api['keys']
    code = list()
    code.append(TabPrinter(0, f"class {api['ObjectName']}:"))

    # __init__
    code.append(TabPrinter(1, "def __init__(self, request):"))
    code.append(TabPrinter(2, "self.status_code = request.status_code"))
    code.append(TabPrinter(2, "self.json = request.json()\n\n"))

    # Success()
    code.append(TabPrinter(1, "def Success(self):"))
    code.append(TabPrinter(2, "return self.status_code == HTTP_OK or self.status_code == HTTP_Created\n\n"))

    # Parser()
    for key in keys:
        code.append(TabPrinter(1, f"def {key}(self):"))
        code.append(TabPrinter(2, f"return self.json['{key}']\n\n"))


    ModifyClipboard('\n'.join(code))
