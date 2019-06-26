from InstagramAPI import InstagramAPI

instaObject = InstagramAPI("username", "password")

def findBadFriends():
    followers = []
    following = []
    for person in instaObject.getTotalSelfFollowers():
        followers.append(person.get("username"))
    for person in instaObject.getTotalSelfFollowings():
        following.append(person.get("username"))

    badFriends = set(following).difference(set(followers))
    print(badFriends)  


def main():
    instaObject.login()
    findBadFriends()

if __name__ == "__main__":
    main()
