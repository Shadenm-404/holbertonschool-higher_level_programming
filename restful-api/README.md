# RESTful API - Task 02

## Description
This task demonstrates how to consume a public REST API using Python and the requests library.

## Fetching Data from an API
The script sends a GET request to the JSONPlaceholder API to retrieve a list of posts.
The HTTP status code of the response is printed to confirm successful communication.

## Processing JSON Data
If the request is successful, the response data is parsed as JSON and the titles of all posts are printed.

## Saving Data to CSV
The fetched data is structured into a list of dictionaries containing id, title, and body.
This data is then written into a CSV file named posts.csv using Python's csv module.
