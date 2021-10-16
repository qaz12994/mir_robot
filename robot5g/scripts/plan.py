#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PointStamped
import tf
import random
import numpy as np

global x,y,z
x = 0.0
y = 0.0
z = 0.0

px, py = [], []

def callback(msg):
    point = PointStamped()
    point.header.stamp = rospy.Time.now()
    point.header.frame_id = "/map"
    point.point.x = msg.point.x      
    point.point.y = msg.point.y
    point.point.z = msg.point.z
    rospy.loginfo("coordinates:x=%f y=%f" %(point.point.x, point.point.y))
    px.append(point.point.x)
    py.append(point.point.y)
    print(px, py)

def listener():
    rospy.init_node('get_position', anonymous=True)
    rospy.point_pub = rospy.Subscriber('/position', PointStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()