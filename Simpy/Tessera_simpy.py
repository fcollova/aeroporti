import simpy

class Plane(object):
    
    def __init__(self, env, name, plane_type="Big"):
        self.env = env
        self.plane_type = type # tipo di aereo
        self.name = name
    
    def run_land(self, env, runway):
        
        print('%s request landing at %.2f.' % (self.name, env.now))

        with runway.request() as req:
            yield req
            yield env.timeout(10)
            print('%s landed at %.2f.' % (self.name, env.now))
        

env = simpy.Environment()
runway = simpy.Resource(env, 1)
myplane = Plane(env, "747", "Big")


for i in range(10):
    myplane=Plane(env, "747-"+ str(i), "Big")
    env.process(myplane.run_land(env, runway))

env.run()
    