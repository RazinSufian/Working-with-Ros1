#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def control_callback(data):
    command = data.data  
    if command == 'w' or command== "W":
        rospy.loginfo("Rover moving forward")
    elif command == 'a'or command== "A":
        rospy.loginfo("Rover turning left")
    elif command == 's'or command== "S":
        rospy.loginfo("Rover moving backward")
    elif command == 'd'or command== "D":
        rospy.loginfo("Rover turning right")
    else:
        rospy.loginfo (" Wrong command")

if __name__ == '__main__':
    rospy.init_node('rover_node')
    rospy.Subscriber('/rover_control', String, control_callback)
    rospy.spin()
