#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  console.log(parseInt(args[0]) + parseInt(args[1]));
}
add();
