import os
import sys
import threading
import tkinter
from tkinter import Button, Entry, LabelFrame, Tk

import requests


def run():
    def getItem():
        try:
            r = requests.get(
                f"https://rest.fnar.net/exchange/{ItemTickerBox.get()}.{ExchangeTickerBox.get()}"
            )
            json = r.json()

            materialName = json["MaterialName"]
            materialAsk = json["Ask"]
            ItemAskA = json["AskCount"]
            materialBid = json["Bid"]
            materialBidAmount = json["BidCount"]

            ItemNameText.delete(0, "end")
            ItemNameText.insert(0, materialName)
            # ItemNameText.config(state="readonly")

            ItemAskText.delete(0, "end")
            ItemAskText.insert(0, materialAsk)
            # ItemAskText.config(state="readonly")

            ItemAskAmount.delete(0, "end")
            ItemAskAmount.insert(0, ItemAskA)
            # ItemAskAmount.config(state="readonly")

            ItemBidText.delete(0, "end")
            ItemBidText.insert(0, materialBid)
            # ItemBidText.config(state="readonly")

            ItemBidAmount.delete(0, "end")
            ItemBidAmount.insert(0, materialBidAmount)
            # ItemBidAmount.config(state="readonly")
        except Exception as e:
            print(e)
            ItemNameText.delete(0, "end")
            ItemNameText.insert(0, e)

    thread = threading.Thread(target=getItem, daemon=True)
    thread.start()


def resource_path2(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = Tk()
icon = resource_path2("icon.ico")
root.iconbitmap(icon)
root.title("Prosperous Universe Item Price Checker")
root.geometry("476x250")
root.resizable(0, 0)
root["bg"] = "#222222"


ItemTicker = LabelFrame(root, text="   Item Ticker:", padx=5, pady=5)
ItemTicker.grid(column=0, row=0, padx=4, pady=4)
ItemTicker["bg"] = "#26353e"
ItemTicker["fg"] = "#fffefc"
ItemTicker["bd"] = 0

ItemTickerBox = Entry(ItemTicker, selectbackground="#26353e", width=25)
ItemTickerBox.grid(column=0, row=0, padx=4, pady=4)
ItemTickerBox["bg"] = "#42361d"
ItemTickerBox["fg"] = "#ffffff"
ItemTickerBox.insert(0, "BEA")

ExchangeTicker = LabelFrame(root, text="   Exchange Ticker:", padx=5, pady=5)
ExchangeTicker.grid(column=1, row=0, padx=4, pady=4)
ExchangeTicker["bg"] = "#26353e"
ExchangeTicker["fg"] = "#ffffff"
ExchangeTicker["bd"] = 0

ExchangeTickerBox = Entry(ExchangeTicker, selectbackground="#26353e", width=25)
ExchangeTickerBox.grid(column=1, row=0, padx=4, pady=4)
ExchangeTickerBox["bg"] = "#42361d"
ExchangeTickerBox["fg"] = "#ffffff"
ExchangeTickerBox.insert(0, "CI1")

ItemName = LabelFrame(root, text="   Item name:", padx=5, pady=5)
ItemName.grid(column=0, row=1, padx=4, pady=4, sticky=tkinter.W)
ItemName["bg"] = "#26353e"
ItemName["fg"] = "#ffffff"
ItemName["bd"] = 0

ItemNameText = Entry(ItemName, selectbackground="#26353e", width=25)
ItemNameText.grid(column=0, row=0, padx=4, pady=4)
ItemNameText["bg"] = "#3fa2de"
ItemNameText["fg"] = "#222222"


ItemAsk = LabelFrame(root, text="   Item ask:", padx=5, pady=5)
ItemAsk.grid(column=0, row=2, padx=4, pady=4)
ItemAsk["bg"] = "#26353e"
ItemAsk["fg"] = "#ffffff"
ItemAsk["bd"] = 0

ItemAskText = Entry(ItemAsk, selectbackground="#26353e", width=25)
ItemAskText.grid(column=0, row=0, padx=4, pady=4)
ItemAskText["bg"] = "#3fa2de"
ItemAskText["fg"] = "#222222"

ItemAskA = LabelFrame(root, text="   Item ask amount:", padx=5, pady=5)
ItemAskA.grid(column=1, row=2, padx=4, pady=4, sticky=tkinter.W)
ItemAskA["bg"] = "#26353e"
ItemAskA["fg"] = "#ffffff"
ItemAskA["bd"] = 0

ItemAskAmount = Entry(ItemAskA, selectbackground="#26353e", width=25)
ItemAskAmount.grid(column=1, row=0, padx=4, pady=4)
ItemAskAmount["bg"] = "#3fa2de"
ItemAskAmount["fg"] = "#222222"

ItemBid = LabelFrame(root, text="   Item bid:", padx=5, pady=5)
ItemBid.grid(column=0, row=3, padx=4, pady=4)
ItemBid["bg"] = "#26353e"
ItemBid["fg"] = "#ffffff"
ItemBid["bd"] = 0

ItemBidText = Entry(ItemBid, selectbackground="#26353e", width=25)
ItemBidText.grid(column=0, row=0, padx=4, pady=4)
ItemBidText["bg"] = "#3fa2de"
ItemBidText["fg"] = "#222222"

ItemBidA = LabelFrame(root, text="   Item bid amount:", padx=5, pady=5)
ItemBidA.grid(column=1, row=3, padx=4, pady=4, sticky=tkinter.W)
ItemBidA["bg"] = "#26353e"
ItemBidA["fg"] = "#ffffff"
ItemBidA["bd"] = 0

ItemBidAmount = Entry(ItemBidA, selectbackground="#26353e", width=25)
ItemBidAmount.grid(column=1, row=0, padx=4, pady=4)
ItemBidAmount["bg"] = "#3fa2de"
ItemBidAmount["fg"] = "#222222"

run_button = Button(ExchangeTicker, text="Check", height=1, width=14, command=run)
run_button.grid(column=2, row=0, padx=4, sticky="s")
run_button["bg"] = "#f7a600"
run_button["fg"] = "#ffffff"
run_button["activebackground"] = "#f7a600"
run_button["activeforeground"] = "#222222"
root.mainloop()


# def getItems(item, exchange, orderType):
#     r = requests.get(f'https://rest.fnar.net/exchange/{item}.{exchange}')
#     json = r.json()
#     orders = json[orderType]
#     lenght = len(orders)
#     print(f"Currently {json['MaterialName']} is selling for: {json['Ask']}, there are {json['AskCount']} on the market.")
#     print(f'{orderType} for: {item}')
#     for x in range(lenght):
#         print(f"Company name: {orders[x]['CompanyName']}, Number of items: {orders[x]['ItemCount']}, Item price: {orders[x]['ItemCost']}")

# # getItems('BEA', 'CI1', 'BuyingOrders')
# # getItems('DW', 'CI1', 'SellingOrders')

# def getItem(item, exchange):
#     r = requests.get(f'https://rest.fnar.net/exchange/{item}.{exchange}')
#     json = r.json()
#     print(f"Currently {json['MaterialName']} are selling for: {json['Ask']} and there are {json['AskCount']} on the market on that price.")

# getItem('BEA', 'CI1')
