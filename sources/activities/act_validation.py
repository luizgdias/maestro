
#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()
os.system("python2 sources/SciPhy/cgi-bin/arpa.py -f  -t  -o out  -a remove_pipe --act validation")

#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()

