#!/usr/bin/node
const args = process.argv;
const len = args.length;
if (len <= 3) {
  console.log(0);
} else {
  const arr = args.slice(2);
  const max = Math.max(...arr);
  const index = arr.indexOf(max.toString());
  arr.splice(index, 1);
  console.log(Math.max(...arr));
}
