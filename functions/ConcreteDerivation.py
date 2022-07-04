import os

from functions.ProvenanceCalls import insertProspectiveCall
from sources.TemplateExecution import createTemplate

def verifyMatchBetweenAbstractAndConcreteItems(ontoexpline, abs_wf, options):
    # print(abs_wf)
    # print(options)
    consumedPorts = []
    relations = []
    ports_associated_with_attributes = []


    for program in options:
        print(program[1])
        for port in program[1].hasInPort:
            print(port)
            consumedPorts.append(port)
    # print("Portas consumidas pelos programas variantes: ",consumedPorts)

    for act in abs_wf:
       # print(act[0].hasOutputRelation)
        for relation in act[0].hasOutputRelation:
            for at in relation.composedBy:
                for p in at.wasAssociatedWith:
                    ports_associated_with_attributes.append(p)
            relations.append(relation)
    # print(relations)

    # print("Portas consumidas pelas atividades do wf: ",ports_associated_with_attributes)

    #faz a varredura nas portas consumidas pelos programas variantes
    for port in consumedPorts:
        #se as portas consumida por esses programas não forem geradas pelas atividades do abs wf
        #maestro não da continuidade na criação concreta e finaliza
        if not(port in ports_associated_with_attributes):
            search = ontoexpline.search(type = ontoexpline.Relation)
            for r in search:
                for a in r.composedBy:
                    if port in a.wasAssociatedWith:
                        # print(r)
                        search2 = ontoexpline.search(type = ontoexpline.Abstract_activity)
                        for aa in search2:
                            if r in aa.hasOutputRelation:
                                print("WF INVÁLIDO, FALTA A PORTA: ", port, " ASSOCIADA A ", port.wasAssociatedWith,
                                      "\nGerada pela Atividade: ", aa, " QUE NÃO ESTÁ NO WF")
                                exit(0)
        else:
            print("Dependência: (porta)", port.name ," verificada...\nIniciando a instanciação concreta...")



def absWfToConcreteWf(ontoexpline, abs_wf, options):
    verifyMatchBetweenAbstractAndConcreteItems(ontoexpline, abs_wf, options)

    print("|*** Creating concrete workflow using: ", options," as options...")
    print("|*** Executing: ", os.path.basename(__file__))

    # df = "df = Dataflow('df_tag')\n\n"
    # f = open("sources/prospectiveProvenance.py", "a+")
    # f.write(df)
    # f.close()

    #aa[0] guarda as atividades, aa[1] guarda as dependências de cada atividade
    for aa in abs_wf:
        # print(aa)
        # insertProspectiveCall(ontoexpline, aa)
        if (ontoexpline.Variant in aa[0].is_a):
            for op in options: #se a aa é variante e está dentro de op enviado via usuário, está coerente
                if (aa[0] in op) and (op[1] in aa[0].executedBy):
                    # print(aa[0]," é variante e pode ser executada por ", op[1].name)
                    # createActivityTemplate(ontoexpline, op[0])
                    createTemplate(ontoexpline, op[1])
        else:
            # print(aa[0], "é mandatória e é executada por ",aa[0].executedBy)
            for program in aa[0].executedBy: #esse for é retórico, a API da ontologia sempre devolve uma lista com um elemento pra cada atividade mandatória
                # print("\n|*** Criando template para", program.name,". In: " , os.path.basename(__file__))
                createTemplate(ontoexpline, program)

            if ontoexpline.Variant in aa[0].is_a:
                print(aa[0], " é variante")
