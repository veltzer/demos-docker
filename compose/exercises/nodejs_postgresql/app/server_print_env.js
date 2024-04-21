#!/usr/bin/env node

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function takeABreak(seconds) {
  console.log("Taking a short break...");
  await sleep(seconds * 1000); // Yield control briefly
  console.log("Back after the break!");
}

console.log(process.env);
takeABreak(3600);
