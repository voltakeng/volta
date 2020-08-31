#!/usr/bin/env python 

import rospy, math 
from geometry_msgs.msg import Pose, Point, Quaternion 
from tf.transformations import quaternion_about_axis 
from utilities import set_model_state, get_model_state, / 
                spawn_coke_can, spawn_table, /
                pause_physics, unpause_physics 

spawn_coke_can('coke_can', Pose(position=Point(0,1,0))) 

model_state = get_model_state('coke_can') 
model_state.pose.position 

new_pose = Pose(position=Point(1,0,0))
set_model_state('coke_can', new_pose)

#pause_physics() 
