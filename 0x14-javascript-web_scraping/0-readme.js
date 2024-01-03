#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs').promises;

async function readFileAsync () {
  try {
    const data = await fs.readFile(args[0], 'utf-8');
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

readFileAsync();
