# instagram-watch-bot

Simple script that has functionality to give users an easy way to watch over their Instagram accounts.

---------------------

## Motivation

There are a few similar bots on Github. Unfortunately, most of these scripts only have options to
DO things, rather than just VIEW them. For example, some scripts will automatically unfollow users
who you follow but do not follow you back - in some cases, you may just want to view these profiles, 
rather than unfollow them immediately. This is especially true when it comes to following verified
accounts; chances are they do not follow you back, so these script would cause you to unfollow these
accounts. This script provides the read-only functionality that some other scripts lack.

---------------------

## Usage

```
python3 app.py <instagram_username> <instagram_password>
```

**After running this script, you will be presented with a prompt that looks like the following:**

```
1: List who you are following.
2: List who follows you.
3: List verified accounts that you follow.
4: List those who you follow but do not follow you back.
5: List those who follow you but you do not follow back.
6: List the like count and URL's of your posts that have recieved the most likes.
```

Choose an option and your results will be returned to your shell.

---------------------

## Outside Packages

Created using [this](https://github.com/LevPasha/Instagram-API-python) really cool package. It can be
installed by running: 

```
pip install InstagramAPI
```
