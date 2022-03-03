#!/usr/bin/python3
import argparse, json
from time import *

import sys, os
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
#task_input = DataSet(dataflow_tag, [Element(['fileConvertedAlignment', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['fileConvertedAlignment', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['fileConvertedAlignment', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['fileConvertedAlignment', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['fileConvertedAlignment', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['fileConvertedAlignment', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="file")
parser.add_argument("-nr", dest="nruns")
parser.add_argument("-nc", dest="nchains")
parser.add_argument("-brn", dest="burnin")
parser.add_argument("-prt", dest="printfreq")
parser.add_argument("-ng", dest="ngen")
parser.add_argument("-rt", dest="rates_mrbayes")

args = parser.parse_args()

print("**** Programa executado: MrBayes \n parâmetros consumidos: ",args.file, args.nruns, args.nchains, args.burnin)
#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()

