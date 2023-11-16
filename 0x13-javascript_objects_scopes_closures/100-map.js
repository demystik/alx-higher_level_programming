#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((num) => num * list.indexOf(num));
console.log(list);
console.log(newList);
