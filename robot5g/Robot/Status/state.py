from Robot.Status import PutStatus, PUT

Starting = 1
Shutting_down = 2
Ready = 3
Pause = 4
Executing = 5
Aborted = 6
Completed = 7
Docked = 8
Docking = 9
Emergency_stop = 10
Manual_control = 11
Error = 12


def setRobotState(ID):
    body = PutStatus().state_id(ID)
    return PUT(body)


def setReady():
    setRobotState(Ready)


def setPause():
    setRobotState(Pause)


def joystick_control():
    setRobotState(Manual_control)


