#!/usr/bin/node
const args = process.argv.slice(2);
function fact (num) {
  if (num < 0) { return (-1); }
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return num * fact(num - 1);
}
console.log(fact(Number(args[0])));
