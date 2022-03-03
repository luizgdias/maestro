import configparser, os
from pathlib import Path
from extractConfigParam import *

print("++++++++++++++")

os.system('/home/luiz/PycharmProjects/MaestroOO/sources/remove_pipe.py -f ' + validation_input)
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mafft.py -f '+ alignment_input)
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mrbayes.py -f '+ alignment_input + " -nr "+ nruns + " -nc " + nchains + " -brn " +burnin)
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/remove_pipe.py -f File1023')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mafft.py -f Validation_output')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/model_generator.py -f file1024')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/read_seq.py -f file1024')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mrbayes.py -f fileConvertedAlignment -f fileEvolutiveModel -nr nruns {} -nc nchains {} -brn burnin {} -prt printfreq {} -ng ngen {} -rt rates_mrbayes {}nrunsnchainsburninprintfreqngenrates_mrbayes')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/remove_pipe.py -f File1023')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mafft.py -f Validation_output')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/model_generator.py -f file1024')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/read_seq.py -f file1024')
os.system('/home/luiz/PycharmProjects/MaestroOO/sources/mrbayes.py -f fileConvertedAlignment -f fileEvolutiveModel -nr nruns -nc nchains -brn burnin -prt printfreq -ng ngen -rt rates_mrbayesnrunsnchainsburninprintfreqngenrates_mrbayes')
