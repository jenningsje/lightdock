const { exec } = require('child_process');

function executeCommand(cmd) {
	exec(cmd, (error, stdout, stderr) => {
		console.log(stdout);
    })
};

executeCommand("ls")