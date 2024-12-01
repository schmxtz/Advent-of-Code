/* 
Input: List of integer pairs
Output: Sum of difference between lowest number pair, 2nd lowest number pair, ..., highest number pair
Example: 
3   4
4   3
2   5
1   3
3   9
3   3
Output: 2 + 1 + 0 + 1 + 2 + 5 = 11
*/

// Include fs module
const fs = require("fs");

// Read input data
const data = fs.readFileSync("./data/day1.txt", { encoding: "utf8", flag: "r" });
let left = [];
let right = [];
// Parse read data for processing
data.split("\r\n").forEach(element => {
    const pair = element.split(" ");
    left.push(parseInt(pair[0]));
    right.push(parseInt(pair[pair.length - 1]));
});

// Sort lists so that we can compare number pairs
left.sort();
right.sort();

let difference = 0;
for (let index = 0; index < left.length; index++) {
    difference += Math.abs(left[index] - right[index]);
}

console.log("Result: %d", difference);

// Part 2 <------------------------>
/* 
Input: List of integer pairs
Output: Sum of each number in left list with their count of occurences in the right list
Example: 
3   4
4   3
2   5
1   3
3   9
3   3
Output: (9 + 4 + 0 + 0 + 9 + 9) = 31
*/
let similarityIndex = 0;
let lastIndex = 0;
for (let index = 0; index < left.length; index++) {
    // Rewind for next loop search
    while (left[index] > right[lastIndex] && lastIndex > 0) {
        lastIndex--;
    }
    let count = 0;
    // Count occurences
    while (left[index] >= right[lastIndex]) {
        if (left[index] == right[lastIndex]) {
            count++;
        }
        lastIndex++;
    }
    similarityIndex += count * left[index];
}

console.log("SimilarityIndex: %d", similarityIndex);
