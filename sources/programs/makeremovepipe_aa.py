#! /usr/bin/env python
# TITULO            : Remove pipe 
# AUTOR             : Kary Soriano
# DATA              : 15/01/2008
# DIFICULDADE       : 1
# ==============================================================================
# Objetivo do script: Executado do profile_phylogeny_aa.py
#                     Substitui pipes | por _ de alinhamentos (logo nexus), usado por MrBayes. 
# ==============================================================================
# (VIVAX)           : python remove_pipe_aa.py /disk1/home/kary/d_06/projeto/script/script_aa_pipeline/python/fasta/rh/rh.mafft
# (CASA)            : python remove_pipe_aa.py /home/kary/dir/d_06_casa/script/script_aa_pipeline/python/fasta/rh/rh.mafft
# ==============================================================================
# Data da ultima alteracao do script: 15/01/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import sys, os, re
#-------------------------------------------------------------------------------
#def paramModule(path_mafft):
  # For file in os.listdir (dirin_do_ficheiro):
      #--- Mount name of fasta and mafft files
      #os.chmod(path_mafft, 0777)  # Assume it's a file
      #mafft = os.path.join (dirin, nome[0]+ ".mafft")

#task = Task(taskId, dataflow_tag, taskName)
#task_input = DataSet(dataflow_tag, [Element(['INPUT_SEQUENCE'])])
#task.add_dataset(task_input)
#task.begin()


findreplace = [
('|' , '_'),
('(' , '_'),
(')' , '_'),
(';' , '_'),
(',' , '_'),
('/' , '_'),
('\\' , '_'),
('[' , '_'),
(']' , '_'),
(' ', '_'),
(':', '_'),
('-', '_'),
('*', '_'),
('.', '_'),
('\t', '_'),
]

def paramModule(dirin):
  print "DIRIN:**************** "+ dirin
  for file in os.listdir (dirin):
    if re.search ('filein.fasta', file) is not None:
      diretorio = file.split("/")
      nome = diretorio[diretorio.count('/')-1].split(".")
      path_mafft = os.path.join (dirin, file)
      print "***PATH MAFFT: "+ path_mafft
      
      print "\tCleaning and removing pipes in file: " + path_mafft + "..."
      tempName=path_mafft+'~~~'
      input = open(path_mafft)
      output = open(tempName,'w')
      s=input.read()
      for couple in findreplace:
          outtext=s.replace(couple[0],couple[1])
          s=outtext
      output.write(outtext)
      output.close()
      input.close()
      os.rename(tempName,path_mafft) 
#task_output = DataSet(dataflow_tag, [Element(['VALIDATED_SEQUENCE'])])
#task.add_dataset(task_output)
#task.end()

