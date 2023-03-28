import { readFileSync } from 'fs';

let input = readFileSync('./input.txt').toString();
console.log(input);
input = input.split('\n');
console.log(input);

const testCaseNum = +input[0];
console.log('testCaseNum : ', testCaseNum);

for(let i = 1; i<= testCaseNum;++i){
    const arr = input[i].split(' ');

    let newArr = [];
    for (let i=0;i<arr.length;++i){
    newArr.push(+arr[i]);
    }

    console.log('arr : ', arr);
    console.log('newarr : ', newArr);
}