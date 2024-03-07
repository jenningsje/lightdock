const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const app = express();
const port = 3000;

// execute analyze.py
const commands = [
    "python Run_Markov.py",
    "lgd_setup.py -s 1 -g 1000 prot1.pdb prot2.pdb --now --noh",
    "lgd_run.py -s scoring.conf setup.json 1 -c 1",
    "./bin/lgd_generate_conformations.py"
]

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

for (let i = 0; i < commands.length; i++) {
    executeCommand(commands[i])
}