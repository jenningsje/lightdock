import os
import subprocess

# Define the directory where your Python script is located
script_directory = '../MarkovProprietary/pipelinestages'

# Change the current working directory to the script directory
os.chdir(script_directory)

# Execute the Python script
subprocess.run("python fetch_protein.py", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
