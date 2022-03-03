df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

df = Dataflow('df_tag')

tf_Atividade_Validation = Transformation(Atividade_Validation)
tf_Atividade_Validation_input = Set(Atividade_Validation, SetType.INPUT,
[Attribute(Input_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Validation.set_sets([tf_Atividade_Validation_input, tf_Atividade_Validation_output])
df.add_transformation(tf_Atividade_Validation)

tf_Atividade_Alignment = Transformation(Atividade_Alignment)
tf_Atividade_Alignment_input = Set(Atividade_Alignment, SetType.INPUT,
[Attribute(Output_Validation_att, AttributeType.TEXT)])
tf_Atividade_Alignment_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Alignment.set_sets([tf_Atividade_Alignment_input, tf_Atividade_Alignment_output])
df.add_transformation(tf_Atividade_Alignment)

tf_Atividade_Evolutive_Model = Transformation(Atividade_Evolutive_Model)
tf_Atividade_Evolutive_Model_input = Set(Atividade_Evolutive_Model, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Evolutive_Model.set_sets([tf_Atividade_Evolutive_Model_input, tf_Atividade_Evolutive_Model_output])
df.add_transformation(tf_Atividade_Evolutive_Model)

tf_Atividade_Sequences_Converter = Transformation(Atividade_Sequences_Converter)
tf_Atividade_Sequences_Converter_input = Set(Atividade_Sequences_Converter, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(converted_alignment_att, AttributeType.TEXT)])
tf_Atividade_Sequences_Converter.set_sets([tf_Atividade_Sequences_Converter_input, tf_Atividade_Sequences_Converter_output])
df.add_transformation(tf_Atividade_Sequences_Converter)

tf_Atividade_Tree_Generation = Transformation(Atividade_Tree_Generation)
tf_Atividade_Tree_Generation_input = Set(Atividade_Tree_Generation, SetType.INPUT,
[Attribute(alignment_att, AttributeType.TEXT)Attribute(converted_alignment_att, AttributeType.TEXT)Attribute(evolutiveModel_att, AttributeType.TEXT)])
tf_Atividade_Tree_Generation_output = Set(activity.name, SetType.OUTPUT,
[Attribute('Alignmt', AttributeType.TEXT),
[Attribute(phylogenomic_tree, AttributeType.TEXT)])
tf_Atividade_Tree_Generation.set_sets([tf_Atividade_Tree_Generation_input, tf_Atividade_Tree_Generation_output])
df.add_transformation(tf_Atividade_Tree_Generation)

