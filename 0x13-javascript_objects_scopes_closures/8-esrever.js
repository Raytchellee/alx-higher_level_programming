#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;

  for (let idx = 0; idx < len / 2; idx++) {
    [list[idx], list[len - idx - 1]] = [list[len - idx - 1], list[idx]];
  }

  return list;
};
