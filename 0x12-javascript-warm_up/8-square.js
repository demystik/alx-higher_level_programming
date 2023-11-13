#!/usr/bin/node

const args = process.argv.slice(2);
let output = '';
if (isNaN(args[0])) { console.log('Missing size'); } else {
  for (let i = 0; i < args[0]; i++) {
    for (let j = 0; j < args[0]; j++) {
      output += 'X';
    }
    console.log(output);
    output = '';
  }
}
