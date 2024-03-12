const fs = require('fs');
const axios = require('axios');

// Path to pdb file
const filePath = 'path/to/your/file.txt';

// URL where you want to send the POST request
const url = 'https://test1-ecru-mu.vercel.app/';

// Send file to front end
function executeProgram() {
    console.log('File has appeared or changed. Executing program...');
    // Send the POST request using Axios
    axios.post(url, pdbFile, {
        headers: {
            'Content-Type': 'application/octet-stream', // Set the content type to indicate a binary file
        }
    })
    .then(response => {
        console.log('Response:', response.data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Watch for changes in the pdb file
fs.watch(filePath, (eventType, filename) => {
    if (filename) {
        console.log(`Event type is: ${eventType}`);
        if (eventType === 'rename') {
            console.log('File has appeared or changed.');
            executeProgram();
        }
    } else {
        console.log('Filename not provided.');
    }
});

console.log(`Watching for changes in ${filePath}`);
