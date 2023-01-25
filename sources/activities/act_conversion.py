
#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()
os.system("python2 sources/SciPhy/cgi-bin/arpa.py -t  -o out  -p read_seq --act conversion --act conversion")

#task_output = DataSet(dataflow_tag, [Element(['CONVERTED_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()

