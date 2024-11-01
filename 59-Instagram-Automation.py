from instabot import Bot
bot = Bot(max_likes_per_day=100, max_follows_per_day=50, max_messages_per_day=20)
bot.login(username="talhawkk", password="mangoman1288")
bot.follow('talhaabbasali')
# bot.upload_photo('photo1.jpg',caption="caption")
# bot.unfollow('talhawkk')
bot.send_message("hi gandu, this message sent to you by instabot made in python by talha dad",["fructoseofficial","az an 03","iamayyan18"])
followers=bot.get_user_followers("talhawkk")
for follower in followers:
    print(bot.get_user_info(follower))
following = bot.get_user_following("talhawkk")
for follow in following:
    print(bot.get_user_info(follow))
