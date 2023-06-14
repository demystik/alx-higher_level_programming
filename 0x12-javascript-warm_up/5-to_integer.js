#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) { console.log('Not a number'); } else { console.log('My number: ' + parseInt(args[0])); }
