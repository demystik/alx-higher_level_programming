#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length <= 1) { console.log('0'); } else {
  console.log(args.sort(function (a, b) { return b - a; })[1]);
}
