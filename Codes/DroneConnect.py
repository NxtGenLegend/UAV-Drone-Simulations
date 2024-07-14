from pymavlink import mavutil

port = "" #syntax = COMx; x = port number

connection = mavutil.mavlink_connection('port')

connection.arducopter_arm()
