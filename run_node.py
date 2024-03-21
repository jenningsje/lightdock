import subprocess

print("fetching pdbs")
subprocess.run("node fetch_pdbs.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("setting up lightdock")
subprocess.run("node lightdock_setup.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
