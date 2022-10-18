#!/usr/bin/python3
import sys, os
from time import *
import argparse

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

os.system('echo "\n*** Executando MODELGENERATOR..."')
parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="in_file")
parser.add_argument("-gamma", dest="number_gamma_categories")

args = parser.parse_args()
os.system('java -jar /home/luiz/PycharmProjects/MaestroOO/sources/activities/modelgenerator_v_851/modelgenerator.jar '+args.in_file+' '+args.number_gamma_categories)
print("**** Programa executado: modelgenerator \nparâmetros consumidos: ",args.in_file, args.number_gamma_categories,"\n")

#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()

