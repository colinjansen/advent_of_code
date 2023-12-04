package utils

import (
	"os"
	"strings"
)

// GetFileLines reads a file and returns its lines as a slice of strings.
func GetFileLines(path string) []string {
	content, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	return strings.Split(string(content), "\n")
}

// MapValues returns a slice of values from a map.
func MapValues[M ~map[K]V, K comparable, V any](m M) []V {
	r := make([]V, 0, len(m))
	for _, v := range m {
		r = append(r, v)
	}
	return r
}

// Reduce reduces a slice to a single value.
func Reduce[T, M any](s []T, f func(M, T) M, initValue M) M {
	acc := initValue
	for _, v := range s {
		acc = f(acc, v)
	}
	return acc
}
