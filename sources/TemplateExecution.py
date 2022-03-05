import os
from functions.ProvenanceCalls import *
from pathlib import Path

def createTemplate(ontoexpline, program):
    template = ''
    conf_param = []
    for meta in program.hasMetadata:
        if ontoexpline.Url in meta.is_a:
            print("script => ",meta.name)
            file_source = Path(meta.name)
            template = template + str(file_source)
            os.system('chmod +x ' + meta.name)

            for inputPort in program.hasInPort:
                template = template + " -f=" + inputPort.name
            insertRetrospectiveCall(ontoexpline, program)

        if ontoexpline.Configuration_Parameter in meta.is_a:
            print("ConfigurationParameter =>",meta.name)
            template = template+" "+meta.name+"="
            for val in meta.value:
                template = template + val+" "
                conf_param.append(val)

        else:
            print(meta.is_a,"*")

    print("chamada => "+template)
    f = open("sources/wf.py", "a")
    template = template.split("/")
    print("SPLIT: "+template[1])
    f.write('os.system("python '+str(template[2])+'")\n')
    # os.system(template)
