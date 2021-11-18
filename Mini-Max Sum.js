/*
HackerRank Algorithm
Finding min and max sum of a given array
*/

const arr = [1, 2, 3, 4, 5];
function miniMaxSum(arr) {
  let max = arr[0], min = arr[0], sum = 0;
  for (let i in arr) {
    if (max < arr[i]) max = arr[i];
    if (min > arr[i]) min = arr[i];
    sum += arr[i];
  }
  console.log(`${sum - max} ${sum - min}`);
}
miniMaxSum(arr);