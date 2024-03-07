const fs = require('fs');
const axios = require('axios');

// Read the PDB file
const pdbFile = fs.readFileSync('your_pdb_file.pdb');

// URL where you want to send the POST request
const url = 'https://test1-ecru-mu.vercel.app/';



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
