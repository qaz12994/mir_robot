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

def talker(point):
    rospy.loginfo(point)
    pub.publish(point)
    rate.sleep()


def callback(msg):
    point = PointStamped()
    point.header.stamp = rospy.Time.now()
    point.header.frame_id = "/map"
    point.point.x = msg.point.x      
    point.point.y = msg.point.y
    point.point.z = msg.point.z
    rospy.loginfo("coordinates:x=%f y=%f" %(point.point.x, point.point.y))
    talker(point)


def listener():
    rospy.point_pub = rospy.Subscriber('/clicked_point', PointStamped, callback)
    rospy.spin()


if __name__ == '__main__':
    rospy.init_node('goal_publisher', anonymous=True)
    pub = rospy.Publisher("/position", PointStamped, queue_size=10)
    rate = rospy.Rate(2) # hz
    listener()