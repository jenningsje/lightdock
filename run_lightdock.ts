const { exec } = require('child_process');
const path = require('path');
const fetchpdbs = require('./markov_modules/stages/fetch_pdbs.ts')

function RunCommand(cmd) {
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

const commands = [
    'node listen_to_front.ts', 
    'node /markov_modules/stages/fetch_pdbs.ts', 
    'node /markov_modules/stages/lightdock_setup.ts', 
    'node /markov_modules/stages/lightdock_run.ts',
    'node /bin/generate_confs.ts']

RunCommand(commands[1])