import os
import subprocess
import logging
import time
from renew import *

logging.basicConfig(level=logging.INFO)

message_path = "../MarkovProprietary/pipelinestages/app/mount/output/message.txt"

from_front_end_path = "../MarkovProprietary/pipelinestages/app/mount/output/from_front_end.txt"

simulation_finished = "docking simulation finished..."

def messager(message):
    try:
        with open(message_path, "w") as m:
            m.write(message)
            print(message)
            time.sleep(5) 
    except:
        logging.error(f"message {' '.join(message)}")

def write_to_from_frontend(message):
    try:
        with open(from_front_end_path, "w") as m:
            m.write(message)
            print(message)
            time.sleep(5) 
    except:
        logging.error(f"message {' '.join(message)}")

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info(f"Command succeeded: {' '.join(command)}")
        logging.info(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {' '.join(command)}")
        logging.error(f"Error: {e.stderr}")

def simulator():
    # Set up simulation
    messager("setting up simulation...")
    run_command(["lgd_setup.py", "-s", "1", "-g", "200", "prot1.pdb", "prot2.pdb", "--now", "--noh"])
    if not os.path.exists("past_setup"):
        os.mkdir("past_setup")
    
    # Run simulation
    messager("running simulation...")
    run_command(["lgd_run.py", "-s", "scoring.conf", "setup.json", "10", "-c", "1"])
    if not os.path.exists("past_run"):
        os.mkdir("past_run")
    
    os.chdir("swarm_0")
    messager("generating conformations...")
    run_command(["lgd_generate_conformations.py", "../prot1.pdb", "../prot2.pdb", "gso_10.out", "1"])
    if not os.path.exists("generated_conformations"):
        os.mkdir("generated_conformations")

    run_command(["mv", "lightdock_0.pdb", "../../MarkovProprietary/pipelinestages/app/mount/output/lightdock_0.pdb"])

    with open("../../MarkovProprietary/pipelinestages/app/mount/output/message.txt", "w") as message:
        message.write(simulation_finished)
        logging.info(simulation_finished)
        time.sleep(5) 

    os.chdir("..")
    logging.info(os.getcwd())
    renew()