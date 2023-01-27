
#task = Task(1, dataflow_tag, taskName_remove_pipe)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(3, dataflow_tag, taskName_clustalw)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(4, dataflow_tag, taskName_modelgenerator)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(5, dataflow_tag, taskName_read_seq)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflow_tag, [Element(['CONVERTED_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(7, dataflow_tag, taskName_mrbayes)
#task_input = DataSet(dataflow_tag, [Element(['CONVERTED_ALIGNMENT', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()

