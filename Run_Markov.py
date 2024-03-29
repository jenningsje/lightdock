import sys
sys.path.append('../MarkovProprietary/pipelinestages')
from fetch_from_mount import *
import os
import shutil

os.chdir('../MarkovProprietary/pipelinestages/app/mount/input')
names = open("names.txt")
print("success")

names_lines = names.readlines()
names.close()
names1 = names_lines[0]
names2 = names_lines[1]

os.chdir('../../..')

# fetch name of protein 1
PDB_ID = search_pdb_by_protein_name(names1)
# fetch file path of protein 1
prot1_file_path = cifDownload(PDB_ID)
# retrieve the name of protein 1
prot1_base_name = os.path.basename(prot1_file_path)
# rename protein 1
prot1_new_name = os.rename(prot1_file_path, "prot1.pdb")
shutil.move("prot1.pdb", "../../lightdock")

# fetch name of protein 2
PDB_ID = search_pdb_by_protein_name(names2)
# fetch file path of protein 2
prot1_file_path = cifDownload(PDB_ID)
# retrieve the name of protein 2
prot2_base_name = os.path.basename(prot1_file_path)
# rename protein 2
prot2_new_name = os.rename(prot1_file_path, "prot2.pdb")
shutil.move("prot2.pdb", "../../lightdock")