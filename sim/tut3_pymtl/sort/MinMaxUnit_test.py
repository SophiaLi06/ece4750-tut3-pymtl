from pymtl import *
from MinMaxUnit import MinMaxUnit

def test_basic( dump_vcd ):
  model = MinMaxUnit()
  model.vcd_file = dump_vcd
  model.elaborate()

  sim = SimulationTool(model)
  sim.reset()
  print ""

  def t( in0, in1, min_out, max_out ):
    model.in0.value = in0
    model.in1.value = in1

    sim.eval_combinational()
    sim.print_line_trace()

    if ( min_out != '?' ) and ( max_out != '?' ):
      assert model.out_min == min_out
      assert model.out_max == max_out

    sim.cycle()

  t( 0x00, 0x01, 0x00, 0x01 )
  t( 0x03, 0x02, 0x02, 0x03 )
  t( 0x05, 0x10, 0x05, 0x10 )
  t( 0x00, 0x00, 0x00, 0x00 )
