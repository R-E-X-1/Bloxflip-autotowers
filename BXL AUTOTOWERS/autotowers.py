import discord
from discord import app_commands 
import bloxflip as bf
from random import randint

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync() 
            self.synced = True
        print(f"Logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'auto_towers', description='auto towers difficulty easy, normal, hard')
async def self(interaction: discord.Interaction, difficulty : str, bet_amount : int, click_amount : int, auth_token : str):
    if difficulty == 'easy' or difficulty == 'normal' or difficulty == 'hard':
        pass
    else:
        em = discord.Embed(title='Invalid gamemode', color=0xff0000)
        await interaction.response.send_message(embed=em)
        return 0
    try:
        bf.Login(a=auth_token)
    except:
        em = discord.Embed(title='Invalid auth provided', color=0xff0000)
        await interaction.response.send_message(embed=em)
        return 0

    try:
        balance = int(bf.Currency.Balance(auth=auth_token))
        bf.Towers.Create(betamount=bet_amount, difficulty=difficulty, auth=auth_token)
        em = discord.Embed(color=0x2525ff)
        em.add_field(name='Starting Game!', value=f'Balance: {balance}')
        await interaction.response.send_message(embed=em)
    except:
        em = discord.Embed(title='Could not start game', color=0xff0000)
        await interaction.followup.send(embed=em)
        return 0
    try:
        count = 0
        for x in range(click_amount):
            a = randint(0, 2)
            bf.Towers.Choose(choice=a, auth=auth_token)
            count += 1
    except:
        em = discord.Embed(title='You Lost', color=0xff0000)
        await interaction.followup.send(embed=em)
        return 0
    try:
        bf.Towers.Cashout(auth=auth_token)
        balance = int(bf.Currency.Balance(auth=auth_token))
        em = discord.Embed(color=0x00ff00)
        em.add_field(name='Cashed out!', value=f'Balance: {balance}\nClicked: {count} times')
        await interaction.followup.send(embed=em)
    except:
        balance = int(bf.Currency.Balance(auth=auth_token))
        em = discord.Embed(title=f"You lost!\nBalance: {balance}", color=0xff0000)
        await interaction.followup.send(embed=em)
        return 0

client.run('ur bots token skid')