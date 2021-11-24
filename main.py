import os
import sys
import threading
import tkinter
from tkinter import Button, Entry, LabelFrame, Tk

import requests


def run():
    def getData():
        try:
            r = requests.get(
                f"https://rest.fnar.net/exchange/{ItemTickerBox.get().upper()}.{ExchangeTickerBox.get().upper()}"
            )
            json = r.json()

            materialName = json["MaterialName"]
            materialAsk = json["Ask"]
            ItemAskA = json["AskCount"]
            materialBid = json["Bid"]
            materialBidAmount = json["BidCount"]
            currency = json["Currency"]
            averagePrice = json["PriceAverage"]
            supply = json["Supply"]
            demand = json["Demand"]

            ItemNameText.delete(0, "end")
            ItemNameText.insert(0, materialName)

            currencyText.delete(0, "end")
            currencyText.insert(0, currency)

            AvgPriceText.delete(0, "end")
            AvgPriceText.insert(0, averagePrice)

            ItemAskText.delete(0, "end")
            ItemAskText.insert(0, materialAsk)

            ItemAskAmount.delete(0, "end")
            ItemAskAmount.insert(0, ItemAskA)

            SupplyText.delete(0, "end")
            SupplyText.insert(0, supply)

            ItemBidText.delete(0, "end")
            ItemBidText.insert(0, materialBid)

            ItemBidAmount.delete(0, "end")
            ItemBidAmount.insert(0, materialBidAmount)

            DemandText.delete(0, "end")
            DemandText.insert(0, demand)
        except Exception as e:
            print(e)
            ItemNameText.delete(0, "end")
            currencyText.delete(0, "end")
            AvgPriceText.delete(0, "end")
            ItemAskText.delete(0, "end")
            ItemAskAmount.delete(0, "end")
            SupplyText.delete(0, "end")
            ItemBidText.delete(0, "end")
            ItemBidAmount.delete(0, "end")
            DemandText.delete(0, "end")
            ItemNameText.insert(0, e)

    thread = threading.Thread(target=getData, daemon=True)
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
root.geometry("450x250")
root.resizable(0, 0)
root["bg"] = "#222222"


ItemTicker = LabelFrame(root, text="   Item Ticker", padx=5, pady=5)
ItemTicker.grid(column=0, row=0, padx=4, pady=4)
ItemTicker["bg"] = "#26353e"
ItemTicker["fg"] = "#ffffff"
ItemTicker["bd"] = 0

ItemTickerBox = Entry(ItemTicker, selectbackground="#26353e", width=20)
ItemTickerBox.grid(column=0, row=0, padx=4, pady=4)
ItemTickerBox["bg"] = "#42361d"
ItemTickerBox["fg"] = "#ffffff"
ItemTickerBox.insert(0, "BEA")

ExchangeTicker = LabelFrame(root, text="   Exchange Ticker", padx=5, pady=5)
ExchangeTicker.grid(column=1, row=0, padx=4, pady=4)
ExchangeTicker["bg"] = "#26353e"
ExchangeTicker["fg"] = "#ffffff"
ExchangeTicker["bd"] = 0

ExchangeTickerBox = Entry(ExchangeTicker, selectbackground="#26353e", width=20)
ExchangeTickerBox.grid(column=1, row=0, padx=4, pady=4)
ExchangeTickerBox["bg"] = "#42361d"
ExchangeTickerBox["fg"] = "#ffffff"
ExchangeTickerBox.insert(0, "CI1")

ItemName = LabelFrame(root, text="   Item name", padx=5, pady=5)
ItemName.grid(column=0, row=1, padx=4, pady=4, sticky=tkinter.W)
ItemName["bg"] = "#26353e"
ItemName["fg"] = "#ffffff"
ItemName["bd"] = 0

ItemNameText = Entry(ItemName, selectbackground="#26353e", width=20)
ItemNameText.grid(column=0, row=0, padx=4, pady=4)
ItemNameText["bg"] = "#3fa2de"
ItemNameText["fg"] = "#222222"

currency = LabelFrame(root, text="   Currency", padx=5, pady=5)
currency.grid(column=1, row=1, padx=4, pady=4, sticky=tkinter.W)
currency["bg"] = "#26353e"
currency["fg"] = "#ffffff"
currency["bd"] = 0

currencyText = Entry(currency, selectbackground="#26353e", width=20)
currencyText.grid(column=0, row=0, padx=4, pady=4)
currencyText["bg"] = "#3fa2de"
currencyText["fg"] = "#222222"

