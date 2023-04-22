package main

import "fmt"

func main() {
	// Define a dictionary
	dict_values := map[string]int{
		"Apple":   100,
		"Mangoes": 200,
		"Banana":  60,
	}

	// Get a slice of the keys from the dictionary
	slice := make([]string, 0, len(dict_values))
	for key := range dict_values {
		slice = append(slice, key)
	}
	fmt.Println("The dictionary is iterated as follows:")
	// Iterate through the keys and get the corresponding values
	for _, key := range slice {
		value := dict_values[key]
		fmt.Println(key, value)
	}
}