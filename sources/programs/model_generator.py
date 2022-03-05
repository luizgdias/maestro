#!/usr/bin/python3
import sys, os
from time import *
import argparse

os.system('echo "\n*** Executando MODELGENERATOR..."')
parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="in_file")
parser.add_argument("-gamma", dest="number_gamma_categories")

args = parser.parse_args()
os.system('java -jar /home/luiz/PycharmProjects/MaestroOO/sources/programs/modelgenerator_v_851/modelgenerator.jar '+args.in_file+' '+args.number_gamma_categories)
print("**** Programa executado: modelgenerator \nparâmetros consumidos: ",args.in_file, args.number_gamma_categories,"\n")
