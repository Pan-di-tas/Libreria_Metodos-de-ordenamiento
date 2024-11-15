# prueba_metodos_ordenamiento.py
from metodosDeOrdenamiento import Directos, Logaritmicos

def main():
    # Crear una lista de ejemplo
    lista = [45, 12, 89, 33, 22, 10, 76]

    print("Lista original:", lista)

    # Usar métodos de Directos
    print("\n--- Pruebas de Directos ---")
    resultado_burbuja = Directos.burbuja_sort(lista.copy())
    print("Ordenado con Burbuja Sort:", resultado_burbuja)

    resultado_insercion = Directos.insercion_sort(lista.copy())
    print("Ordenado con Inserción Sort:", resultado_insercion)

    resultado_seleccion = Directos.seleccion_sort(lista.copy())
    print("Ordenado con Selección Sort:", resultado_seleccion)

    # Usar métodos de Algoritmicos
    print("\n--- Pruebas de Algoritmicos ---")
    algoritmos = Logaritmicos()
    lista_algoritmos = lista.copy()  # Copiar la lista original para no modificarla

    # Quicksort
    print("\nEjecutando Quicksort:")
    resultado_quick = algoritmos.quicksort(lista_algoritmos.copy())
    print("Ordenado con Quicksort:", resultado_quick)

    # Radix Sort
    lista_radix = lista.copy()
    print("\nEjecutando Radix Sort:")
    algoritmos.radix_sort(lista_radix)
    print("Ordenado con Radix Sort:", lista_radix)

    # Heap Sort (Descendente)
    lista_heap = lista.copy()
    print("\nEjecutando Heap Sort (Descendente):")
    algoritmos.heapsort_descendente(lista_heap)
    print("Ordenado con Heap Sort (Descendente):", lista_heap)

    # Shell Sort
    lista_shell = lista.copy()
    print("\nEjecutando Shell Sort:")
    algoritmos.shell_sort(lista_shell)
    print("Ordenado con Shell Sort:", lista_shell)

if __name__ == "__main__":
    main()
