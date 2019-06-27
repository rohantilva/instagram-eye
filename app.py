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

def findMostLikedPosts():
    dic = {}
    for post in instaObject.getTotalSelfUserFeed():
        urls = []
        if post.get("carousel_media"): # if multiple pictures present
           for pic in post.get("carousel_media"):
                urls.append(pic["image_versions2"]["candidates"][0]["url"])    
        else:
            urls.append(post.get("image_versions2").get("candidates")[0].get("url"))
        likes = post.get("like_count")
        dic[likes] = urls
    dic = sorted(dic.items(), key=lambda x: x[0], reverse=True)
    for post in dic:
        print("Likes: " + str(post[0]))
        for i in range(len(post[1])):
            print("Url " + str(i + 1) + ": " + str(post[1][i]))
        print("\n")
    return dic

def main():
    instaObject.login()
    #pprint.pprint(instaObject.getTotalSelfUserFeed()[0])
    findMostLikedPosts()


if __name__ == "__main__":
    main()
