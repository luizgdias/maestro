#!/usr/bin/python3
import os
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
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_output'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['Validation_input'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['File1023_Validated.txt'])])
#task.add_dataset(task_input)
#task.begin()

os.system('echo "*** executing mafft\n"')


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()


#task_output = DataSet(dataflow_tag, [Element(['file1024'])])
#task.add_dataset(task_output)
#task.end()

