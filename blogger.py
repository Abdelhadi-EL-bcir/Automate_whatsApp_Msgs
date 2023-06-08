import requests
import json

# Set up the necessary credentials and parameters
API_KEY = 'AIzaSyARMci7Ly0Gct3GdvedC0RvEkIkJxPp8us'
BLOG_ID = '7386981156040281183'  # Replace with your Blogger blog ID

# Define the API endpoint
url = f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts'

# Set the query parameters for the API request
params = {
    'key': API_KEY,
    'fetchBodies': False,  # Set to True if you want to fetch the post content as well
    'maxResults': 10  # Number of posts to retrieve
}

# Send the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    data = json.loads(response.text)

    # Extract information about each post
    for post in data['items']:
        post_id = post['id']
        post_title = post['title']
        post_published = post['published']
        post_updated = post['updated']
        # Add more attributes as per your requirement

        # Print the information
        print('Post ID:', post_id)
        print('Title:', post_title)
        print('Published:', post_published)
        print('Updated:', post_updated)
        print('---')

else:
    print('Error:', response.status_code)