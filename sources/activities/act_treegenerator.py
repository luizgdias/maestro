
#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['CONVERTED_ALIGNMENT', 'fileEvolutiveModel'])])
#task.add_dataset(task_input)
#task.begin()
os.system("python2 sources/SciPhy/cgi-bin/arpa.py -p mrbayes -t  -o out  -nr nruns  -nc nchains  -brn burnin  -prt printfreq  -ng ngen  -rt rates_mrbayes  --act treegenerator")

#task_output = DataSet(dataflow_tag, [Element(['fileTree'])])
#task.add_dataset(task_output)
#task.end()

