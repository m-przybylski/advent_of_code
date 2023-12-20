from collections import deque
from math import lcm

input = "input/day20"

class Module:
    def __init__(self, name) -> None:
        self.name = name
        self.state = False
        self.outputs = []
        self.inputs = []

    def addOutput(self, output) -> None:
        self.outputs.append(output)

    def addInput(self, input) -> None:
        self.inputs.append(input)


    def __str__(self) -> str:
        return f"{self.name}, type: {self._type} state: {'on' if self.state else 'off'}, in: {self.inputs}, out: {self.outputs}"
    
    def __repr__(self) -> str:
        return self.__str__()


class FlipFlop(Module):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._type = '%'
    
    def input(self, signal: bool, _) -> bool | None:
        if (not signal):
            self.state = not self.state
            return self.state
        
        return None

class Inverter(Module):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._type = "&"

    def input(self, signal: bool, wires) -> bool:
        if all([wire.state for wire in [wires[input] for input in self.inputs]]):
            self.state = False
        else:
            self.state = True
        
        return self.state

connections = open(input).read().splitlines()

def createModule(type, name) -> Module:
    if (type == '%'):
        return FlipFlop(name)
    else:
        return Inverter(name)

def parseConnection(connection: str):
    input, outputs = connection.split(" -> ")
    outputs = [output for output in outputs.split(", ")]
    return (input[1:], input[0], outputs)

def buildCircuit(connections):
    wires = {}
    start = None
    for connection in connections:
        input, type, outputs = parseConnection(connection)
        if (type == 'b'):
            start = outputs
        else:
            wires[input] = createModule(type, input)

    for connection in connections:
        input, type, outputs = parseConnection(connection)
        if (type == 'b'):
            start = outputs
        else:
            for output in outputs:
                wires[input].addOutput(output)
                if (output in wires):
                    wires[output].addInput(input)

    return start, wires

def partOne(start, wires):
    def buttonPress():
        low_count = 1
        high_count = 0
        signals = deque()
        def addSignal(signal, outputs):
            signals.append((signal, outputs))

        def pulse(signal: bool, outputs: list):
            high_count = 0
            low_count = 0
            for output in outputs:
                if signal:
                    high_count += 1
                else:
                    low_count += 1

                if output in wires:
                    module = wires[output]
                    new_pulse = module.input(signal, wires)
                    if new_pulse != None:
                        addSignal(new_pulse, module.outputs.copy())
            
            return (low_count, high_count)
        
        addSignal(False, start)
        
        while len(signals) > 0:
            signal, outputs = signals.popleft()
            l, h = pulse(signal, outputs)
            low_count += l
            high_count += h
            

        return (low_count, high_count)

    count_l = 0
    count_h = 0

    for _ in range(1000):
        l, h = buttonPress()
        count_l += l
        count_h += h

    print(count_l * count_h)


def partTwo():
    start, wires = buildCircuit(connections)
    def findNode(module_name):
        for wire in wires.values():
            if module_name in wire.outputs:
                return wire

    final = findNode("rx")

    def buttonPress(module_should_be_true, wires):
        signals = deque()
        def addSignal(signal, outputs):
            signals.append((signal, outputs))

        def pulse(signal: bool, outputs: list):
            for output in outputs:
                if output in wires:
                    module = wires[output]
                    new_pulse = module.input(signal, wires)
                    if new_pulse != None:
                        if module_should_be_true in module.outputs and new_pulse == False:
                            return True
                        addSignal(new_pulse, module.outputs.copy())
        
        addSignal(False, start)
        
        while len(signals) > 0:
            signal, outputs = signals.popleft()
            if pulse(signal, outputs):
                return False
            
        return True
    
    def getButtonPressesToBeHigh(module_should_be_true):
        _, wires = buildCircuit(connections)
        count = 1
        while buttonPress(module_should_be_true, wires):
            count += 1

        return count

    print(lcm(*[getButtonPressesToBeHigh(input) for input in final.inputs]))
    

s, w = buildCircuit(connections)
# 684125385
partOne(s, w)
# 225872806380073
partTwo()
