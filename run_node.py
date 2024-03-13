import subprocess

subprocess.run("fetch_pdbs.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)