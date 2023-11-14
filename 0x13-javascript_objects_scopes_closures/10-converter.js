!#/usr/bin/node

exports.converter = function (base) {
  // Define a recursive helper function
  const convertRecursive = (number, result) => {
    if (number === 0) {
      return result;
    } else {
      // Calculate the remainder
      const remainder = number % base;
      
      // Recursive call with quotient and current result
      return convertRecursive(Math.floor(number / base), remainder.toString() + result);
    }
  };

  // Return the main function
  return function (number) {
    // Check if the input is a valid positive integer
    if (!Number.isInteger(number) || number < 0) {
      throw new Error("Input must be a non-negative integer.");
    }

    // Handle the special case when the input number is 0
    if (number === 0) {
      return "0";
    }

    // Call the recursive helper function with the initial result as an empty string
    return convertRecursive(number, "");
  };
};

