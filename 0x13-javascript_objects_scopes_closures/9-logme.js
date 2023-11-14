#!/usr/bin/node

let numOfTime = 0;
exports.logMe = function (item) {
  console.log(numOfTime + ': ' + item);
  numOfTime++;
};
