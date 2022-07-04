#! /usr/bin/env python
# TITULO             : Clustalw: Alinhamento de sequencias
# AUTOR              : Kary Ocana
# DATA               : 26/10/2009
# DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Executa Clustalw 
# ==============================================================================
# Data da ultima alteracao do script: 30/01/2008
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, sys, commands, re, pickle, string 
#-------------------------------------------------------------------------------
# Abrindo o diretorio....
  sequence_count = '0';                                                           #contar as sequencias pro ajuste do MAFFT
  # For file in os.listdir (dirin_do_ficheiro):
      #--- Mount directory and separate filename
      #--- Mount name of fasta and mafft files
# Saida automatica .aln e .dnd

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()


def paramModuleExecution(dirin):
  for file in os.listdir (dirin):
    if re.search ('filein.fasta', file) is not None:
      diretorio = file.split("/")
      nome = diretorio[diretorio.count('/')-1].split(".")

      fasta = os.path.join (dirin, file)
      clustalw = os.path.join (dirin, nome[0]+ ".aln")
      
      print "Aligning: " + fasta + " ...";

      cmd = "clustalw -output=fasta -infile=" + fasta + " -outfile=" + clustalw 
      handle = os.popen(cmd, 'r', 1)
      for line in handle:
        print line,
      handle.close()



#task_output = DataSet(dataflow_tag, [Element(['SEQUENCES_ALIGNMENT'])])
#task.add_dataset(task_output)
#task.end()

