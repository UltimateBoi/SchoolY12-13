package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	// Define the URL of the API endpoint
	url := "https://api.hypixel.net/v2/skyblock/auctions_ended"

	// Make the HTTP GET request
	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error making the request:", err)
		return
	}
	defer resp.Body.Close()

	// Read the response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading the response body:", err)
		return
	}

	// Unmarshal the JSON data to check for errors
	var jsonData interface{}
	if err := json.Unmarshal(body, &jsonData); err != nil {
		fmt.Println("Error unmarshalling JSON:", err)
		return
	}

	// Write the raw JSON data to a file
	if err := ioutil.WriteFile("auctions_ended.json", body, 0644); err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}

	fmt.Println("Data successfully written to auctions_ended.json")
}