import sys, shutil, time, subprocess, logging, os
sys.path.append('../MarkovProprietary/pipelinestages')
sys.path.append('..')
from gemmi import *
from fetch_from_mount import *
from fetch_from_alphafold import *
from fetch_protein import *
from simulate import *

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

logger = logging.getLogger(__name__)

from_alphafold = "file not available on the protein databank fetching file from the alphafold databank instead..."
from_pdb = "fetching from the pdb..."
simulation_finished = "docking simulation finished..."

def Markov():
    while True:

        try:

            logging.info(f"current directoy is: {os.getcwd()}")

            with open('../output/from_front_end.txt', 'w'):
                pass

            # fetch the current signal from the front end
            from_front_end_size = os.path.getsize("../output/from_front_end.txt")

            if from_front_end_size == 0:
                with open("../output/message.txt", "w") as message:
                    message.write("fetch the next two proteins...")
                    logger.info("fetch the next two proteins...")
                    
                    time.sleep(5) 

            # retrieve the size of file
            open("names.txt", "w")
            file_size = os.path.getsize("names.txt")
        
            # while the size of the file is zero wait for user input
            while (file_size == 0):
                # fetch user input
                names = open("names.txt")
                names_lines = names.readlines()
                file_size = os.path.getsize("names.txt")
                logger.info("no user input")
                time.sleep(5)

            # fetch user input
            names = open("names.txt")
            names_lines = names.readlines()
            logger.info(names_lines[0])

            # fetch the first protein if present otherwise tell the user to try another query
            fetch_protein(names_lines[0], "../../../../../lightdock/prot1.pdb")
            logger.info("current working directory:" + os.getcwd())

            # erase the data from names.txt
            logger.info("test")
            with open("names.txt", "w"):
                pass

            # fetch the current signal from the front end
            from_front_end = open("../output/from_front_end.txt")
            from_front_end_lines = from_front_end.readlines()

            # wait for signal from front end to arrive to the backend
            while from_front_end_lines[0] not in (from_alphafold, from_pdb):
                logger.info(from_front_end_lines[0])
                logger.info(from_pdb)
                logger.info("waiting for signal from front end...")
                from_front_end = open("../output/from_front_end.txt")
                from_front_end_lines = from_front_end.readlines()
                val = from_front_end_lines[0] != (from_alphafold or from_pdb)
                logger.info(val)
                time.sleep(5)

                # delete names.txt file if present
                if os.path.isfile("names.txt"):
                    os.remove("names.txt")

                # if a bad query was made then allow the user to try another query, this will repeat until a protein is obtained
                if from_front_end_lines[0] == "that protein does not exist in the protein databank or the alphafold databank, please try another query":
                    logger.info("inside if statement")

                    # fetch user input and create an empty names.txt file
                    with open("names.txt", "w") as names:
                        # read the lines of names.txt
                        names_lines = names.readlines()

                    # get the size of the names.txt file
                    file_size = os.path.getsize("names.txt")
                
                    # while the size of the file is zero wait for user input
                    while (file_size == 0):
                        # fetch user input
                        names = open("names.txt")
                        names_lines = names.readlines()
                        file_size = os.path.getsize("names.txt")
                        logger.info("no user input")
                        time.sleep(5)

                    # fetch user input
                    names = open("names.txt")
                    names_lines = names.readlines()
                    logger.info(names_lines[0])
                    fetch_protein(names_lines[0], "../../../../../lightdock/prot1.pdb")
                time.sleep(5) 

            with open("../output/from_front_end.txt"):
                pass

            # fetch user input and create an empty names.txt file
            with open("names.txt", "a+") as names:
                # read the lines of names.txt
                names_lines = names.readlines()
                time.sleep(5) 
            
            # check the size of the file again
            new_file_size = os.path.getsize("names.txt")

            # erase the data from the message
            with open("../output/message.txt", "w") as message:
                message.write("fetch the next protein...")
                logger.info("fetch the next protein...")
                time.sleep(5) 

            # while the size of the file is zero wait for user input
            while (new_file_size == 0):
                # fetch user input
                names = open("names.txt")
                names_lines = names.readlines()
                new_file_size = os.path.getsize("names.txt")
                logger.info("no user input")
                time.sleep(5)

            # fetch user input
            names = open("names.txt")
            names_lines = names.readlines()
            logger.info(names_lines[0])
            logger.info("end of for loop")

            fetch_protein(names_lines[0], "../../../../../lightdock/prot2.pdb")

            # erase the data from names.txt
            logger.info("test")
            with open("names.txt", "w"):
                pass

            # fetch the current signal from the front end
            from_front_end = open("../output/from_front_end.txt")
            from_front_end_lines = from_front_end.readlines()

            while len(from_front_end_lines) == 0:
                logger.info("test")
                time.sleep(5) 

            # wait for signal from front end to arrive to the backend
            while from_front_end_lines[0] not in (from_alphafold, from_pdb):
                logger.info(from_front_end_lines[0])
                logger.info(from_pdb)
                logger.info("waiting for signal from front end...")
                from_front_end = open("../output/from_front_end.txt")
                from_front_end_lines = from_front_end.readlines()
                val = from_front_end_lines[0] != (from_alphafold or from_pdb)
                print(val)
                time.sleep(5)

                # delete names.txt file if present
                if os.path.isfile("names.txt"):
                    os.remove("names.txt")

                # if a bad query was made then allow the user to try another query, this will repeat until a protein is obtained
                if from_front_end_lines[0] == "that protein does not exist in the protein databank or the alphafold databank, please try another query":
                    logger.info("inside if statement")

                    # fetch user input and create an empty names.txt file
                    with open("names.txt", "a+") as names:
                        # read the lines of names.txt
                        names_lines = names.readlines()
                        time.sleep(5)

                    # get the size of the names.txt file
                    file_size = os.path.getsize("names.txt")
                
                    # while the size of the file is zero wait for user input
                    while (file_size == 0):
                        # fetch user input
                        names = open("names.txt")
                        names_lines = names.readlines()
                        file_size = os.path.getsize("names.txt")
                        logger.info("no user input")
                        time.sleep(5)

                    # fetch user input
                    names = open("names.txt")
                    names_lines = names.readlines()
                    logger.info(names_lines[0])
                    fetch_protein(names_lines[0], "../../../../../lightdock/prot2.pdb")

                time.sleep(5) 

            with open("../output/message.txt", "w") as message:
                message.write("docking simulator ready...")
                logger.info("docking simulator ready...")
                time.sleep(5) 

            os.chdir("../../../../../lightdock")
            time.sleep(5)
            
            while not os.path.isfile("../MarkovProprietary/pipelinestages/app/mount/input/ping.json"):
                time.sleep(5)

            simulator()

            logging.info(f"current working directory: {os.getcwd()} changing to /app/mount/input")
            os.chdir("../MarkovProprietary/pipelinestages/app/mount/input")

            logging.info(f"current working directory: {os.getcwd()} attempting open from_front_end.txt")
            from_front_end = open("../output/from_front_end.txt")
            from_front_end_lines = from_front_end.readlines()

            while from_front_end_lines[0] != simulation_finished:
                from_front_end = open("../output/from_front_end.txt")
                from_front_end_lines = from_front_end.readlines()
                logging.info(f"not past while loop, front_front_end_lines: {from_front_end_lines[0]}")
                time.sleep(1)

            logging.info(f"past while loop, front_front_end_lines: {from_front_end_lines[0]}")

            logging.info(f"current working directory before swiching to input diretory {os.getcwd()}")

        except Exception as e:
            # Log the exception and continue the loop
            logger.error(f"Error occurred: {e}", exc_info=True)
            time.sleep(5)

if __name__ == "__main__":
    Markov()