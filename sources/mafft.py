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



os.system('echo "\n*** Executando Mafft..."')
parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="file")
args = parser.parse_args()

print("**** Programa executado: Mafft \nparâmetros consumidos: ",args.file,"\n")




