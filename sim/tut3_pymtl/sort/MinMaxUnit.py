#=========================================================================
# MinMaxUnit
#=========================================================================
# This module takes two inputs, compares them, and outputs the larger
# via the "max" output port and the smaller via the "min" output port.

from pymtl import *

class MinMaxUnit( Model ):

  # Constructor

  def __init__( s, nbits=8 ):

    s.in0     = InPort  ( nbits )
    s.in1     = InPort  ( nbits )
    s.out_min = OutPort ( nbits )
    s.out_max = OutPort ( nbits )

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert
    # logic here to implement the min/max unit. You should also write a
    # unit test from scratch named MinMaxUnit_test.py.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    @s.combinational
    def block():
      if s.reset:
        s.out_min.value = 0
        s.out_max.value = 0
      else:
        if s.in0 < s.in1:
          s.out_min.value = s.in0
          s.out_max.value = s.in1
        else:
          s.out_min.value = s.in1
          s.out_max.value = s.in0

  def line_trace( s ):
    return "{} {} {} {}".format( s.in0, s.in1, s.out_min, s.out_max )
