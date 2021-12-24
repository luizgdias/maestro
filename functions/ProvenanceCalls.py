from dfa_lib_python.dataflow import Dataflow
from dfa_lib_python.dataflow import Dataflow
from dfa_lib_python.dependency import Dependency
from dfa_lib_python.transformation import Transformation
from dfa_lib_python.attribute import Attribute
from dfa_lib_python.attribute_type import AttributeType
from dfa_lib_python.set import Set
from dfa_lib_python.set_type import SetType
from dfa_lib_python.task import Task
from dfa_lib_python.dataset import DataSet
from dfa_lib_python.element import Element

def insertRetrospectiveCall(ontoexpline, program):
    '''Essa função separa o que é import do que é conteudo executável,
    depois de separar ela insere as chamadas de proveniencia deixando o arquivo com estrutura:
    imports, inicio da chamada de proveniencia, conteudo do script, final da chamada de proveniência.'''
    originalProgram = open("sources/"+str(program.name).lower()+".py", "r")
    originalContent = originalProgram.readlines()

    imports = []
    content = []
    for line in originalContent:
        if ((("#!/usr/bin/python3") in line) or (("import") in line)):
            imports.append(line)
        else:
            content.append(line)

    f = open("sources/"+str(program.name).lower()+".py", "w")
    for line in imports:
        f.write(str(line))

    inports = []
    for i in program.hasInPort:
        inports.append(i.name)

    provenance_start = "#task = Task(taskId, dataflow_tag, taskName)\n" +\
            "#task_input = DataSet(dataflow_tag, [Element("+str(inports)+")])\n"+\
            "#task.add_dataset(task_input)\n"+\
            "#task.begin()"

    f.write(str("\n"+provenance_start+"\n"))

    for line in content:
        f.write(str(line))
    outports = []
    for i in program.hasOutPort:
        outports.append(i.name)

    provenance_end =    "#task_output = DataSet(dataflow_tag, [Element("+str(outports)+")])\n"+\
                        "#task.add_dataset(task_output)\n" +\
                        "#task.end()\n"

    f.write(str("\n"+provenance_end+"\n"))
    f.close()