AvgPrice = LabelFrame(root, text="   Average price", padx=5, pady=5)
AvgPrice.grid(column=2, row=1, padx=4, pady=4)
AvgPrice["bg"] = "#26353e"
AvgPrice["fg"] = "#ffffff"
AvgPrice["bd"] = 0

AvgPriceText = Entry(AvgPrice, selectbackground="#26353e", width=20)
AvgPriceText.grid(column=0, row=0, padx=4, pady=4)
AvgPriceText["bg"] = "#3fa2de"
AvgPriceText["fg"] = "#222222"

ItemAsk = LabelFrame(root, text="   Item ask", padx=5, pady=5)
ItemAsk.grid(column=0, row=2, padx=4, pady=4)
ItemAsk["bg"] = "#26353e"
ItemAsk["fg"] = "#ffffff"
ItemAsk["bd"] = 0

ItemAskText = Entry(ItemAsk, selectbackground="#26353e", width=20)
ItemAskText.grid(column=0, row=0, padx=4, pady=4)
ItemAskText["bg"] = "#3fa2de"
ItemAskText["fg"] = "#222222"

ItemAskA = LabelFrame(root, text="   Item ask amount", padx=5, pady=5)
ItemAskA.grid(column=1, row=2, padx=4, pady=4, sticky=tkinter.W)
ItemAskA["bg"] = "#26353e"
ItemAskA["fg"] = "#ffffff"
ItemAskA["bd"] = 0

ItemAskAmount = Entry(ItemAskA, selectbackground="#26353e", width=20)
ItemAskAmount.grid(column=1, row=0, padx=4, pady=4)
ItemAskAmount["bg"] = "#3fa2de"
ItemAskAmount["fg"] = "#222222"

Supply = LabelFrame(root, text="   Supply", padx=5, pady=5)
Supply.grid(column=2, row=2, padx=4, pady=4)
Supply["bg"] = "#26353e"
Supply["fg"] = "#ffffff"
Supply["bd"] = 0

SupplyText = Entry(Supply, selectbackground="#26353e", width=20)
SupplyText.grid(column=0, row=0, padx=4, pady=4)
SupplyText["bg"] = "#3fa2de"
SupplyText["fg"] = "#222222"

ItemBid = LabelFrame(root, text="   Item bid", padx=5, pady=5)
ItemBid.grid(column=0, row=3, padx=4, pady=4)
ItemBid["bg"] = "#26353e"
ItemBid["fg"] = "#ffffff"
ItemBid["bd"] = 0

ItemBidText = Entry(ItemBid, selectbackground="#26353e", width=20)
ItemBidText.grid(column=0, row=0, padx=4, pady=4)
ItemBidText["bg"] = "#3fa2de"
ItemBidText["fg"] = "#222222"

ItemBidA = LabelFrame(root, text="   Item bid amount", padx=5, pady=5)
ItemBidA.grid(column=1, row=3, padx=4, pady=4, sticky=tkinter.W)
ItemBidA["bg"] = "#26353e"
ItemBidA["fg"] = "#ffffff"
ItemBidA["bd"] = 0

ItemBidAmount = Entry(ItemBidA, selectbackground="#26353e", width=20)
ItemBidAmount.grid(column=1, row=0, padx=4, pady=4)
ItemBidAmount["bg"] = "#3fa2de"
ItemBidAmount["fg"] = "#222222"

Demand = LabelFrame(root, text="   Demand", padx=5, pady=5)
Demand.grid(column=2, row=3, padx=4, pady=4)
Demand["bg"] = "#26353e"
Demand["fg"] = "#ffffff"
Demand["bd"] = 0

DemandText = Entry(Demand, selectbackground="#26353e", width=20)
DemandText.grid(column=0, row=0, padx=4, pady=4)
DemandText["bg"] = "#3fa2de"
DemandText["fg"] = "#222222"

button = LabelFrame(root, padx=5, pady=5)
button.grid(column=2, row=0, padx=4, pady=4)
button["bg"] = "#26353e"
button["fg"] = "#ffffff"
button["bd"] = 0

run_button = Button(button, text="Check", height=1, width=16, command=run)
run_button.grid(column=0, row=0, padx=4, pady=9)
run_button["bg"] = "#f7a600"
run_button["fg"] = "#ffffff"
run_button["activebackground"] = "#f7a600"
run_button["activeforeground"] = "#222222"

root.mainloop()
