#! /usr/bin/env python

#TITULO             : RAxML: Parametros para a execucao de RAxML
#AUTOR              : Kary Soriano
#DATA               : 03/11/2008
#DIFICULDADE        : 1
# ==============================================================================
# Objetivo do script: Executado do myscript_nucl.py
#                     Executa Parametros 
# ==============================================================================
# Data da ultima alteracao do script: 	03/11/2008
# ==============================================================================
#-------------------------------------------------------------------------------
# declarando os modulos a usar 
#-------------------------------------------------------------------------------
import os, re
#-------------------------------------------------------------------------------
def paramModuleRaxml(dirin, model, rates_raxml_nucl, bootstrap, nb_categ,):
  btp = str(bootstrap)
  mod = str(model)
  nbc = str(nb_categ)
  rat = str(rates_raxml_nucl)
  model = mod + rat

  #------------------------------------------------------------
  # Executando Parametros do Raxml 
  #------------------------------------------------------------
  #1.- RAXML: Maximum Likelihood: Parameter status
  # Trabalhando com o diretorio script onde esta o raxml.conf 
  for f in os.listdir(dirin):
    if f.endswith('_phy'):                                                    
      phylip = f
      print "Executing RAxML:\n"
  #2.- RAXML: Estimating a Single Maximum-Likelihood Tree from Protein Sequences
      os.chdir(dirin)
      cmd_raxml_s = "raxmlHPC -s " + phylip + " -n " + phylip + "_raxml_tree1.singleTree -c " + nbc + " -f d -m " + model # + " -o " + ">SceRH"
      handle_s = os.popen(cmd_raxml_s, 'r', 1)
      for line_s in handle_s:
        print line_s,
      handle_s.close()
  #3.- RAXML: Estimating a Set of Non-Parametric Bootstrap Trees
      ###os.chdir(dirin)
      #cmd_raxml_b = "raxmlHPC -s " + phylip + " -n " + phylip + ".raxml -c 4 -f d -m " + modelMB + " -o " + ">SceRH -b 234534251 -N 100"
      cmd_raxml_b = "raxmlHPC -s " + phylip + " -n " + phylip + "_tree2.raxml -c " + nbc + " -f d -m " + model + " -b 234534251 -N " + btp
      handle_b = os.popen(cmd_raxml_b, 'r', 1)
      for line_b in handle_b:
        print line_b,
      handle_b.close()
  #4.- RAXML: Projecting Bootstrap Confidence Values onto ML Tree
      ###os.chdir(dirin)
      #cmd_mb_p = "ls -lh" 
      cmd_raxml_c = "raxmlHPC -f b -m " + model + " -c " + nbc + " -s " + phylip + " -z " + "RAxML_bootstrap." + phylip + "_tree2.raxml -t RAxML_bestTree." + phylip + "_raxml_tree1.singleTree -n " + phylip + "_tree3.BS_TREE"
      handle_c = os.popen(cmd_raxml_c, 'r', 1)
      for line_c in handle_c:
        print line_c,
      handle_c.close()
  
  print 'The execution has been finished with sucess'
  
  ###
  ###
  ###
  ###
  ####2.- RAXML: Maximum Likelihood: Execution status
  ###    os.chdir(dirin)
  ###    #cmd_mb_p = "ls -lh" 
  ###    cmd_mb_p = "raxmlHPC -s " + phylip + " -n " + phylip + "_raxml-out -m " + modelMB + " -o " + "gi_6812406" + " -b 123476 -# 100"
  ###    handle_p = os.popen(cmd_mb_p, 'r', 1)
  ###    for line_p in handle_p:
  ###      print line_p,
  ###    handle_p.close()
  ###
  ###print 'The execution has been finished with sucess'
  
#------------------------------------------------------------
 
#raxmlHPC -s rh_nucl.mafft_phy -n rh_nucl_phy_raxml-out -m GTRCAT -o gi_6812406 -b 123476 -# 100

#1.- Alignment Error Checking
#In case that RAxML detects Identical Sequences and/or Undetermined Columns and was executed,
#e.g., with -n alignmentName it will automatically write an alignment file called alignmentName.reduced
#with Identical Sequences and/or Undetermined Columns removed. If this is detected for a multiple model
#analysis a respective model file modelFileName.reduced will also be written. In case RAxML encounters
#identical sequence names or undetermined sequences or illegal characters in taxon names it will exit with
#an error and you will have to fix your alignment.
#2.-      Program Options
#raxmlHPC[-MPI|-PTHREADS] -s sequenceFileName
#                         -n outputFileName
#                         -m substitutionModel
#                         [-a weightFileName]
#                         [-b bootstrapRandomNumberSeed]
#                         [-c numberOfCategories]
#                         [-d]
#                         [-e likelihoodEpsilon]
#                         [-E excludeFileName]
#                         [-f a|b|c|d|e|g|h|i|j|m|n|o|p|s|t|w|x]
#                         [-g groupingFileName]
#                         [-h]
#                         [-i initialRearrangementSetting]
#                                             6
#[-j]
#[-k]
#[-l sequenceSimilarityThreshold]
#[-L sequenceSimilarityThreshold]
#[-M]
#[-o outGroupName1[,outGroupName2[,...]]]
#[-p parsimonyRandomSeed]
#[-P proteinModel]
#[-q multipleModelFileName]
#[-r binaryConstraintTree]
#[-t userStartingTree]
#[-T numberOfThreads]
#[-u multiBootstrapSearches]
#[-v]
#[-w workingDirectory]
#[-x rapidBootstrapRandomNumberSeed]
#[-y]
#[-z multipleTreesFile]
##[-#|-N numberOfRuns]

#3.-       -# numberOfRuns
#Specifies the number of alternative runs on distinct starting trees. E.g. if
#-# 10 is specified RAxML will compute 10 distinct ML trees starting from
#10 distinct randomized maximum parsimony starting trees. In combination
#with the -b option, this will invoke a multiple bootstrap analysis

#4.-   -o outgroupName(s)
#Specify the name/names of the outgroup taxa, e.g.,-o Mouse or -o Mouse,Rat. Dont leave spaces between
#the taxon names in the list! If there is more than one outgroup a check for monophyly will be performed. If
#the outgroups are not monophyletic the tree will be rooted at the first outgroup in the list and a respective
#warning will be printed.
#Example: raxmlHPC -s alg -m GTRGAMMA -o Rat,Mouse -n TEST
