#!/usr/bin/python3
import argparse
import sys, os
from time import *
from optparse import OptionParser
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
from dfa_lib_python.element import Element
from time import sleep

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

os.system('echo "\n*** Executando RemovePipe..."')

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="file")
args = parser.parse_args()

validated = open("/home/luiz/PycharmProjects/MaestroOO/sources/input/VALIDATED_SEQUENCE", "w")
f = open(str(args.file), "r")

lines_seen_so_far = set()
for line in f:
    if line not in lines_seen_so_far:
        validated.write(line)
        lines_seen_so_far.add(line)
validated.close()
f.close()
print("**** Programa executado: RemovePipe \nparâmetros consumidos: ",args.file)

#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()

