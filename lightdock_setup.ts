const { exec } = require('child_process');

// execute analyze.py
const cmd = "lgd_setup.py -s 1 -g 1000 prot1.pdb prot2.pdb --now --noh"

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
