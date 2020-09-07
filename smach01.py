#!/usr/bin/env python2

import rospy
import actionlib
import smach
import smach_ros
from smach import State,StateMachine
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,currentdir) 
import NavGoalPublish

smach.State.__init__(NavGoalPublish, outcomes=['success', 'failed'])

stateMachine1 = smach.StateMachine(outcomes=['FAILED'])

with stateMachine1:
    StateMachine.add('KITCHEN',
        NavGoalPublish(3.8  0.55)),
        transitions={'success': 'ENTRANCE', 'failed' : 'FAILED' })

    StateMachine.add('ENTRANCE',
        NavGoalPublish(-0.577 , 0.151),
        transitions={'success': 'KITCHEN', 'failed' : 'FAILED' })

sis = smach_ros.IntrospectionServer('smach_server', stateMachine1 , '/SM_ROOT')
sis.start()
patrol.execute()
sis.stop()