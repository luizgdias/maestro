
#task = Task(1, dataflowTag_Experiment_1, taskName_remove_pipe)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflowTag_Experiment_1, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(3, dataflowTag_Experiment_1, taskName_clustalw)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflowTag_Experiment_1, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(4, dataflowTag_Experiment_1, taskName_model_generator)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflowTag_Experiment_1, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(5, dataflowTag_Experiment_1, taskName_readseq)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflowTag_Experiment_1, [Element(['CONVERTED_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()


#task = Task(7, dataflowTag_Experiment_1, taskName_mrbayes)
#task_input = DataSet(dataflow_tag, [Element(['CONVERTED_ALIGNMENT', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()

#task_output = DataSet(dataflowTag_Experiment_1, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()

