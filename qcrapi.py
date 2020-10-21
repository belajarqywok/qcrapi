#!/bin/env python3
"""

follow @qywok_exploiter_357


"""
import os,sys,json,base64,requests,datetime,pandas
from time import sleep
class Generate:
    def __init__(self,token1,token2):
        self.getToken1=requests.get(base64.b64decode("".join(reversed(token1))).decode("ascii"))
        self.getToken2=requests.get(base64.b64decode("".join(reversed(token2))).decode("ascii"))
        self.coins=["bitcoin","doge","verus"]
    def dataGenerator(self):
        operators=1
        price=[]
        datas=[]
        data1=json.loads(self.getToken1.content)
        data2=json.loads(self.getToken2.content)
        for generate in range(len(self.coins)-1):
            if generate<operators:
                price.append(data1[generate]["market_data"]["current_price"]["usd"])
                operators+=47
                if(operators>generate):
                    price.append(data1[generate+operators]["market_data"]["current_price"]["usd"])
                    operators-=47
            else:
                price.append(data2["price_usd"])
                for generates in range(len(price)):
                    datas.append({
                        "cryptocurrency name\t ":self.coins[generates],
                        "price\t ":price[generates]
                    })
                dataFrame=pandas.DataFrame(datas)
                dataFrame.to_csv(str(datetime.datetime.now().strftime("%Y%m%d%H"))+".csv", index=False, encoding="utf-8")
class executed:
    def __init__(self):
        self.key1='vMnbp92YvMjdvkGch9SbvNmLvt2Yldmbp92YukGch9yL6MHc0RHa'
        self.key2='0V2ayFWbvMXdyVmdvQXZu5Cbv9GcrNWds9yL6MHc0RHa'
        self.generate=Generate(self.key1,self.key2)  

    def exec(self) :
        while True:
            os.system("clear")
            self.generate.dataGenerator()
            print("generate.... ")
            sleep(3)
if __name__=="__main__":
    try:    
        executed().exec()
    except KeyboardInterrupt:
        os.system("clear")
        print("exit")
        sys.exit(1)

