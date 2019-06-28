from InstagramAPI import InstagramAPI
import sys

username, password = sys.argv[1], sys.argv[2]
instaObject = InstagramAPI(username, password)

def getBadFriends():
    followers = getFollowers()
    following = getFollowing()
    badFriends = set(following).difference(set(followers))
    return badFriends  

def getUnfollowingFollowers():
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

def getMostLikedPosts():
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
    liked_posts = ""
    for post in dic:
        liked_posts += "Likes: " + str(post[0]) + "\n"
        for i in range(len(post[1])):
            liked_posts += "Url " + str(i + 1) + ": " + str(post[1][i]) + "\n"
        liked_posts += "\n"
    return liked_posts


def main():
    options = {1: getFollowing,
           2: getFollowers,
           3: getVerifiedFollowing,
           4: getBadFriends,
           5: getUnfollowingFollowers,
           6: getMostLikedPosts}

    instaObject.login()
    #pprint.pprint(instaObject.getTotalSelfUserFeed()[0])
    choice = input("1: List who you are following.\n" + 
                   "2: List who follows you.\n" +
                   "3: List verified accounts that you follow.\n" + 
                   "4: List those who you follow but do not follow you back.\n" + 
                   "5: List those who follow you but you do not follow back.\n" + 
                   "6: List the like count and URL's of your posts that have recieved the most likes.\n\n" + 
                   "Choose an option: ")
    print("\n")
    print(options[int(choice)]())


if __name__ == "__main__":
    main()
