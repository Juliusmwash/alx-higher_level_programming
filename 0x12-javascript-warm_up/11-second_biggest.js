#!/usr/bin/node
const numArgs = process.argv;
const argsLen = numArgs.length;

if (argsLen === 2 || argsLen === 3) {
  console.log('0');
} else {
  let bigNum = parseInt(numArgs[2]);
  let secBigNum = parseInt(numArgs[2]);
  let i = 2; let tmpNum;
  for (; i < argsLen; i++) {
    tmpNum = parseInt(numArgs[i]);
    if (tmpNum > bigNum) {
      bigNum = tmpNum;
    }
  } for (i = 2; i < argsLen; i++) {
    tmpNum = parseInt(numArgs[i]);
    if (tmpNum < bigNum && secBigNum < tmpNum) {
      secBigNum = tmpNum;
    }
  }
  console.log(secBigNum);
}
