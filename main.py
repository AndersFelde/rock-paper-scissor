import tkinter
import random
from functools import partial

joe = {}
joe["papir"] = {"papir": "Det ble likt",
                "stein": "Du vant", "saks": "Du tapte"}
joe["saks"] = {"saks": "Det ble likt", "papir": "Du vant", "stein": "Du tapte"}
joe["stein"] = {"stein": "Det ble likt",
                "saks": "Du vant", "papir": "Du tapte"}

print(joe)


def updateResult(text):
    result["text"] = text


def updatePick(text):
    pick["text"] = text


def win(text, res):
    result2["text"] = joe[text][res]


def game(text):
    updatePick(text)
    res = getRandom()
    updateResult(res)
    win(text, res)


def getRandom():
    rand = ["stein", "saks", "papir"]
    return random.choice(rand)


top = tkinter.Tk()
# C = tkinter.Canvas(top, bg="blue", height=250, width=300)
# C.create_text(text="Stein, saks eller papir?")
# C.pack()
tkinter.Label(top, text="Stein, saks, papir", height="4").grid(row=0, column=1)

tkinter.Label(top, text="Du valgte: ", height=4).grid(row=1, column=0)

pick = tkinter.Label(top, text="", height=4)
pick.grid(row=1, column=1)


tkinter.Label(top, text="Maskin valgte: ", height=4).grid(row=2, column=0)
result = tkinter.Label(top, text="", height=4)
result.grid(row=2, column=1)

result2 = tkinter.Label(top, text="", height=4)
result2.grid(row=3, column=1)

tkinter.Button(top,
               text="stein", height=4, command=partial(game, "stein")).grid(row=4, column=0)
tkinter.Button(top,
               text="saks", height=4, command=partial(game, "saks")).grid(row=4, column=1)
tkinter.Button(top,
               text="papir", height=4, command=partial(game, "papir")).grid(row=4, column=2)


top.mainloop()
