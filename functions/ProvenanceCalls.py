import os

from dfa_lib_python.dataflow import Dataflow
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

def insertProspectiveCall(ontoexpline, abs_wf):

    df = "df = Dataflow('df_tag')\n\n"
    f = open("sources/prospectiveProvenance.py", "a+")

    #limpando o arquivo que contém o modelo de dados de proveniência (prospectiveProvenance.py)
    if not(os.path.getsize("sources/prospectiveProvenance.py") == 0):
        print("prospectiveProvenance file is not empty! Cleaning file..")
        file_to_delete = open("sources/prospectiveProvenance.py", 'w')
        file_to_delete.write("")
        file_to_delete.close()

    #inserindo a tag do dataflow
    f.write(df)

    for activity in abs_wf:
        print("PROSPECTIVE CALL ABOUT: ",activity)
        # tf = Transformation(activity.name)
        # tf_input = Set(activity.name, SetType.INPUT,
        #                 [Attribute("Alignmt", AttributeType.TEXT),
        #                  Attribute("Trimmer", AttributeType.TEXT),
        #                  Attribute("Program", AttributeType.TEXT)])
        # tf_output = Set(activity.name, SetType.OUTPUT,
        #                  [Attribute("Alignmt", AttributeType.TEXT),
        #                   Attribute("Trimmer", AttributeType.TEXT),
        #                   Attribute("Program", AttributeType.TEXT)])
        # tf.set_sets([tf_input, tf_output])
        # df.add_transformation(tf)

        input_attributes = ""
        output_attributes = ""

        #captura os atributos de entrada da atividade para definir como atributos da dfanalyzer
        for in_rel in activity[0].hasInputRelation:
            for in_att in in_rel.composedBy:
                input_attributes = input_attributes+"Attribute("+in_att.name+", AttributeType.TEXT)"

        #captura os atributos de saida da atividade para definir como atributos da dfanalyzer
        for out_rel in activity[0].hasOutputRelation:
            for out_att in out_rel.composedBy:
                output_attributes = output_attributes+"Attribute("+out_att.name+", AttributeType.TEXT)"

        prospectiveCall = "tf_"+str(activity[0].name)+" = Transformation("+str(activity[0].name)+")\n" +\
                          "tf_"+str(activity[0].name)+"_input = Set("+str(activity[0].name)+", SetType.INPUT,\n" +\
                          "["+input_attributes+"])\n" + \
                          "tf_"+str(activity[0].name)+"_output = Set("+str(activity[0].name)+", SetType.OUTPUT,\n"+\
                          "[Attribute('Alignmt', AttributeType.TEXT),\n" +\
                          "["+output_attributes+"])\n" + \
                          "tf_"+str(activity[0].name)+".set_sets([tf_"+str(activity[0].name)+"_input, tf_"+str(activity[0].name)+"_output])\n" +\
                          "df.add_transformation(tf_"+str(activity[0].name)+")\n\n"
        f.write(prospectiveCall)
    f.close()

def insertRetrospectiveCall(ontoexpline, program, source):
    '''Essa função separa o que é import do que é conteudo executável,
    depois de separar ela insere as chamadas de proveniencia deixando o arquivo com estrutura:
    imports, inicio da chamada de proveniencia, conteudo do script, final da chamada de proveniência.'''
    if (False in program.hasRetrospectiveCall):
        #procura o metadado referente ao arquivo py que vai executar a atividade e insere as chamadas de proveniencia
        # print("meta name:", source)
        originalProgram = open(source, "r")
        retrospectiveProvenanceFile = open("/home/luiz/PycharmProjects/MaestroOO/sources/retrospectiveProvenance.py", "a")

        print("|*** Inserting DfAnalyzer retrospective calls on: ", source, ". In:", os.path.basename(__file__))
        print("|*** Using program: ", program, " to run: ", source,"\n")

        originalContent = originalProgram.readlines()

        imports = []
        content = []
        for line in originalContent:
            if ((("#") in line) or (("import") in line)) :
                imports.append(line)
            else:
                content.append(line)

        f = open(source, "w")
        for line in imports:
            f.write(str(line))

        inports = []
        for i in program.hasInPort:
            inports.append(i.name)

        provenance_start = "#task = Task(taskId, dataflow_tag, taskName)\n" +\
                "#task_input = DataSet(dataflow_tag, [Element("+str(inports)+")])\n"+\
                "#task.add_dataset(task_input)\n"+\
                "#task.begin()"

        f.write(str("\n"+provenance_start+"\n"))
        retrospectiveProvenanceFile.write(str("\n"+provenance_start+"\n"))



        for line in content:
            f.write(str(line))
        outports = []
        for i in program.hasOutPort:
            outports.append(i.name)

        provenance_end =    "#task_output = DataSet(dataflow_tag, [Element("+str(outports)+")])\n"+\
                            "#task.add_dataset(task_output)\n" +\
                            "#task.end()\n"

        f.write(str("\n"+provenance_end+"\n"))
        retrospectiveProvenanceFile.write(str("\n"+provenance_end+"\n"))

        f.close()
        retrospectiveProvenanceFile.close()

        program.hasRetrospectiveCall = [True]
        ontoexpline.save(file="ontologies/ontoexpline.owl", format="rdfxml")