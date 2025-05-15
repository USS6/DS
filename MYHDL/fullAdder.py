""" myhdl package initialization.

This module provides the following myhdl objects:
Simulation -- simulation class
StopSimulation -- exception that stops a simulation
now -- function that returns the current time
Signal -- factory function to model hardware signals
SignalType -- Signal base class
ConcatSignal --  factory function that models a concatenation shadow signal
TristateSignal -- factory function that models a tristate shadow signal
delay -- callable to model delay in a yield statement
posedge -- callable to model a rising edge on a signal in a yield statement
negedge -- callable to model a falling edge on a signal in a yield statement
join -- callable to join clauses in a yield statement
intbv -- mutable integer class with bit vector facilities
modbv -- modular bit vector class
downrange -- function that returns a downward range
bin -- returns a binary string representation.
       The optional width specifies the desired string
       width: padding of the sign-bit is used.
concat -- function to concat ints, bitstrings, bools, intbvs, Signals
       -- returns an intbv
instances -- function that returns all instances defined in a function
always --
always_comb -- decorator that returns an input-sensitive generator
always_seq --
ResetSignal --
enum -- function that returns an enumeration type
traceSignals -- function that enables signal tracing in a VCD file
toVerilog -- function that converts a design to Verilog

"""
from myhdl import block, always_seq, Signal, intbv, instance, delay, Simulation, now, ResetSignal
# 1. Define the Inputs and Outputs --> block
@block
def binary_counter(clk,reset,count):
# 2. Describe the Internal Logic --> logic
    @always_seq(clk.posedge,reset=reset)
    def logic():
        if reset:
            count.next = 0
        else:
            count.next = count+1
    return logic
# 3. Implement the Counter in MyHDL
# 4. Create a Testbench
# 5. Convert to Verilog
@block
def testbench():
    clk = Signal(bool(0))
    reset = ResetSignal(0, active=1, isasync=True)
    count = Signal(intbv(0)[4:])

    counter_inst = binary_counter(clk, reset, count)

    @instance
    def clkgen():
        while True:
            clk.next = not clk
            yield delay(10)

    @instance
    def stimulus():
        print("Time    Reset   Count")
        reset.next = 1
        yield delay(20)
        reset.next = 0

        for _ in range(10):
            yield clk.posedge
            print(f"{now():<7} {int(reset):<7} {int(count):04b}")

    return counter_inst, clkgen, stimulus

tb = testbench()
sim = Simulation(tb)
sim.run(200)
