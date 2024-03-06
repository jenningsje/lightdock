const { exec } = require('child_process');

// execute analyze.py
const cmd = "lgd_generate_conformations.py ../1zgx.pdb ../253l.pdb ../swarm_0/gso_0.out 1"

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

executeCommand(cmd)