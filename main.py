import time
import requests
import json


def main(i):
    v_i  = i
    API_KEY = ''
    BLOG_ID = ''  # Replace with your Blogger blog ID

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
        if v_i == 10 :
            return 0
        # Extract information about each post
        post = data['items'][v_i]
        post_title = post['title']
        post_url = post['url']

        url = "https://whin2.p.rapidapi.com/send"
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": '',
            "X-RapidAPI-Host": "whin2.p.rapidapi.com"}
        url = "https://whin2.p.rapidapi.com/send2group"
        querystring = {"gid": ""}
        requests.request("POST", url, json={"text": post_title + "\n" + post_url}, headers=headers, params=querystring)
        main(i+1)

    else:
        print('Error:', response.status_code)


main(2)
