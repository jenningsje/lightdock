import subprocess

commands = ["fetch_pdbs.ts, lightdock_setup.ts, lightdock_run.ts, ../generate_confs.ts"]

subprocess.run("node fetch_pdbs.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("past 1")
subprocess.run("node lightdock_setup.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("past 2")
subprocess.run("node lightdock_run.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("past 3")
subprocess.run("node ../generate_confs.ts", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("past 4")

for command in commands:
    print(command)
