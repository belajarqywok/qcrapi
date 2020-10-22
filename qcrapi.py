#!/bin/env python3
"""

follow @qywok_exploiter_357


"""
import os
import sys
import json
import base64
import pandas
import requests
import datetime
from time import sleep
from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment
class Generate:
    def __init__(self,token1,token2):
        self.getToken1=requests.get(base64.b64decode("".join(reversed(token1))).decode("ascii"))
        self.getToken2=requests.get(base64.b64decode("".join(reversed(token2))).decode("ascii"))
        self.coins=["bitcoin","doge","verus"]
    def csvGenerator(self):
        operators=1
        price=[]
        datas=[]
        data1=json.loads(self.getToken1.content)
        data2=json.loads(self.getToken2.content)
        for generate in range(len(self.coins)-1):
            if generate<operators:
                price.append(data1[generate]["market_data"]["current_price"]["usd"])
                operators+=48
                if(operators>generate):
                    price.append(data1[generate+operators]["market_data"]["current_price"]["usd"])
                    operators-=48
            else:
                price.append(data2["price_usd"])
                for generates in range(len(price)):
                    datas.append({
                        "cryptocurrency name ":self.coins[generates],
                        "price ":price[generates]
                    })
                dataFrame=pandas.DataFrame(datas)
                dataFrame.to_csv(str(datetime.datetime.now().strftime("%Y%m%d%H"))+".csv", index=False, encoding="utf-8")
    def jsonGenerator(self):
        operators=1
        price=[]
        datas=[]
        data1=json.loads(self.getToken1.content)
        data2=json.loads(self.getToken2.content)
        for generate in range(len(self.coins)-1):
            if generate<operators:
                price.append(data1[generate]["market_data"]["current_price"]["usd"])
                operators+=48
                if(operators>generate):
                    price.append(data1[generate+operators]["market_data"]["current_price"]["usd"])
                    operators-=48
            else:
                price.append(data2["price_usd"])
                for generates in range(len(price)):
                    datas.append({
                        "cryptocurrency name ":self.coins[generates],
                        "price ":price[generates]
                    })
                    objects=json.dumps(datas, indent = 4) 
                    with open(str(datetime.datetime.now().strftime("%Y%m%d%H"))+".json", "w") as writeFile:
                        writeFile.write(objects)
    def xmlGenerator(self):
        operators=1
        prices=[]
        data1=json.loads(self.getToken1.content)
        data2=json.loads(self.getToken2.content)
        def prettify(elem):
            rough_string = ElementTree.tostring(elem, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            return reparsed.toprettyxml(indent="  ")
        cryptocurrency=Element("cryptocurrency")
        for addPrices in range(len(self.coins)-1):
            if addPrices<operators:
                prices.append(data1[addPrices]["market_data"]["current_price"]["usd"])
                operators+=48
                if operators>addPrices:
                    prices.append(data1[addPrices+operators]["market_data"]["current_price"]["usd"])
                    operators-=48
            else:
                prices.append(data2["price_usd"])
                for crypto in range(len(prices)):
                    cryptocurrency.append(Comment(self.coins[crypto]+'coin'))
                    SubElement(cryptocurrency, self.coins[crypto]).text=str(prices[crypto])
        with open(str(datetime.datetime.now().strftime("%Y%m%d%H"))+".xml", "w") as writeFile:
            writeFile.write(prettify(cryptocurrency))
class executed:
    def __init__(self):
        self.key1='vMnbp92YvMjdvkGch9SbvNmLvt2Yldmbp92YukGch9yL6MHc0RHa'
        self.key2='0V2ayFWbvMXdyVmdvQXZu5Cbv9GcrNWds9yL6MHc0RHa'
        self.generate=Generate(self.key1,self.key2)  
    def exec(self) :
        while True:
            os.system("clear")
            self.generate.csvGenerator()
            self.generate.jsonGenerator()
            self.generate.xmlGenerator()
            print("generate.... ")
            sleep(3)
if __name__=="__main__":
    try:    
        executed().exec()
    except KeyboardInterrupt:
        os.system("clear")
        print("exit")
        sys.exit(1)

