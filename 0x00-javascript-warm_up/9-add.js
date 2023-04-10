#!/usr/bin/node
function add (a, b) {
  if (a === b) {
    return 3 * (a + b);
  } else {
    return (a + b);
  }
}
console.log(add(10, 20));
console.log(add(10, 10));
