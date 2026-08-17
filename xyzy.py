from pystyle import Colors, Colorate
import time
import discord
from discord.ext import commands
from zendaya import nuke, rename, evspam, delemj, delroles, crtroles, banall
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
guild = os.getenv("GUILD_ID")
author_id = os.getenv("OWNER_ID")


ping = "@everyone @here"
def cprint(text=""):
    print(Colorate.Horizontal(Colors.blue_to_cyan, text))


def cinput(msgg=""):
    return input(Colorate.Horizontal(Colors.blue_to_cyan, msgg))

menu = """
_______________________________________________

                 dev: discord/@asyncio.wait,
                 open-src | customisable nbot,
                 extensible,
                 
                 [i] help
                 
_______________________________________________
"""  
     
hlp = """
_______________________________________________

for support @asyncio.wait on discord      |

------------------ Command List ------------------ |

                      [i] nuke
                      [ii] rename
                      [iii] eventspam
                      [iv] delallemojis
                      [v] delallroles 
                      [vi] rolespam
                      [vii] banall
                      [0] exit                    


_______________________________________________

""" 
       
cprint(menu)
time.sleep(3)
cprint(hlp)

intents = discord.Intents.all()

relight = commands.Bot(
    command_prefix="relight",
    intents=intents,
    help_command=None
)

@relight.event
async def on_ready():
    cprint("")
    cprint("=" * 50)
    cprint("@asyncio.wait")
    cprint("=" * 50)
    cprint(f"Bot      : {relight.user}")
    cprint(f"Bot ID   : {relight.user.id}")
    cprint(f"Servers  : {len(relight.guilds)}")
    cprint("")
    cprint("SERVER INFORMATION")
    cprint("-" * 50)

    for guild in relight.guilds:
        me = guild.me

        cprint(f"Name : {guild.name}")
        cprint(f"ID   : {guild.id}")

        if me is not None:
            perms = me.guild_permissions

            enabled_perms = [
                name.replace("_", " ").title()
                for name, value in vars(perms).items()
                if isinstance(value, bool) and value
            ]

            cprint("Permissions:")

            for permission in enabled_perms:
                cprint(f"  - {permission}")
        else:
            cprint("Permissions: Unable to determine")

        cprint("-" * 50)


@relight.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    raise error

async def menu():
    while True:
        try:
            cmd_inp = int(cinput("enter: "))
        except ValueError:
            print("Enter a number.")
            continue

        if cmd_inp == 0:
            break

        elif cmd_inp == 1:
            await nuke(guild)

        elif cmd_inp == 2:
            await rename(guild)

        elif cmd_inp == 3:
            await evspam(guild)

        elif cmd_inp == 4:
            await delemj(guild)

        elif cmd_inp == 5:
            await delroles(guild)

        elif cmd_inp == 6:
            await crtroles(guild)

        elif cmd_inp == 7:
            await banall(guild, author_id)

        else:
            print("Invalid option.")


asyncio.run(menu())
relight.run(TOKEN)
 

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
