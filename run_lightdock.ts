const { exec } = require('child_process');
const path = require('path');
const fetchpdbs = require('./markov_modules/stages/fetch_pdbs.ts')
const lightdock_setup = require('./markov_modules/stages/lightdock_setup.ts')