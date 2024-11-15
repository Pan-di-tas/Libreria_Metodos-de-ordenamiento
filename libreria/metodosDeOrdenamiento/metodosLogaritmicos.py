
class Logaritmicos:
    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    def radix_sort(self, arr):
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10

    def heapify_min(self, arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify_min(arr, n, smallest)

    def heapsort_descendente(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_min(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify_min(arr, i, 0)
        
        arr.reverse()

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        print(f"Ordenando con pivote {pivot}: {arr}")
        print(f"Menores que {pivot}: {left}")
        print(f"Iguales a {pivot}: {middle}")
        print(f"Mayores que {pivot}: {right}")
        
        return self.quicksort(left) + middle + self.quicksort(right)
