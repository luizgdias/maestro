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

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

os.system('echo "\n*** Executando CLUSTALW..."')
parser = argparse.ArgumentParser()
parser.add_argument("-in", dest="in_file")
parser.add_argument("-out", dest="out_format")

args = parser.parse_args()
#obs: o diretório do arquivo phylip de saida e sempre o mesmo do diretorio da entrada!!!!!
os.system('clustalw -INFILE='+args.in_file+' -OUTPUT='+args.out_format)
print("**** Programa executado: CLUSTALW \nparâmetros consumidos: ",args.in_file, args.out_format,"\n")

#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()

