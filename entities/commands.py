

def parse(commands):

    parsed_commands = []
    
    for instr in commands:

        clauses = instr.split(" ")

        if len(clauses) == 2:
            if clauses[0] == "CAPTURE":
                parsed_commands.append(instr)

            else:
                steps = int(clauses[1])//5
                for i in range (steps):

                    parsed_commands.append(f"{clauses[0]} 5")

                rem = int(clauses[1])%5
                if rem != 0:
                    parsed_commands.append(f"{clauses[0]} {rem}")
        
        elif len(clauses) == 3:

            if clauses[0] == "FORWARD" and clauses[2] == "RIGHT":
                
                parsed_commands += ["ROTATE 45"]
                for i in range(5):
                    parsed_commands.append("FORWARD 7.071")
                parsed_commands += ["ROTATE 45"]

            elif clauses[0] == "FORWARD" and clauses[2] == "LEFT":
                
                parsed_commands += ["ROTATE -45"]
                for i in range(5):
                    parsed_commands.append("FORWARD 7.071")
                parsed_commands += ["ROTATE -45"]

            elif clauses[0] == "BACKWARD" and clauses[2] == "LEFT":
                
                parsed_commands += ["ROTATE 45"]
                for i in range(5):
                    parsed_commands.append("REVERSE 7.071")
                parsed_commands += ["ROTATE 45"]
            elif clauses[0] == "BACKWARD" and clauses[2] == "RIGHT":
                
                parsed_commands += ["ROTATE -45"]
                for i in range(5):
                    parsed_commands.append("REVERSE 7.071")
                parsed_commands += ["ROTATE -45"]

    
    return parsed_commands






