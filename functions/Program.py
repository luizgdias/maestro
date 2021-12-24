def createProgram(onto, name, operation, source):
    program = onto.Program(name)
    program.is_a.append(operation)

    metadata_url = onto.Url(source)
    program.hasMetadata.append(metadata_url)

    return program

def associateProgramPort(program, inPorts, outPorts):
    """[função utilizada para associar programas em portas]
        Arguments:
            ontoexpline {[ontology]} -- [ontologia utilizada pelo código, no caso: ontoexpline com provone, expline, metadata e edam]
            inports {[port list ]} -- [lista de portas de entrada]
            outports {[port list]} -- [lista de portas de saída]
        """
    if inPorts and outPorts:
        program.hasInPort = inPorts
        program.hasOutPort = outPorts
    else:
        print("|*** Relações não podem ser vazias!")
        return exit()

