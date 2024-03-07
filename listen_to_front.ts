const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

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

