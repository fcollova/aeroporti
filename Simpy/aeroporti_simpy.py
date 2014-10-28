#!/usr/bin/env python
# airport.py
# from  pyt079D.py (from sms079D.tex)
# 2004 December cleaned up and simplified
# $Revision: 1.1.1.1 $ $Date: 2005/01/15 15:16:51 $ $Author: kgmuller $

"""
  N2 planes arrive at an airport during the day. Of these
  N1  arrive in a bunch at the start of the day (time 0.0) and the
  remainder arrive at equal intervals of, int hr.  (Thus plane
  N1+1 arrives at time 0.0+int. Each plane lands on the single
  runway, blocking it for L hr, and stays at the airport for a
  fixed turnround time, T hr, and then leaves, using the same
  runway, taking the same time.
   
  - N1 = 4 = number of planes arriving in a bunch at the start of the day
  - N2 = 12 = The total number of planes landing in the day
  - int = 0.4 = equal arrival intervals for remaining planes
  - L = 0.1 hr = time runway is blocked with a plane on it
  - T = 0.65 hr = time plane stays at the airport

  The eventual objective of this simulation is to determine the degree of
  congestion by counting the total number in the airport at any time.
  The planes report the time and their identifier  on arrival
  before landing, on leaving (before using the runway) and on final
  departure (i.e. a trace).

  In this version the only ouput is a trace; no statistics are gathered.
  
"""

__version__ = '\nModel: airport.py'

from __future__ import generators
from SimPy.Simulation import *
from random import expovariate,uniform

T = 0.0
L = 0.1

class Generator(Process):
    """ Generates a series of N planes at int intervals."""

    def execute(self,N1,N2,int):
        for i in range(N1):  # initial batch of planes
            p = Plane('Plane'+str(i))
            activate(p,p.execute(),0.0)

        n=N2-N1
        for i in range(n):   # the remainder
            no = N1+i
            p = Plane('Plane'+str(no))
            activate(p,p.execute())
            yield hold,self,int       
        
    def trace(self,message):
        if TRACING: print "%7.4f %s %s "%\
                  (now() , "Generator", message)

class Plane(Process):
    """ a Plane landing at the airport
    """

    def execute(self):
        self.trace("arrived")
        yield request,self,runway
        self.trace("got runway arriving")
        yield hold,self,L
        yield release,self,runway
        self.trace("landed")

        yield hold,self,T

        yield request,self,runway
        self.trace("got runway leaving")
        yield hold,self,L
        yield release,self,runway

        self.trace("farewell!")
        
    def trace(self,message):
        if TRACING: print "%7.4f %s %s "%\
                  (now() , self.name, message)

run = 1

print __version__
TRACING = 1

N1 = 4
N2 = 12
int = 0.4
T = 0.6
initialize()
g = Generator('Source')
activate(g,g.execute(N1,N2,int),0.0)
runway = Resource(1) # 1 runway
simulate(until=20.0)
