import sys
sys.path.append('/Users/james/Desktop/file_cabinet/work/bioinformatics/github/Markov/MarkovProprietary/pipelinestages')
from fetch_from_mount import *
import subprocess
import os

os.chdir('../MarkovProprietary/pipelinestages/app/mount/input')
names = open("names.txt")
print("success")