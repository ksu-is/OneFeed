# OneFeed
This application would be a social media aggregator. Its main purpose would be to combine all the feeds of your various social media platforms to keep it all in one place. The main audience for this would be the younger generations that have grown up so involved in social networking. A way to simplify and consolidate all of that information to one location would be a huge convenience and make leisure time that much easier. The user would interact with this by first downloading it, then once opened the user would be prompted to select the social media platforms that they would like to aggregate in OneFeed. After that they would enter the log in information to all of those platforms so that the app has the proper authorization to access the user’s individual feeds from each platform. At this point the users OneFeed would be fully operational. I think an important feature to add would be the ability to filter the feed by social platforms. For example, if the user has Facebook, Instagram, Twitter, Pinterest, etc they can select certain ones to combine or have certain lists. Like if they only wanted to see Facebook and twitter posts they could filter out Instagram and Pinterest. One more feature that I would like to see added is the ability to filter posts by media type. For example if you only wanted to see photos, or only words you could filter that by media type rather than the actual platform from which they originated. On  GetStream.io (https://getstream.io/build/social-networks/python/ ) I found some really informative tutorial on how to build a social media feed (or live feed in general) using python. 

# Requirements
- Install Python to run the program
- A Github account to properly communicate and submit the assignment

# Examples
- (https://getstream.io/build/social-networks/python/ )
- https://Twitter.com
- Instagram

# Sample Coding
- Below is code that I am going to start with and try after I receive an API key if one is made available to me through this site.

$ pip install stream-python
- Initialize the client with your api key and secret
import stream
client = stream.connect('YOUR_API_KEY', 'API_KEY_SECRET')
- For the feed group 'user' and user id 'eric' get the feed
eric_feed = client.feed('user', 'eric')
- Add the activity to the feed
eric_feed.add_activity({'actor': 'eric', 'verb': 'tweet', 'object': 1, 'tweet': 'Hello world'})

# Contributing
- I will be working alone, but contributions would always be appreciated!
- Fork it and then submit a pull request to help, if you choose to

# Clone
- To clone this repository to your computer use https://github.com/maverickjones21/IS3020/

# License
- We are using MIT license for this program
- Copyright 2019 IS Coding @ KSU

