#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist



def callback(data):

    robot = rospy.Publisher('/tb2_0/cmd_vel',Twist,queue_size=10)

    poruka = Twist()

    poruka = data

    robot.publish(poruka)

    print('poslao')



def listener():



    rospy.init_node('roscopy', anonymous=True)



    rospy.Subscriber('/tb3_0/cmd_vel', Twist, callback)



    rospy.spin()



if __name__ == '__main__':
   try:
	listener()

   except rospy.ROSInterruptException: pass
