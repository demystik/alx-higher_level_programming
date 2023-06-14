#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number = number + 1;
  theFunction(number);
};
