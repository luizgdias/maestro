import configparser, os
from time import *
from pathlib import Path
from extractConfigParam import *
from time import *


path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "conf.ini")

cfg = configparser.ConfigParser()
cfg.read(config_path)

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

print("++++++++++++++")


os.system('/home/luiz/PycharmProjects/MaestroOO/sources/remove_pipe.py -f ' + validation_input)
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mafft.py -f '+ alignment_input)
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/model_generator.py -f '+ modelgenerator_input)
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/read_seq.py -f '+ converter_input)
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mrbayes.py -f ' + tree_generator +' -f fileEvolutiveModel -nr nruns -nc nchains -brn burnin -prt printfreq -ng ngen -rt value_rates_mrbayes')
