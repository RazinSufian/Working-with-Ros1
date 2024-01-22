
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    twist = Twist()
    if data.data == 'w':  # Forward
        twist.linear.x = 1.0
    elif data.data == 's':  # Backward
        twist.linear.x = -1.0
    elif data.data == 'a':  # Left
        twist.angular.z = 1.0
    elif data.data == 'd':  # Right
        twist.angular.z = -1.0

    pub.publish(twist)

if __name__ == '__main__':
    rospy.init_node('translator_node')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('/rover_control', String, callback)
    rospy.spin()