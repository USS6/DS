#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Structure for hash table entries
typedef struct {
    int key;
    int value;
} HashEntry;

// Hash function
int hashFunction(int key, int size) {
    return abs(key) % size;
}

// Function to find two numbers that add up to the target
void findTwoSum(int arr[], int size, int target) {
    // Create a hash table
    HashEntry *hashTable = (HashEntry *)calloc(size, sizeof(HashEntry));

    // Initialize hash table keys to INT_MIN to indicate unused entries
    for (int i = 0; i < size; i++) {
        hashTable[i].key = INT_MIN;
    }

    for (int i = 0; i < size; i++) {
        int complement = target - arr[i];
        int hashIndex = hashFunction(complement, size);

        // Check if the complement exists in the hash table
        if (hashTable[hashIndex].key != INT_MIN && hashTable[hashIndex].key == complement) {
            printf("Elements %d and %d add up to target %d\n", complement, arr[i], target);
            free(hashTable);
            return;
        }

        // Add the current element to the hash table
        hashIndex = hashFunction(arr[i], size);
        hashTable[hashIndex].key = arr[i];
        hashTable[hashIndex].value = i;
    }

    printf("No two elements add up to the target %d\n", target);
    free(hashTable);
}

int main() {
    int arr[] = {2, 7, 11, 15};
    int target = 9;
    int size = sizeof(arr) / sizeof(arr[0]);

    findTwoSum(arr, size, target);

    return 0;
}