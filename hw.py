import timeit
import random

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для тестування алгоритмів
def test_sorting_algorithm(algorithm, data):
    start_time = timeit.default_timer()
    algorithm(data)
    end_time = timeit.default_timer()
    return end_time - start_time

# Створення наборів даних для тестування
def create_data_sets():
    random_data = [random.randint(0, 1000) for _ in range(10000)]
    sorted_data = sorted(random_data)
    reverse_data = sorted_data[::-1]
    return random_data, sorted_data, reverse_data

# Тестування алгоритмів на різних наборах даних
def run_tests():
    random_data, sorted_data, reverse_data = create_data_sets()
    
    # Тестування merge sort
    merge_sort_time_random = test_sorting_algorithm(merge_sort, random_data.copy())
    merge_sort_time_sorted = test_sorting_algorithm(merge_sort, sorted_data.copy())
    merge_sort_time_reverse = test_sorting_algorithm(merge_sort, reverse_data.copy())
    
    # Тестування insertion sort
    insertion_sort_time_random = test_sorting_algorithm(insertion_sort, random_data.copy())
    insertion_sort_time_sorted = test_sorting_algorithm(insertion_sort, sorted_data.copy())
    insertion_sort_time_reverse = test_sorting_algorithm(insertion_sort, reverse_data.copy())
    
    # Тестування timsort
    timsort_time_random = test_sorting_algorithm(sorted, random_data.copy())
    timsort_time_sorted = test_sorting_algorithm(sorted, sorted_data.copy())
    timsort_time_reverse = test_sorting_algorithm(sorted, reverse_data.copy())
    
    results = {
        "Merge Sort": {
            "Random": merge_sort_time_random,
            "Sorted": merge_sort_time_sorted,
            "Reverse": merge_sort_time_reverse
        },
        "Insertion Sort": {
            "Random": insertion_sort_time_random,
            "Sorted": insertion_sort_time_sorted,
            "Reverse": insertion_sort_time_reverse
        },
        "Timsort": {
            "Random": timsort_time_random,
            "Sorted": timsort_time_sorted,
            "Reverse": timsort_time_reverse
        }
    }
    
    return results

# Запис результатів у файл readme.md
def write_results_to_readme(results):
    with open("README.md", "w") as f:
        f.write("# Порівняння алгоритмів сортування\n\n")
        f.write("## Результати тестування\n\n")
        
        for algorithm, times in results.items():
            f.write(f"### {algorithm}\n")
            f.write(f"- Випадкові дані: {times['Random']:.6f} секунд\n")
            f.write(f"- Відсортовані дані: {times['Sorted']:.6f} секунд\n")
            f.write(f"- Зворотно відсортовані дані: {times['Reverse']:.6f} секунд\n")
            f.write("\n")

        f.write("## Висновки\n\n")
        f.write("Результати тестування показали, що алгоритм Timsort, який використовується вбудованими функціями сортування Python, є найефективнішим серед розглянутих алгоритмів на всіх наборах даних. Це підтверджує теоретичні оцінки складності та ефективність поєднання сортування злиттям і сортування вставками в алгоритмі Timsort.\n")

# Основна функція
if __name__ == "__main__":
    results = run_tests()
    write_results_to_readme(results)
    print("Тестування завершено. Результати записані у файл README.md.")
