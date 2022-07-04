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

os.system('echo "\n*** Executando MUSCLE..."')
parser = argparse.ArgumentParser()
parser.add_argument("-in", dest="in_file")
parser.add_argument("-out", dest="out_file")

args = parser.parse_args()
os.system('muscle -in '+args.in_file+' -out '+args.out_file)
print("**** Programa executado: MUSCLE \nparâmetros consumidos: ",args.in_file, args.out_file,"\n")
