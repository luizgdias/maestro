from sources.TemplateExecution import createTemplate


def absWfToConcreteWf(ontoexpline, abs_wf, options):
    # wf_head = ontoexpline.search(type=ontoexpline.First)
    # wf_rel = ontoexpline.search(type=ontoexpline.Relation)
    #
    # for head in wf_head:
    #     x = (head.hasInputRelation)
    # wf_head.append(x)
    #
    # abs_wf.insert(0, list(wf_head)) #inserindo a primeira atividade do wf


    #aa[0] guarda as atividades, aa[1] guarda as dependências de cada atividade
    for aa in abs_wf:
        if (ontoexpline.Variant in aa[0].is_a):
            for op in options: #se a aa é variante e está dentro de op enviado via usuário, está coerente
                if (aa[0] in op) and (op[1] in aa[0].executedBy):
                    # print(aa[0]," é variante e pode ser executada por ", op[1].name)
                    print("\nCriando template para", op[1].name)
                    createTemplate(ontoexpline, op[1])
        else:
            # print(aa[0], "é mandatória e é executada por ",aa[0].executedBy)
            for program in aa[0].executedBy: #esse for é retórico, a API da ontologia sempre devolve uma lista com um elemento pra cada atividade mandatória
                print("\nCriando template para", program)
                createTemplate(ontoexpline, program)



            if ontoexpline.Variant in aa[0].is_a:
                print(aa[0], " é variante")
