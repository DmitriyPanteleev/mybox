package main

import (
	"fmt"
	"sort"
	"strconv"
)

func brusselsChoice(n, mink, maxk int) []int {
	s := strconv.Itoa(n)
	results := make(map[int]bool)

	for start := 0; start < len(s); start++ {
		for end := start + 1; end <= len(s); end++ {
			// Подстрока s[start:end]
			length := end - start
			if length < mink || length > maxk {
				continue
			}
			subStr := s[start:end]
			val, err := strconv.Atoi(subStr)
			if err != nil || val <= 0 {
				continue
			}

			// Проверяем половину (если чётно)
			if val%2 == 0 {
				halfVal := val / 2
				newStr := s[:start] + strconv.Itoa(halfVal) + s[end:]
				newNum, err2 := strconv.Atoi(newStr)
				if err2 == nil && newNum > 0 {
					results[newNum] = true
				}
			}

			// Проверяем удвоение
			doubleVal := val * 2
			newStr := s[:start] + strconv.Itoa(doubleVal) + s[end:]
			newNum, err3 := strconv.Atoi(newStr)
			if err3 == nil && newNum > 0 {
				results[newNum] = true
			}
		}
	}

	// Превращаем множество в отсортированный список
	unique := make([]int, 0, len(results))
	for x := range results {
		unique = append(unique, x)
	}
	sort.Ints(unique)
	return unique
}

func main() {
	// Примеры из условия:
	fmt.Println(brusselsChoice(10, 2, 5))    // [5 20]
	fmt.Println(brusselsChoice(9, 1, 4))     // [18]
	fmt.Println(brusselsChoice(47, 1, 1))    // [27 87 414]
	fmt.Println(brusselsChoice(100, 84, 99)) // []
}
