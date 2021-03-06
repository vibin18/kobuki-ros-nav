#!/usr/bin/env python2

import argparse
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

parser = argparse.ArgumentParser(prog='NavGoalPublish.py', usage='%(prog)s [xGoal yGoal]')
parser.add_argument( 'xGoal', type=float, help='Goal x in float')
parser.add_argument( 'yGoal', type=float, help='Goal y in float')
args = parser.parse_args()

#this method will make the robot move to the goal location
def move_to_goal(xGoal,yGoal):

        #define a client for to send goal requests to the move_base server through a SimpleActionClient
        ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

        #wait for the action server to come up
        while(not ac.wait_for_server(rospy.Duration.from_sec(120))):
                rospy.loginfo("Waiting for the move_base action server to come up")

        goal = MoveBaseGoal()


        #set up the frame parameters
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        # moving towards the goal*/

        goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0

        rospy.loginfo("Sending goal location ...")
        ac.send_goal(goal)

        ac.wait_for_result(rospy.Duration(60))

        if(ac.get_state() ==  ac.GoalStatus.SUCCEEDED):
                rospy.loginfo("You have reached the destination")
                return 'success'

        else:
                rospy.loginfo("The robot failed to reach the destination")
                return 'failed'
        
        

if __name__ == '__main__':
    rospy.init_node('patrol')
    move_to_goal(args.xGoal,args.yGoal)
    rospy.spin()