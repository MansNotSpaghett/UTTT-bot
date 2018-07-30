import discord
from discord.ext import commands
import asyncio
import rules, board, boardList, boardListFunc, nextMove
bot = commands.Bot(command_prefix="$")
import os
doThey=None
O = [" / ", " - "," \\ ",
     " | ", "   ", " | ",
     " \\ "," - ", " / "]
X = [" \\ ", "   ", " / ",
     "   ", " ☓ ", "   ",
      " / ", "   ", " \\ "]
T = [" - "," - "," - ",
     "   ", " | ", "   ",
     "   ", " | ", "   "]
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id) 
    print('-------')
@bot.command()
async def UTTT(ext,z,x=[],O=O,X=X,T=T):
    if ext.author == bot.user:
        return
    if z=="UTTT":
        UTTT.counter=0
        UTTT.counter+=1
        await ext.channel.send("Do you know the controls? [Y/N]: ")
    elif UTTT.counter%2==1:
        if z=="Y":
            doThey="Y"
            print("a")
            UTTT.play=1
        elif z=="N":
            doThey="N"
            print("b")
            UTTT.play=1
        else:
            doThey=None
            print("c")
        if doThey=="Y":
            pass
            UTTT.counter=0
        elif doThey=="N":
            UTTT.counter=0
            await ext.channel.send("""\nthe ultimate board is made out of 9 different boards and numbered like so:
1 2 3
4 5 6
7 8 9
so selecting "1" would select the top left board. the same thing applies for the small boards. So "23" would select the top middle board's top right place.""")
        else:
            await ext.channel.send("Y or N!")
            await ext.channel.send("Do you know the controls? [Y/N]: ")
    #Introduction is done, time for the actual game:
    #######
    elif UTTT.play==1 and z=="play":
        finished=[]
        put="21"
        a = 1
        canPlayAnywhere = False
        while True:
            zU = 0
            z = 0
            nM = nextMove.nM(put)
            if all(elem in finished for elem in [nM]) == True and isinstance(put, int):
                canPlayAnywhere = True
            if rules.theWinner(boardList.bLU) != 0:
                await ext.channel.send("The winner is {}!".format("X" if rules.theWinner(boardList.bLU) == 1 else "O"))
                UTTT.play=0
                for x in range(1,10):
                    setattr(boardList,"bL"+str(x),[[0,0,0],[0,0,0],[0,0,0]])
                    for y in range(1,10):
                        setattr(board,"b"+str(x)+str(y),"   ")
                setattr(boardList,"bLU",[[0,0,0],[0,0,0],[0,0,0]])
                break
            for x in boardList.bLU:
                for y in x:
                    if y != 0:
                        zU += 1
                if zU == 9:
                    await ext.channel.send("It's a tie!")
                    UTTT.play=0
                    for x in range(1,10):
                        setattr(boardList,"bL"+str(x),[[0,0,0],[0,0,0],[0,0,0]])
                        for y in range(1,10):
                            setattr(board,"b"+str(x)+str(y),"   ")
                    setattr(boardList,"bLU",[[0,0,0],[0,0,0],[0,0,0]])
                    break
            a += 1
            await ext.channel.send(board.board())
            if nM != None and canPlayAnywhere != True and isinstance(put, str) != True:
                await ext.channel.send("You must make a move on the {}th tile".format(nM))
            elif canPlayAnywhere == True:
                await ext.channel.send("You can play anywhere you like because your opponent sent you to a tile that was already finished!")
            await ext.channel.send("\n{}s turn!\n".format("X" if a%2==0 else "O"))
            await ext.channel.send("Where do you want to put your mark?")
            put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)
            put=put.content
            if put=="die":
                await ext.channel.send("ded af")
                for x in range(1,10):
                    setattr(boardList,"bL"+str(x),[[0,0,0],[0,0,0],[0,0,0]])
                    for y in range(1,10):
                        setattr(board,"b"+str(x)+str(y),"   ")
                setattr(boardList,"bLU",[[0,0,0],[0,0,0],[0,0,0]])
                UTTT.play=0
                break
            try:
                put = int(put)
            except:
                pass
            if a % 2==0:
                mark = " X "
            else:
                mark = " O "
            while isinstance(put, str) or (str(put)[0] != nM and nM != None) or all(elem not in [int(str(x)+str(y)) for x in range(1,10) for y in range(1,10)] for elem in [put]) or len(str(put)) != 2 or getattr(boardList, "bL"+str(put)[0])[boardListFunc.Func1(put)][boardListFunc.Func2(put)] != 0 or boardList.bLU[boardListFunc.FuncU1(put)][boardListFunc.FuncU2(put)] != 0 or rules.theWinner(getattr(boardList, "bL"+str(put)[0])) != 0:
                try:
                    if canPlayAnywhere == True:
                        if isinstance(put, str):
                            await ext.channel.send(board.board())
                            await ext.channel.send("You can play anywhere you like because your opponent sent you to a tile that was already finished!")
                            await ext.channel.send("You didn't type a number!")
                            await ext.channel.send("Where do you want to put your mark?")
                            put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)                       
                        try:
                            if getattr(boardList, "bL"+str(put)[0])[boardListFunc.Func1(put)][boardListFunc.Func2(put)] != 0 and len(str(put)) != 2:
                                await ext.channel.send(board.board())
                                await ext.channel.send("You can play anywhere you like because your opponent sent you to a tile that was already finished!")
                                await ext.channel.send("There is already a mark there")
                                await ext.channel.send("Where do you want to put your mark?")
                                put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)
                        except:
                            pass
                        if all(elem not in [int(str(x)+str(y)) for x in range(1,10) for y in range(1,10)] for elem in [put]) or len(str(put)) != 2:
                            await ext.channel.send(board.board())
                            await ext.channel.send("You can play anywhere you like because your opponent sent you to a tile that was already finished!")
                            await ext.channel.send("What you typed wasn't what the computer expected as a place. Try again")
                            await ext.channel.send("Where do you want to put your mark?")
                            put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)      
                        elif str(put)[0] != nM and nM != None:
                            break
                        elif (getattr(boardList, "bL"+str(put)[0])[boardListFunc.FuncU1(put)][boardListFunc.FuncU2(put)] != 0  and len(str(put)) != 2) or rules.theWinner(getattr(boardList, "bL"+str(put)[0])) != 0:
                            await ext.channel.send(board.board())
                            await ext.channel.send("You can play anywhere you like because your opponent sent you to a tile that was already finished!")
                            await ext.channel.send("That tile is already finished!")
                            await ext.channel.send("Where do you want to put your mark?")
                            put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)           
                    elif isinstance(put, str):
                        await ext.channel.send(board.board())
                        if a != 2:
                            await ext.channel.send("You must make a move on the {}th tile".format(nM))
                        await ext.channel.send("You didn't type a number!")
                        await ext.channel.send("Where do you want to put your mark?")
                        put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)       
                    elif (getattr(boardList, "bL"+str(put)[0])[boardListFunc.FuncU1(put)][boardListFunc.FuncU2(put)] != 0  and len(str(put)) != 2) or rules.theWinner(getattr(boardList, "bL"+str(put)[0])) != 0:
                        await ext.channel.send(board.board())
                        if a != 2:
                            await ext.channel.send("You must make a move on the {}th tile".format(nM))
                        await ext.channel.send("That tile is already finished!")
                        await ext.channel.send("Where do you want to put your mark?")
                        put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)
                    elif len(str(put)) != 2:
                        await ext.channel.send(board.board())
                        if a != 2: 
                            await ext.channel.send("You must make a move on the {}th tile".format(nM))
                        await ext.channel.send("What you typed wasn't what the computer expected as a place. Try again")
                        await ext.channel.send("Where do you want to put your mark?")
                        put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)
                    elif str(put)[0] != nM and nM != None:
                        await ext.channel.send(board.board())
                        if a != 2:
                            await ext.channel.send("You must make a move on the {}th tile".format(nM))
                        await ext.channel.send("You didn't make your move on the specified tile")
                        await ext.channel.send("Where do you want to put your mark?")
                        put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)  
                    try:
                        if getattr(boardList, "bL"+str(put)[0])[boardListFunc.Func1(put)][boardListFunc.Func2(put)] != 0 and isinstance(put, int):
                            await ext.channel.send(board.board())
                            if a != 2:
                                await ext.channel.send("You must make a move on the {}th tile".format(nM))
                            await ext.channel.send("There is already a mark there")
                            await ext.channel.send("Where do you want to put your mark?")
                            put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)
                    except:
                        pass
                except:
                    await ext.channel.send(board.board())
                    if a != 2:
                        await ext.channel.send("You must make a move on the {}th tile".format(nM))
                    await ext.channel.send("What you typed wasn't what the computer expected as a place. Try again")
                    await ext.channel.send("Where do you wanna put your mark? (e.g: 99 for the right-down right-down place as in 9th TTT table and 9th place) ")
                    put=await bot.wait_for("message", check=lambda msg: msg.author != bot.user)
                put = put.content
                if put=="die":
                    break
                try:
                    put = int(put)
                except:
                    pass
            setattr(board,"b"+str(put),mark)   
            getattr(boardList, "bL"+str(put)[0])[boardListFunc.Func1(put)][boardListFunc.Func2(put)] = 1 if mark == "X" else 2
            if put=="die":
                await ext.channel.send("ded af")
                UTTT.play=0
                for x in range(1,10):
                    setattr(boardList,"bL"+str(x),[[0,0,0],[0,0,0],[0,0,0]])
                    for y in range(1,10):
                        setattr(board,"b"+str(x)+str(y),"   ")
                setattr(boardList,"bLU",[[0,0,0],[0,0,0],[0,0,0]])
                break
            if rules.theWinner(getattr(boardList, "bL"+str(put)[0])) != 0:
                await ext.channel.send(getattr(boardList,"bL"+str(put)[0]))
                for x in range(1, 10):
                    if rules.theWinner(getattr(boardList, "bL"+str(put)[0])) == 1:
                        setattr(board,"b"+str(put)[0]+str(x), X[-x])
                    else:
                        setattr(board,"b"+str(put)[0]+str(x), O[-x])
                boardList.bLU[boardListFunc.FuncU1(put)][boardListFunc.FuncU2(put)] = 1 if mark == "X" else 2
                await ext.channel.send(mark)
                finished.append(str(put)[0])
                setattr(board,"bL"+str(put)[0], [[1,1,1],[1,1,1],[1,1,1]])
            print((boardList.bLU[boardListFunc.FuncU1(put)][boardListFunc.FuncU2(put)]) != 3)
            if (boardList.bLU[boardListFunc.FuncU1(put)][boardListFunc.FuncU2(put)]) != 3:
                for x in getattr(boardList, "bL"+str(put)[0]):
                    for y in x:
                        if y != 0:
                            z += 1
                if z == 9:
                    boardList.bLU[boardListFunc.FuncU1(put)][boardListFunc.FuncU2(put)] = 3
                    for y in range(9):
                        setattr(board,"b"+str(put)[0]+str(y+1), T[y])
                    setattr(boardList,"bL"+str(put)[0], [[1,1,1],[1,1,1],[1,1,1]])   
                    finished.append(str(put)[0])
            await ext.channel.send(getattr(boardList,"bL"+str(put)[0]))
            canPlayAnywhere = False
bot.run(os.environ['BOT_TOKEN'])
