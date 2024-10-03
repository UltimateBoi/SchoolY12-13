import json
import random
import time
from concurrent.futures import ThreadPoolExecutor

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sorted_arrays(arr1, arr2):
    sorted_array = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1
    sorted_array.extend(arr1[i:])
    sorted_array.extend(arr2[j:])
    return sorted_array

def parallel_insertion_sort(arr, num_threads):
    chunk_size = len(arr) // num_threads
    chunks = [arr[i * chunk_size:(i + 1) * chunk_size] for i in range(num_threads)]
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        sorted_chunks = list(executor.map(insertion_sort, chunks))
    
    while len(sorted_chunks) > 1:
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            merged_chunks = list(executor.map(lambda x: merge_sorted_arrays(x[0], x[1]), zip(sorted_chunks[::2], sorted_chunks[1::2])))
        sorted_chunks = merged_chunks
    
    return sorted_chunks[0]

if __name__ == "__main__":
    # Generate a list of 100,000 randomly ordered numbers
    random_numbers = [random.randint(1, 1000000) for _ in range(100000)]
    
    # Save the unsorted numbers to unsorted_numbers.json
    with open("unsorted_numbers.json", "w") as f:
        json.dump(random_numbers, f)
    
    # Load the unsorted numbers from unsorted_numbers.json
    with open("unsorted_numbers.json", "r") as f:
        unsorted_numbers = json.load(f)
    
    # Sort the numbers using parallel insertion sort
    start_time = time.time()
    sorted_numbers_parallel = parallel_insertion_sort(unsorted_numbers.copy(), num_threads=8)
    end_time = time.time()
    parallel_sort_time = end_time - start_time
    
    # Output the time it took to sort the numbers
    print(f"Time taken to sort 100,000 numbers with parallel insertion sort: {parallel_sort_time} seconds")
    
    # Save the sorted numbers to sorted_numbers.json
    with open("sorted_numbers.json", "w") as f:
        json.dump(sorted_numbers_parallel, f)
