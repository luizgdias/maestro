import configparser, os
from time import *
from pathlib import Path
from extractConfigParam import *
from time import *


print("++++++++++++++")


os.system('/home/luiz/PycharmProjects/MaestroOO/sources/remove_pipe.py -f File1023')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mafft.py -f Validation_output')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/model_generator.py -f file1024')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/read_seq.py -f file1024')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mrbayes.py -f fileConvertedAlignment -f fileEvolutiveModel -nr nruns -nc nchains -brn burnin -prt printfreq -ng ngen -rt rates_mrbayesnrunsnchainsburninprintfreqngenrates_mrbayes')
