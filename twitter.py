import matplotlib.pyplot as plt
import random
from datetime import datetime

print("Twitter Data Visualization Script")
print("Creating fake Twitter data...")

usernames = []
tweet_texts = []
likes = []
retweets = []
hours = []

example_users = ["alice_codes", "bob_learns", "charlie_data", "diana_python", 
                 "eve_student", "frank_tech", "grace_ai", "henry_dev"]

example_tweets = [
    "Just learned Python! #coding",
    "Data visualization is so cool!",
    "My first program works!",
    "University life is amazing!",
    "Love learning new things!",
    "Python is easier than I thought!",
    "Just made my first chart!",
    "Programming is fun!"
]

number_of_tweets = 50

print(f"Creating {number_of_tweets} fake tweets...")

for i in range(number_of_tweets):
    random_user = random.choice(example_users)
    usernames.append(random_user)
    
    random_tweet = random.choice(example_tweets)
    tweet_texts.append(random_tweet)
    
    random_likes = random.randint(1, 100)
    likes.append(random_likes)
    
    random_retweets = random.randint(0, 50)
    retweets.append(random_retweets)
    
    random_hour = random.randint(0, 23)
    hours.append(random_hour)

print("Fake data created successfully!")
print(f"Generated {len(usernames)} tweets")

print("First 3 tweets:")
for i in range(3):
    print(f"Tweet {i+1}: @{usernames[i]} said '{tweet_texts[i]}' and got {likes[i]} likes")

plt.figure(figsize=(10, 6))
plt.hist(likes, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Likes Distribution')
plt.xlabel('Number of Likes')
plt.ylabel('Number of Tweets')
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(likes, retweets, color='pink', alpha=0.6, s=50)
plt.title('Likes vs Retweets')
plt.xlabel('Number of Likes')
plt.ylabel('Number of Retweets')
plt.grid(True, alpha=0.3)
plt.show()

tweets_per_hour = [0] * 24

for hour in hours:
    tweets_per_hour[hour] = tweets_per_hour[hour] + 1

hour_labels = list(range(24))

plt.figure(figsize=(12, 6))
plt.bar(hour_labels, tweets_per_hour, color='lightgreen', edgecolor='black')
plt.title('Tweet Activity by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Tweets')
plt.grid(True, alpha=0.3)
plt.show()

user_tweet_count = {}

for user in usernames:
    if user in user_tweet_count:
        user_tweet_count[user] = user_tweet_count[user] + 1
    else:
        user_tweet_count[user] = 1

print("Tweet counts by user:")
for user, count in user_tweet_count.items():
    print(f"@{user}: {count} tweets")

user_names = list(user_tweet_count.keys())
tweet_counts = list(user_tweet_count.values())

plt.figure(figsize=(12, 6))
plt.bar(user_names, tweet_counts, color='orange', edgecolor='black')
plt.title('Most Active Twitter Users')
plt.xlabel('Username')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.show()

total_likes = sum(likes)
print(f"Total likes across all tweets: {total_likes}")

average_likes = total_likes / len(likes)
print(f"Average likes per tweet: {average_likes:.1f}")

max_likes = max(likes)
max_likes_index = likes.index(max_likes)
print(f"Most liked tweet: '{tweet_texts[max_likes_index]}' by @{usernames[max_likes_index]} with {max_likes} likes")

max_retweets = max(retweets)
max_retweets_index = retweets.index(max_retweets)
print(f"Most retweeted: '{tweet_texts[max_retweets_index]}' by @{usernames[max_retweets_index]} with {max_retweets} retweets")

low_engagement = 0
medium_engagement = 0
high_engagement = 0

for like_count in likes:
    if like_count <= 30:
        low_engagement = low_engagement + 1
    elif like_count <= 60:
        medium_engagement = medium_engagement + 1
    else:
        high_engagement = high_engagement + 1

engagement_labels = ['Low (0-30 likes)', 'Medium (31-60 likes)', 'High (61+ likes)']
engagement_sizes = [low_engagement, medium_engagement, high_engagement]
colors = ['lightcoral', 'lightyellow', 'lightgreen']

plt.figure(figsize=(8, 8))
plt.pie(engagement_sizes, labels=engagement_labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Tweet Engagement Levels')
plt.show()

print("Data visualization complete!")
print("Charts created:")
print("1. Likes distribution histogram")
print("2. Likes vs retweets scatter plot") 
print("3. Tweet activity by hour bar chart")
print("4. Most active users bar chart")
print("5. Engagement levels pie chart")