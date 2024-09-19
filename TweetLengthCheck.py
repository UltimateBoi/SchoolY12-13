def is_valid_tweet(tweet):
    MAX_TWEET_LENGTH = 280  # Define the maximum tweet length
    return len(tweet) <= MAX_TWEET_LENGTH  # Check if the length of the tweet is within the allowed limit
