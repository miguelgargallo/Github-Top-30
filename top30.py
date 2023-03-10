import requests

# Set the URL for the GitHub API endpoint
url = "https://api.github.com/search/repositories?q=stars:%3E1&sort=stars&order=desc"

# Send a request to the GitHub API and store the response
response = requests.get(url)

# Check the status code to make sure the request was successful
if response.status_code != 200:
    print("Error: Could not retrieve data from GitHub")
    exit(1)

# Parse the JSON data from the response
data = response.json()

# Open the top30.md file for writing
with open("top30.md", "w") as f:
    # Write the heading for the top 30 list
    f.write("# Top 30 Most Starred Projects on GitHub\n\n")

    # Iterate through the first 30 items in the data
    for i in range(30):
        # Check if the list has fewer than 30 items
        if i >= len(data["items"]):
            break
        # Get the current repository information
        repo = data["items"][i]
        # Write the repository name and number of stars to the file
        f.write(
            f"{i+1}. [{repo['name']}]({repo['html_url']}) - {repo['stargazers_count']} stars\n")

print("Top 30 most starred projects written to top30.md")
