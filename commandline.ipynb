from math import sin, cos, radians
from matplotlib import pyplot as plt
class Cannon:
    def __init__(self, x0, y0, v, angle):
    # current x and y coordinates of the missile
        self.x    = x0
        self.y    = y0
    # current value of velocity components
        self.vx  = v*cos(radians(angle))
        self.vy  = v*sin(radians(angle))
    # acceleration by x and y axes
        self.ax   = 0
        self.ay   = -9.8
    # start time
        self.time = 0
    # these list will contain discrete set of missile coordinates
        self.xarr = [self.x]
        self.yarr = [self.y]
    def updateVx(self, dt):
        self.vx = self.vx + self.ax*dt
        return self.vx
    def updateVy(self, dt):
        self.vy = self.vy + self.ay*dt
        return self.vy
    def updateX(self, dt):
        self.x = self.x + 0.5*(self.vx + self.updateVx(dt))*dt
        return self.x
    def updateY(self, dt):
        self.y = self.y + 0.5*(self.vy + self.updateVy(dt))*dt
        return self.y
    def step(self, dt):
        self.xarr.append(self.updateX(dt))
        self.yarr.append(self.updateY(dt))
        self.time = self.time + dt
def makeShoot(x0, y0, velocity, angle):
    """
    Returns a tuple with sequential pairs of x and y coordinates
    """
    cannon = Cannon(x0, y0, velocity, angle)
    dt = 0.05 # time step
    t = 0 # initial time
    cannon.step(dt)
    ###### THE  INTEGRATION ######
    while cannon.y >= 0:
        cannon.step(dt)
        t = t + dt
    ##############################
    return (cannon.xarr, cannon.yarr)
def main():
    x0 = 0
    y0 = 0
    velocity = float(input("Enter the initial velocity:  "))
    angle = float(input("Enter the initial angle in degree's:  "))
    xt, yt = makeShoot(x0, y0, velocity, angle)
    plt.plot(xt, yt, 'bo-', [0, 12], [0, 0], 'k-')
    plt.legend(['lintasan euy'])
    plt.xlabel('X coordinate (m)')
    plt.ylabel('Y coordinate (m)')
    plt.show()
if __name__ == '__main__':
    main()
