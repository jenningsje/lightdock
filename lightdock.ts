const { exec } = require('child_process');

// execute analyze.py
const cmd1 = "lgd_setup.py -s 2 1zgx.pdb 253l.pdb --now"
const cmd2 = "lgd_run.py -s macro setup.json 1 -c 2 -l 0"
const cmd3 = "lgd_generate_conformations.py ../1zgx.pdb ../253l.pdb gso_1.out 1"

function executeCommand(cmd) {
	exec(cmd, (error, stdout, stderr) => {
	if (error) {
		console.log(`error: ${error.message}`);
	}
	if (stderr) {
		console.log(`stderr: ${stderr}`);
	}
	//console.log(`stdout: ${stdout}`);
	else {
		console.log(`stdout: ${stdout}`);
	}
	});
};

executeCommand(cmd1)
executeCommand(cmd2)
executeCommand(cmd3)