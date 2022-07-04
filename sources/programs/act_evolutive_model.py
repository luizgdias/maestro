
#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()
os.system("python2 sources/SciPhy/cgi-bin/arpa.py -gamma GAMMA_CATEGORIES  -t aa  -o out  -p modelgenerator --act evolutive_model")

#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()

