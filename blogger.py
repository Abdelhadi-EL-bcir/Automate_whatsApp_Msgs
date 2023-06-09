import requests
import json
import pywhatkit
import pyautogui
import time
# Set up the necessary credentials and parameters
API_KEY = 'AIzaSyARMci7Ly0Gct3GdvedC0RvEkIkJxPp8us'
BLOG_ID = '7386981156040281183'  # Replace with your Blogger blog ID

# Define the API endpoint
url = f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts'

# Set the query parameters for the API request
params = {
    'key': API_KEY,
    'fetchBodies': False,  # Set to True if you want to fetch the post content as well
    'maxResults': 5 # Number of posts to retrieve
}

# Send the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    data = json.loads(response.text)

    # Extract information about each post
    i = 42
    for post in data['items']:
        post_title = post['title']
        post_url = post['url']
        string = "Hello, World! How are you?"
        # Delete the substring "http://"
        print(str(post_title))
        start_index = post_url.find("http://")
        end_index = start_index + len("http://")
        new_url = post_url[:start_index] + post_url[end_index:]
        #pywhatkit.sendwhatmsg_to_group('Jx6531uBlAPDnTsY2IvrQk', post_title+"\n"+new_url, 16, i)
        pywhatkit.sendwhatmsg_to_group('Jx6531uBlAPDnTsY2IvrQk', str(post_title)+"\n"+new_url  , 23 , i )
        pyautogui.hotkey('enter')
        i = i + 1
else:
    print('Error:', response.status_code)