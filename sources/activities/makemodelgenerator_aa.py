#! /usr/bin/env python
# TITULO            : Make Modelgenerator
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do arpa.py
#                     Executa Modelgenerator. Da modelo evolutivo (AIC1 [usada], AIC2, BIC) e
#                     Saida de parametros phymlBoot.sh, phyml.sh, puzzleBoot.sh, treePuzzle.sh
# ==============================================================================
# Data da ultima alteracao do script: 30/01/2008
#                                   : 15/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
import shutil as sh
#-------------------------------------------------------------------------------
  # Abrindo o modelgenerator para leitura
  os.chmod(path_mg, 0755)  # Assume it's a file
  # Lendo o arquivo modelgenerator0.out para editar e obter parametros AIC1, AIC2 ou BIC
  # Extraindo informacao de modelgenerator0.out 
  mg_info = mg_parameter[1].split(":")                                          # mg_info[1] = modelo e parametros limpos
  parametro_filogenia = mg_info[1].split("\n")                          # os parametros de Modelos Evolutivos sao MODEL+I+G+F (estes tres ultimos sao os parametros e nao tem ordem definida)
  parametro_filogenia_clean = parametro_filogenia[0].replace(" ", "")           # Limpando de espacos em branco
  modelo_param = parametro_filogenia_clean.split("+")                          # os parametros de Modelos Evolutivos sao MODEL+I+G+F (estes tres ultimos sao os parametros e nao tem ordem definida)
  # Executando o modelgenerator do shell
    #original if m.endswith('.mafft'):
      #originais path_mafft = os.path.join(dirin, m)
      #originais os.chmod(path_mafft, 0755)  # Assume it's a file
      os.chmod(path_aln, 0755)  # Assume it's a file
      #original cmd_mg = "java -jar /usr/local/modelgenerator/modelgenerator.jar " + path_mafft + " 6 " 
      os.chmod(path_mg, 0755)  # Assume it's a file
      #Chamando def paramCleanModelgenerator
      #Chamando def paramMoveFilesModelgenerator

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_input)
#task.begin()

def paramCleanModelgenerator(dirincurrent, mg):
  print "\tOpening the existing " + mg + " for read"
  path_mg = os.path.join(dirincurrent, mg)
  print mg
  print path_mg
  text_mg = open(path_mg).read()
  mg_parameter = text_mg.split("\n\n****Akaike Information Criterion 1 (AIC1)****\n\n")
  model_only = str(modelo_param[0])
  print model_only
  return model_only

def paramMoveFilesModelgenerator(dirin, dirincurrent):
  print "\tMoving modelgenerator0.out and *.sh files " + "from " + dirincurrent + " to " + dirin 
  found = False
  for file_move in os.listdir(dirincurrent):
    if file_move.endswith('.out'):
      found  = True
      sh.move(file_move, dirin)						
    if file_move.endswith('.sh'):
      found  = True
      sh.move(file_move, dirin)
  if found is False:
    print "There is not modelgenerator.out and files.sh"
    sys.exit(2)
  
def paramModuleModelgenerator(dirin):
  found = False
  for m in os.listdir(dirin):
    if m.endswith('.aln'):
      found  = True
      path_aln = os.path.join(dirin, m)
  
      print "Building the Modelgenerator file"
      cmd_mg = "java -jar modelgenerator.jar " + path_aln + " 6 " 
      handle_mg = os.popen(cmd_mg, 'r', 1)
      for line_mg in handle_mg:
        print line_mg,
      handle_mg.close()
  if found is False:
    print "There is not a '*.aln' alignment file"
    sys.exit(2)

  dirincurrent = os.getcwd( )
  print dirincurrent
  for mg in os.listdir(dirincurrent):
    if mg.endswith('.out'):
      found  = True
      path_mg = os.path.join(dirincurrent, mg)
      print dirin
      print dirincurrent
      print "\tWas created " + mg + " in " + dirincurrent
      model=paramCleanModelgenerator(dirincurrent, mg)  
      paramMoveFilesModelgenerator(dirin, dirincurrent)
  if found is False:
    print "\tWas not created " + mg + " in " + dirincurrent
    sys.exit(2)

  return model

#task_output = DataSet(dataflow_tag, [Element(['fileEvolutiveModel'])])
#task.add_dataset(task_output)
#task.end()

