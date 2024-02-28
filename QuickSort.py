import random
import timeit
import matplotlib.pyplot as plt

def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        while i <= j and array[i] <= pivot:
            i += 1
        while j >= i and array[j] >= pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[low], array[j] = array[j], array[low]
    return j

def quicksort(array, low, high):
    if low < high:
        pi_index = partition(array, low, high)
        quicksort(array, low, pi_index - 1)
        quicksort(array, pi_index + 1, high)

def random_pivot(array, low, high):
    if low < high:
        pi_index = random.randint(low, high)
        array[low], array[pi_index] = array[pi_index], array[low]
        pi_index = partition(array, low, high)
        random_pivot(array, low, pi_index - 1)
        random_pivot(array, pi_index + 1, high)

def generate_best_case_input(n):
    return [i for i in range(n)]

def generate_worst_case_input(n):
    return [i for i in range(n, 0, -1)]

def generate_average_case_input(n):
    return [random.randint(0, 1000) for _ in range(n)]

def benchmark_sorting_function(sort_func, input_generator, sizes, iterations=5):
    times = []
    for size in sizes:
        total_time = 0
        for _ in range(iterations):
            arr = input_generator(size)
            start_time = timeit.default_timer()
            sort_func(arr, 0, len(arr) - 1)
            end_time = timeit.default_timer()
            total_time += end_time - start_time
        avg_time = total_time / iterations
        times.append(avg_time)
    return times

input_array = [150,250,350,550,750]

best_case_times = benchmark_sorting_function(quicksort, generate_best_case_input, input_array)
worst_case_times = benchmark_sorting_function(quicksort, generate_worst_case_input, input_array)
average_case_times = benchmark_sorting_function(quicksort, generate_average_case_input, input_array)

plt.plot(input_array, best_case_times, label='Best Case')
plt.plot(input_array, worst_case_times, label='Worst Case')
plt.plot(input_array, average_case_times, label='Average Case')
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.title('Non-Random Pivot Quicksort Benchmark')
plt.legend()
plt.show()
