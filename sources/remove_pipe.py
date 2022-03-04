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


os.system('echo "\n*** Executando RemovePipe..."')

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="file")
args = parser.parse_args()

print("**** Programa executado: RemovePipe \nparâmetros consumidos: ",args.file)
