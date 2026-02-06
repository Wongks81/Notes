class Car:
    # Can take in input values to initate what should be object initial values be
    # If declare to take in values so when creating an Object of the class values will be needed
    def __init__(self, seats):
        self.seats = seats

# Object will be created with the value of the seats = 5
car = Car(5)

class User:
    # class constructor
    # All methods need to have a 'self' as input
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        # Can also declare default values
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(user_id="001", username="KS")
user2 = User(user_id="002", username="ABC")

print(user1.username)
user1.follow(user2)

print(user1.following)
print(user1.followers)