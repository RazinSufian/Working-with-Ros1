#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


# pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

def control_callback(data):
    command = data.data
    msg=Twist()
    if command == 'w' or command== "W":
        rospy.loginfo("Rover moving forward")
        msg.linear.x = 1.0
    elif command == 's'or command== "S":
        rospy.loginfo("Rover moving backward")
        msg.linear.x = -1.0
        
    elif command == 'a'or command== "A":
        rospy.loginfo("Rover turning left")
        msg.angular.z = 1.0

    elif command == 'd'or command== "D":
        rospy.loginfo("Rover turning right")
        msg.angular.z = -1.0
    elif command == 'x'or command== "X":
        rospy.loginfo("Rover Break")
        msg.linear.x = 0
        msg.angular.z = 0
    else:
        rospy.loginfo (" Wrong command")
    pub.publish(msg)



if __name__ == '__main__':
    rospy.init_node('Huskey_control')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('/rover_control', String, control_callback)
    rospy.spin()


#Husky lunch
    
# roslaunch husky_gazebo husky_playpen.launch
# roslaunch husky_control teleop_keyboard.launch