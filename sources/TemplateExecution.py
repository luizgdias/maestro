import os
from functions.ProvenanceCalls import *
from pathlib import Path

def createTemplate(ontoexpline, program):
    print("|*** Creating command line to ", program.name ,". In: ", os.path.basename(__file__))
    #buscando a atividade que é implementada pelo programa
    # so pode ter 1 metadado url que é o arquivo py
    activity = ontoexpline.search(executedBy=program)
    print(activity[0].hasMetadata[0].name)

    template = ''
    conf_param = []
    for meta in program.hasMetadata:
        if ontoexpline.Url in meta.is_a:
            # print("script => ",meta.name)
            file_source = Path(meta.name)
            template = template + str(meta.name)
            os.system('chmod +x ' + meta.name)

            # f = open(activity[0].hasMetadata[0].name, "w")
            # f.write("python2 "+str(file_source))
            # f.close()

            # for inputPort in program.hasInPort:
            #     template = template + " -f=" + inputPort.name

        if ontoexpline.Configuration_Parameter in meta.is_a:
            print("|*** ConfigurationParameter: ",meta.name," in: ", os.path.basename(__file__))
            template = template+" "+meta.name+" "

            if meta.name == "--act":
                print("******************meta", meta)
                template = template + str(program.implements[0].name)

            if meta.name == "-a":
                template = template + str(program.name)

            if meta.name == "-p":
                template = template + str(program.name)



            for val in meta.value:
                template = template + val+" "
                conf_param.append(val)

    f = open(activity[0].hasMetadata[0].name, "w")
    f.write('os.system("python2 '+str(template)+'")\n')
    f.close()

    f = open("sources/wf.py", "a")
    f.write('os.system("python '+str(activity[0].hasMetadata[0].name)+'")\n')
    insertRetrospectiveCall(ontoexpline, program, activity[0].hasMetadata[0].name)

    # os.system(template)
