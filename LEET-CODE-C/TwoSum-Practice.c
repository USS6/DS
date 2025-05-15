// Two Sum Problem
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
// Example 1: Given nums = [2, 7, 11, 15], target = 9, return [0, 1].
// Example 2: Given nums = [3, 2, 4], target = 6, return [1, 2].
// CONCEPT: 2-POINTERS
// Time Complexity: O(n)
// Space Complexity: O(n)
// The code is written in C language

#include<stdio.h>
#include<stdlib.h>

typedef struct {
    int index;
    int value;
}hashtable;

void TwoSum(int arr[],int size,int target){
    // int i=0;
    hashtable* table=calloc(size,sizeof(hashtable)); 
    for(int i=0;i<size;i++){
        int diff = target-arr[i];

        if(table[abs(diff)%size].value!=0 && table[abs(diff)%size].value==diff){
            printf("Taget found with %d %d\n",arr[i],table[abs(diff)%size].value);
            free(table);
            return;
        }
        table[abs(arr[i])%size].index = i;
        table[abs(arr[i])%size].value = arr[i];
    }
}  

int main(){
    int arr[] = {4,8,3,3,9};
    int target = 7;
    int size = sizeof(arr)/sizeof(arr[0]);
    // Create a hash table and store based with a logic
    TwoSum(arr,size,target);
}