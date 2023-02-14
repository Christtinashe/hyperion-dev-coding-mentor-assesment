def equivalent_resistance(network):
    # Helper function to calculate the equivalent resistance of a parallel network
    def parallel(resistors):
        reciprocal = 0
        for resistor in resistors:
            reciprocal += 1 / resistor
        return 1 / reciprocal
    
    # A list to store the resistors in the network
    resistors = []
    # A string to temporarily store the current resistor being processed
    current_resistor = ""
    # A flag to indicate if the resistors are in a parallel configuration
    in_parallel = False
    # Iterate over each character in the network string
    for char in network:
        # If the character is '(' then a new sub-network is starting
        if char == '(':
            # If there is a current resistor, add it to the resistors list
            if current_resistor:
                resistors.append(float(current_resistor))
                current_resistor = ""
            # Add a new list to represent the sub-network
            resistors.append([])
        # If the character is ')' then the sub-network has ended
        elif char == ')':
            # If there is a current resistor, add it to the sub-network
            if current_resistor:
                resistors[-1].append(float(current_resistor))
                current_resistor = ""
            # Calculate the equivalent resistance of the sub-network
            resistors[-1] = equivalent_resistance("".join(map(str, resistors[-1])))
        # If the character is '[' then a parallel network is starting
        elif char == '[':
            # If there is a current resistor, add it to the resistors list
            if current_resistor:
                resistors.append(float(current_resistor))
                current_resistor = ""
            # Set the in_parallel flag to True
            in_parallel = True
            # Add a new list to represent the parallel network
            resistors.append([])
        # If the character is ']' then the parallel network has ended
        elif char == ']':
            # If there is a current resistor, add it to the parallel network
            if current_resistor:
                resistors[-1].append(float(current_resistor))
                current_resistor = ""
            # Set the in_parallel flag to False
            in_parallel = False
            # Calculate the equivalent resistance of the parallel network
            resistors[-1] = parallel(resistors[-1])
        # If the character is ',' then a new resistor is starting
        elif char == ',':
            # If there is a current resistor, add it to the appropriate list
            if current_resistor:
                if in_parallel:
                    resistors[-1].append(float(current_resistor))
                else:
                    resistors.append(float(current_resistor))
                current_resistor = ""
        # Otherwise, add the character to the current resistor string
        else:
            current_resistor += char
    # If there is a remaining current resistor, add it to the resistors list
    if current_resistor:
        resistors.append(float(current_resistor))
    
    if len(resistors) == 1:
        return resistors[0]
    else:
        return sum(resistors)
