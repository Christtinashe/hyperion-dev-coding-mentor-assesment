def equivalent_resistance(network):
    # Helper function to calculate the equivalent resistance of a parallel network
    def parallel(resistors):
        reciprocal = 0
        for resistor in resistors:
            reciprocal += 1 / resistor
        return 1 / reciprocal
    
    resistors = []
    current_resistor = ""
    in_parallel = False
    for char in network:
        if char == '(':
            if current_resistor:
                resistors.append(float(current_resistor))
                current_resistor = ""
            resistors.append([])
        elif char == ')':
            if current_resistor:
                resistors[-1].append(float(current_resistor))
                current_resistor = ""
            resistors[-1] = equivalent_resistance("".join(map(str, resistors[-1])))
        elif char == '[':
            if current_resistor:
                resistors.append(float(current_resistor))
                current_resistor = ""
            in_parallel = True
            resistors.append([])
        elif char == ']':
            if current_resistor:
                resistors[-1].append(float(current_resistor))
                current_resistor = ""
            in_parallel = False
            resistors[-1] = parallel(resistors[-1])
        elif char == ',':
            if current_resistor:
                if in_parallel:
                    resistors[-1].append(float(current_resistor))
                else:
                    resistors.append(float(current_resistor))
                current_resistor = ""
        else:
            current_resistor += char
    if current_resistor:
        resistors.append(float(current_resistor))
    
    if len(resistors) == 1:
        return resistors[0]
    else:
        return sum(resistors)
