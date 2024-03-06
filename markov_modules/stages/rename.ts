var fs = require('fs');
fs.rename('/path/to/Afghanistan.png', '/path/to/AF.png', function(err) {
    if ( err ) console.log('ERROR: ' + err);
});