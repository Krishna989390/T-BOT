from logging import error
import discord
from discord import user
from discord.ext import commands

client = commands.Bot(command_prefix="#")

filtered_words = ["shit" , "poo" , "hagde"]

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()
            

    await client.process_commands(msg)

@client.event
async def on_command_error(ctx,error):
     if isinstance(error,commands.MissingPermissions):
         await ctx.send("You can't do that ;-;")
         await ctx.message.delete()
     elif isinstance(error,commands.MissingRequiredArgument):
         await ctx.send("Please enter all the required args.")
         await ctx.message.delete()
     else:
        raise error


@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
      await ctx.guild.unban(discord.Object(id=member))

@client.command()
async def hello(ctx):
    await ctx.send("Hi, @everyone Its me your T bot...")

@client.command(alases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit = amount)


@client.command(alases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member ,*,reason = "No reason provided"):
    try:
        await member.send("You have been kicked from the coding community, Because :" + reason)
    except:
        print("Can't send message to that user")
    await ctx.send(member.name+" has been kicked from the coding community, Because :" + reason)
    await member.kick(reason=reason)


@client.command(alases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member ,*,reason = "No reason provided"):
    try:
        await member.send("You have been banned from the coding community, Because :" + reason)
    except:
        print("Can't send message to that user")
    await ctx.send(member.name+" has been banned from the coding community, Because :" + reason)
    await member.ban(reason=reason)



@client.command(aliases=["m"])
@commands.has_permissions(kick_members=True)
async def mute(ctx , member : discord.Member):
    muted_role = ctx.guild.get_role(900026520368717845)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted ")



@client.command(aliases=["um"])
@commands.has_permissions(kick_members=True)
async def unmute(ctx , member : discord.Member):
    muted_role = ctx.guild.get_role(900026520368717845)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " has been unmuted ")


@client.command(aliases=['user' , 'info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx , member : discord.Member):
    embed = discord.Embed(title=member.name , description = member.mention , color =discord.Colour.green())
    embed.add_field(name="ID" , value = member.id , inline= True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url , text = f"Requested by {ctx.author.name}" )
    await ctx.send(embed=embed )





client.run("ODk5Njg1MjMzNTM0ODUzMTgx.YW2XKw.e0wRPdjInYKuHxl3gAoKMF_J9iM")