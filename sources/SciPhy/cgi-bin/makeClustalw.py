#!/usr/bin/python3
import os
import argparse
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
#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()
#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()


os.system('echo "\n*** Executando Alinhamento..."')
parser = argparse.ArgumentParser()
parser.add_argument("-INFILE", dest="in_file")
parser.add_argument("-OUTFILE", dest="out_file")
parser.add_argument("aa", dest="sequence_type")
parser.add_argument("-o", dest="directory")
parser.add_argument("-act", dest="activity_id")
parser.add_argument("-a", dest="alignment_program")


os.system("python2 arpa.py -t "+ parser.sequence_type+" -o "+parser.directory+" --act "+parser.activity_id+" -a "+parser.alignment_program+" inputTestGc/", parser.in_file)
print("**** Programa executado: Mafft \nparâmetros consumidos: ",parser.in_file,parser.out_file,"\n")



#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()
