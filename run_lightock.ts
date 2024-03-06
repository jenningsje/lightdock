const { exec } = require('child_process');
const path = require('path');

function runNode(command) {
    // Run the Node.js file
    const nodeProcess = exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing the Node.js file: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
        }
        console.log(`Output: ${stdout}`);
    });
    
    nodeProcess.on('exit', (code) => {
        console.log(`Child process exited with code ${code}`);
    });}

const commands = [
    'node listen_to_front.ts', 
    'node /markov_modeules/stages/fetch_pdbs.ts', 
    'node /markov_modules/stages/lightdock_setup.ts', 
    'node /markov_modules/stages/lightdock_run.ts',
    'node /bin/generate_confs.ts']

for (let i = 0; i < commands.length; i++) {
    runNode(commands[i])
    console.log(`ran ${commands[i]} in js`)
}