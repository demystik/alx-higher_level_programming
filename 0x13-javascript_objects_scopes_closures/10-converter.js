!#/usr/bin/node

exports.converter = function (base) {
  const convertRecursive = (number, result) => {
    if (number === 0) {
      return result;
    } else {
      const remainder = number % base;
      
      return convertRecursive(Math.floor(number / base), remainder.toString() + result);
    }
  };

  return function (number) {
    if (!Number.isInteger(number) || number < 0) {
      throw new Error("Input must be a non-negative integer.");
    }

    if (number === 0) {
      return "0";
    }

    return convertRecursive(number, "");
  };
};
