#df = Dataflow('df_tag')

#tf_validation = Transformation(validation)
#tf_validation_input = Set(validation, SetType.INPUT,
#[Attribute(Input_Validation_att, AttributeType.TEXT)])
#tf_validation_output = Set(validation, SetType.OUTPUT,
#[Attribute('Alignmt', AttributeType.TEXT),
#[Attribute(Output_Validation_att, AttributeType.TEXT)])
#tf_validation.set_sets([tf_validation_input, tf_validation_output])
#df.add_transformation(tf_validation)

#tf_alinhamento = Transformation(alinhamento)
#tf_alinhamento_input = Set(alinhamento, SetType.INPUT,
#[Attribute(Output_Validation_att, AttributeType.TEXT)])
#tf_alinhamento_output = Set(alinhamento, SetType.OUTPUT,
#[Attribute('Alignmt', AttributeType.TEXT),
#[Attribute(alignment_att, AttributeType.TEXT)])
#tf_alinhamento.set_sets([tf_alinhamento_input, tf_alinhamento_output])
#df.add_transformation(tf_alinhamento)

#tf_evolutive_model = Transformation(evolutive_model)
#tf_evolutive_model_input = Set(evolutive_model, SetType.INPUT,
#[Attribute(alignment_att, AttributeType.TEXT)])
#tf_evolutive_model_output = Set(evolutive_model, SetType.OUTPUT,
#[Attribute('Alignmt', AttributeType.TEXT),
#[Attribute(evolutiveModel_att, AttributeType.TEXT)Attribute(data_transformation_execution_id_2023_att, AttributeType.TEXT)])
#tf_evolutive_model.set_sets([tf_evolutive_model_input, tf_evolutive_model_output])
#df.add_transformation(tf_evolutive_model)

#tf_conversion = Transformation(conversion)
#tf_conversion_input = Set(conversion, SetType.INPUT,
#[Attribute(alignment_att, AttributeType.TEXT)])
#tf_conversion_output = Set(conversion, SetType.OUTPUT,
#[Attribute('Alignmt', AttributeType.TEXT),
#[Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att_eq, AttributeType.TEXT)])
#tf_conversion.set_sets([tf_conversion_input, tf_conversion_output])
#df.add_transformation(tf_conversion)

#tf_treegenerator = Transformation(treegenerator)
#tf_treegenerator_input = Set(treegenerator, SetType.INPUT,
#[Attribute(alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)Attribute(data_transformation_execution_id_2023_att, AttributeType.TEXT)])
#tf_treegenerator_output = Set(treegenerator, SetType.OUTPUT,
#[Attribute('Alignmt', AttributeType.TEXT),
#[Attribute(phylogenomic_tree, AttributeType.TEXT)])
#tf_treegenerator.set_sets([tf_treegenerator_input, tf_treegenerator_output])
#df.add_transformation(tf_treegenerator)

