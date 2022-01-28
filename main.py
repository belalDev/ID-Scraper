import discum 
token = "TOKENHERE" #  Your account token
guild_id = 'GUILD_ID_HERE' # The guild you wanna scrape id
channel_id = 'CHANNEL_ID_HERE' # get the id of a channel that most people can see like #rules etc
bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild_id, channel_id, keep=['username','discriminator'],startIndex=0, method='overlap',wait=1)
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()

with open('result.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        print(f'ID: {id}\n')
        file.write(f'{id}\n')
           