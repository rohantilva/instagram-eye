from InstagramAPI import InstagramAPI
import sys

username, password, option = sys.argv[1], sys.argv[2], sys.argv[3]
instaObject = InstagramAPI(username, password)

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
