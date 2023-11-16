#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const content1 = fs.readFileSync(args[0], 'utf8');
const content2 = fs.readFileSync(args[1], 'utf8');

const concatContent = content1 + content2;

fs.writeFileSync(args[2], concatContent, 'utf8');
