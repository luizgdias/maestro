import configparser, os
from pathlib import Path


cfg = configparser.ConfigParser()
cfg.read('conf.ini')

validation_input = cfg.get('VALIDATION', 'in_file')
alignment_input = cfg.get('ALIGNMENT', 'in_file')
modelgenerator_input = cfg.get('MODELGENERATOR', 'in_file')
converter_input = cfg.get('CONVERTER', 'in_file')

tree_generator = cfg.get('TREEGENERATOR', 'in_file')
nruns = cfg.get('TREEGENERATOR', 'nruns')
nchains = cfg.get('TREEGENERATOR', 'nchains')
burnin = cfg.get('TREEGENERATOR', 'burnin')
printfreq = cfg.get('TREEGENERATOR', 'printfreq')
ngen = cfg.get('TREEGENERATOR', 'ngen')
rates_mrbayes = cfg.get('TREEGENERATOR', 'rates_mrbayes')