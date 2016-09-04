from Simulation import simulation

class Algorithm(object):
    """Third phase"""
    def __init__(self):
        return
    def brute_force(self, max_x,min_x, max_y, min_y):
        sim=simulation.Simulation()
        x_result=None
        y_result=None
        max_result=float("-inf")
        for x in (range(min_x,max_x)):
            for y in (range(min_y,max_y)):
                result=sim.compute(x,y)
                if result>max_result:
                    max_result=result
                    x_result=x
                    y_result=y
        return x_result , y_result
final_result=Algorithm()
print (final_result.brute_force(3,0,3,0))




