#!/usr/bin/node
const data = require('./101-data');

// Original dictionary
const originalDict = data.dict;

// New dictionary to store occurrences and corresponding user ids
const occurrencesDict = {};

// Iterate over the original dictionary
for (const userId in originalDict) {
  const occurrences = originalDict[userId];

  // Check if the occurrences value is already a key in the new dictionary
  if (occurrencesDict[occurrences]) {
    occurrencesDict[occurrences].push(userId);
  } else {
    occurrencesDict[occurrences] = [userId];
  }
}

// Print the new dictionary
console.log(occurrencesDict);
