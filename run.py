import pandas as pd

# Load the CSV files
posts_df = pd.read_csv("posts.csv", delimiter=";")
comments_df = pd.read_csv("comments.csv", delimiter=";")

# Drop all empty rows
posts_df.dropna(inplace=True)
comments_df.dropna(inplace=True)

posts_ids = posts_df["Post Id"].unique()
for post_id in posts_ids:

    result = ""

    # Get the post title and text
    post_df = posts_df[posts_df["Post Id"] == post_id]
    post_title = post_df["Title"].values[0]
    post_text = post_df["Text"].values[0]

    result += f"POST ID: {post_id} / POST TITLE: {post_title}\n"
    result += "="*100
    result += f"\n{post_text}\n\n"
    result += "POST COMMENTS:\n"
    result += "="*100 + "\n"

    # Get the comments for the post
    post_data = comments_df[comments_df["Post ID"] == post_id]

    # Iterate over the comments for the post
    for _, comment in post_data.iterrows():
        comment_id = comment["Comment ID"]
        comment_upvotes = comment["Comment Upvotes"]
        subreddit = comment["Subredit"]
        comment_text = comment["Comment Text"]

        result += f"ID: {comment_id} # OF UPVOTES: {comment_upvotes} SUBREDDIT: {subreddit}\n"
        result += f"COMMENT TEXT: {comment_text}\n"
        result += "-"*100 + "\n"
    
    # Save the result to a file
    with open(f"posts/{post_id}.txt", "w") as f:
        f.write(result)

