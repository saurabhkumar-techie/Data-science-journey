# Implement the Algorithm
# We'll create a function that:

# Finds all friends of a given user.
# Identifies mutual friends between non-friends.
# Ranks recommendations by the number of mutual friends.

import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def find_people_you_may_know(user_id, data):
    user_friends = {}
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])
    
    if user_id not in user_friends:
        return []
    
    direct_friends = user_friends[user_id]
    suggestions = {}
    
    for friend in direct_friends:
        # For all friends of friend
        for mutual in user_friends[friend]:
            # If mutual id is not the same user and not already a direct friend of user
            if mutual != user_id and mutual not in direct_friends:
                # Count mutual friends
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
    
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [user_id for user_id, _ in sorted_suggestions]

# Load data
data = load_data("massive_data.json")
user_id = 1  # Example: Finding suggestions for Amit
recommendations = find_people_you_may_know(user_id, data)
print(f"People You May Know for User {user_id}: {recommendations}")

# Expected Output:

# If Amit (ID: 1) and Sara (ID: 4) share Priya (ID: 2) as a mutual friend, the output might be
# People You May Know for User 1: [7, 8, 9, 10, 11, 12]