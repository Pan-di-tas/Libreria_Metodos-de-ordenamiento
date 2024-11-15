# metodos_directos.py

class Directos:
    @staticmethod
    def burbuja_sort(lista):
        """
        Ordena una lista en orden ascendente usando el método de ordenamiento de burbuja.
        
        Parámetros:
            lista (list): La lista de elementos que se desea ordenar.

        Retorna:
            list: La lista ordenada en orden ascendente.
        """
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:  # Intercambia si el actual es mayor que el siguiente
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    @staticmethod
    def insercion_sort(lista):
        """
        Ordena una lista en orden ascendente usando el método de ordenamiento por inserción.
        
        Parámetros:
            lista (list): La lista de elementos que se desea ordenar.

        Retorna:
            list: La lista ordenada en orden ascendente.
        """
        for i in range(1, len(lista)):
            actual = lista[i]
            j = i - 1

            while j >= 0 and lista[j] > actual:
                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = actual
        return lista

    @staticmethod
    def seleccion_sort(lista):
        """
        Ordena una lista en orden ascendente usando el método de ordenamiento por selección.
        
        Parámetros:
            lista (list): La lista de elementos que se desea ordenar.

        Retorna:
            list: La lista ordenada en orden ascendente.
        """
        for i in range(len(lista)):
            min_index = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[min_index]:
                    min_index = j

            # Intercambia el valor mínimo encontrado con el primer elemento del segmento
            lista[i], lista[min_index] = lista[min_index], lista[i]
        return lista
