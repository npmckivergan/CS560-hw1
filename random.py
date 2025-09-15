import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('random')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0
        self.spin = random.uniform(-2.0, 2.0)

    def create_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        return msg

    def get_twist_msg(self):

        # Turn to a random direction and draw an arrow

        # Orient in a random direction
        if self.time < 4:
            msg = self.create_twist(0.0, self.spin)

        # Straight
        elif self.time >= 5 and self.time < 10:
            msg = self.create_twist(1.0, 0.0)

        # 90 degrees right
        elif self.time >= 11 and self.time < 13:
            msg = self.create_twist(0.0, -1.6)

        # Straight
        elif self.time >= 14 and self.time < 16:
            msg = self.create_twist(1.0, 0.0)

        # 135 degrees left
        elif self.time >= 17 and self.time < 20:
            msg = self.create_twist(0.0, 1.6)

        # Straight
        elif self.time >= 21 and self.time < 25:
            msg = self.create_twist(1.0, 0.0)

        # 90 degrees left
        elif self.time >= 26 and self.time < 28:
            msg = self.create_twist(0.0, 1.6)

        # Straight
        elif self.time >= 29 and self.time < 33:
            msg = self.create_twist(1.0, 0.0)

        # 135 degrees left
        elif self.time >= 34 and self.time < 37:
            msg = self.create_twist(0.0, 1.6)

        # Straight
        elif self.time >= 38 and self.time < 40:
            msg = self.create_twist(1.0, 0.0)

        # 90 degrees right
        elif self.time >= 41 and self.time < 43:
            msg = self.create_twist(0.0, -1.6)

        # Straight
        elif self.time >= 44 and self.time < 49:
            msg = self.create_twist(1.0, 0.0)

        # 90 degrees left
        elif self.time >= 50 and self.time < 52:
            msg = self.create_twist(0.0, 1.6)

        # Straight
        elif self.time >= 53 and self.time < 54.5:
            msg = self.create_twist(1.0, 0.0)

        # Stop
        else:
            msg = self.create_twist(0.0, 0.0)
        return msg
    
    def timer_callback(self):
        msg = self.get_twist_msg()       
        self.publisher.publish(msg)
        self.time += 1
        print("time: {}".format(self.time))

def main(args=None):
    rclpy.init(args=args)

    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
