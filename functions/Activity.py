def createActivity(ontoexpline, name, domainOperation, inRelations, outRelations, optional, implementers, first):
    for program in implementers:
        if (domainOperation in program.is_a):
            activity = ontoexpline.Abstract_activity(name)
            activity.is_a.append(domainOperation)
            activity.hasInputRelation = inRelations
            activity.hasOutputRelation = outRelations
            activity.executedBy.append(program)
            program.implements.append(activity)

            if (optional == True):
                activity.is_a.append(ontoexpline.Optional)
            else:
                activity.is_a.append(ontoexpline.Mandatory)
            if(first == True):
                activity.is_a.append(ontoexpline.First)
        else:
            print("|*** Activity e ", program," possuem tipos domínio incompatíveis!")

    for r in inRelations:
        r.consumedBy.append(activity)
    for r_out in outRelations:
        r_out.generatedBy.append(activity)

    print("|*** Activity: ", activity.name, " instanciada.")

    if (len(implementers) > 1):
        activity.is_a.append(ontoexpline.Variant)

    return activity