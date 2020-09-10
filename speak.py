#! /usr/bin/env python
import roslib; roslib.load_manifest('sound_play')
import rospy
import actionlib
from sound_play.msg import SoundRequest, SoundRequestAction, SoundRequestGoal

class speak():
    def __init__(self, matter):
        self.client = actionlib.SimpleActionClient('sound_play', SoundRequestAction)
        self.client.wait_for_server()
        self.goal = SoundRequestGoal()

    def say(self):
        rospy.loginfo("Say")

        self.goal.sound_request.sound = SoundRequest.SAY
        self.goal.sound_request.command = SoundRequest.PLAY_ONCE
        self.goal.sound_request.arg = matter
        self.goal.sound_request.volume = 1.0

        self.client.send_goal(self.goal)
        self.client.wait_for_result()
        rospy.loginfo("End Say")

if __name__ == '__main__':
    rospy.init_node('speak')
    matter =  "pa-na-am"
    o=speak(matter)
    o.say()
