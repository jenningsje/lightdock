import subprocess

print("fetching pdbs")
subprocess.run("node fetch_pdbs.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("setting up lightdock")
subprocess.run("node lightdock_setup.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("running lightdock")
subprocess.run("node lightdock_run.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("fetching conformation")
subprocess.run("node ./bin/generate_confs.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("cleaning directory")
subprocess.run("rm *.pdb")