class User:
    def __init__(self, name):
        self.name = name

import random
import math
from util import Queue
class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return "WARNING: You cannot be friends with yourself"
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return "WARNING: Friendship already exists"
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically Adds the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    def populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        x = 0
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    
                
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend ID and the value is the path.
        """
        q  = Queue()
        q.enqueue([user_id]) 
        # I made a dictionary instead of set
        visited = {} 
        
        while q.size() > 0:
            cur = q.dequeue()
            last = cur[-1]
            visited[last] = cur
            for f in self.friendships[last]:
                if f not in visited:
                    new_path = cur + [f]
                    q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)