from twitchio.ext import commands
import pydirectinput

a = True
correr = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token='seu_tolken', prefix='!', initial_channels=['canal'])

    async def event_ready(self):
        print(f'Bot {self.nick} ligado')

    @commands.command()
    async def esquerda(self, ctx: commands.Context, algo=1):
        try:
            number = int(algo)
            if number > 1:
                for c in range(0, number):
                    pydirectinput.press('left')
        except:
            pydirectinput.press('left')

    @commands.command()
    async def andar_esquerda(self, ctx: commands.Context):
        global a
        if a == True:
            pydirectinput.keyDown('left')
            a = False
        else:
            pydirectinput.keyUp('left')
            a = True

    @commands.command()
    async def direita(self, ctx: commands.Context, algo=1):
        try:
            number = int(algo)
            if number > 1:
                for c in range(0, number):
                    pydirectinput.press('right')
        except:
            pydirectinput.press('right')

    @commands.command()
    async def andar_direita(self, ctx: commands.Context):
        global a
        if a == True:
            pydirectinput.keyDown('right')
            a = False
        else:
            pydirectinput.keyUp('right')
            a = True

    @commands.command()
    async def pular(self, ctx: commands.Context):
        pydirectinput.press('z')

    @commands.command()
    async def rodar(self, ctx: commands.Context):
        pydirectinput.press('x')

    @commands.command()
    async def correr(self, ctx: commands.Context):
        global correr
        if correr == True:
            pydirectinput.keyDown('s')
            correr = False
        if not correr:
            pydirectinput.keyUp('s')
            correr = True


bot = Bot()
bot.run()
