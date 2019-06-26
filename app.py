from InstagramAPI import InstagramAPI
import sys, pprint

username, password, option = sys.argv[1], sys.argv[2], sys.argv[3]
instaObject = InstagramAPI(username, password)

def findBadFriends():
    followers = getFollowers()
    following = getFollowing()
    badFriends = set(following).difference(set(followers))
    return badFriends  

def findUnfollowingFollowers():
    followers = getFollowers()
    following = getFollowing()
    goodFriends = set(followers).difference(set(following))
    return goodFriends

def getFollowers():
    followers = []
    for person in instaObject.getTotalSelfFollowers():
        followers.append(person.get("username"))
    return followers

def getFollowing():
    following = []
    for person in instaObject.getTotalSelfFollowings():
        following.append(person.get("username"))
    return following

def getVerifiedFollowing():
    verified = []
    for person in instaObject.getTotalSelfFollowings():
        if person.get("is_verified"):
            verified.append(person.get("username"))
    return verified 
    
def main():
    instaObject.login()
    print(findUnfollowingFollowers())


if __name__ == "__main__":
    main()
