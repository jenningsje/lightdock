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
    "./bin/lgd_generate_conformations"
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


// Middleware to parse JSON request body
app.use(bodyParser.json());

// Endpoint to handle the click event from the frontend
app.post('https://markov-backend.internal.graydune-2d508ddb.southcentralus.azurecontainerapps.io/', (req, res) => {
    console.log('Click event received from the frontend!');
    // You can perform backend logic here
    res.send('Click event received successfully!');
    const fs = require('fs');

    // Read JSON file
    fs.readFile('input.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading JSON file:', err);
            return;
        }

        try {
            const jsonData = JSON.parse(data);
            const textContent = JSON.stringify(jsonData, null, 4); // Convert JSON to formatted text

            // Write to names
            fs.writeFile('../MarkovProprietary/pipelinestages/app/mount/input/names.txt', textContent, 'utf8', (err) => {
                if (err) {
                    console.error('Error writing to text file:', err);
                    return;
                }
                console.log('Data written to output.txt successfully.');
            });
        } catch (err) {
            console.error('Error parsing JSON:', err);
        }
    });

});

// Start the server
app.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
});

for (let i = 0; i < commands.length; i++) {
    executeCommand(commands[i])
}