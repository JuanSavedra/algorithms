package main

import "fmt"

func pesquisa_binaria(lista []int, item int) int {
	baixo := 0
	alto := len(lista) - 1

	for baixo <= alto {
		meio := (baixo + alto) / 2
		chute := lista[meio]

		if chute == item {
			return meio
		}

		if chute > item {
			alto = meio - 1
		} else {
			baixo = meio + 1
		}
	}

	return -1
}

func main() {
	var minha_lista = []int{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

	fmt.Printf("Resultado: %d\n", pesquisa_binaria(minha_lista, 13))
	fmt.Printf("Resultado para -1: %d\n", pesquisa_binaria(minha_lista, -1))
}
