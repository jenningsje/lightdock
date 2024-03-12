const fs = require('fs');
import {PdbParser} from 'pdb-parser-js';

// Path to the file you want to watch
const file = fs.readFileSync('[pdb file path]', 'utf-8')

const parser = new PdbParser()

// Function to execute when the file changes
function executeProgram() {
    console.log('File has appeared or changed. Executing program...');
    //collect the json file and send to the viewer
    parser.collect(file.split('\n'))
    const pdb = parser.parse()
    const xhr = new XMLHttpRequest();
    //send post request to vercel
    xhr.open("POST", "https://test1-ecru-mu.vercel.app/");
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    //json to send to the server
    const body = JSON.stringify({
    userId: 1,
    title: pdb,
    completed: false
});
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 201) {
    console.log(JSON.parse(xhr.responseText));
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};
xhr.send(body);
}

// Watch for changes in the file
fs.watch(file, (eventType, filename) => {
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

console.log(`Watching for changes in ${file}`);
