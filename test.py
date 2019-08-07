import requests
from datetime import datetime
import time
from config import Apikey
from config import Tradeconfig
from pprint import pprint
import hmac
import hashlib
from WrapperAPI import WrapperAPI
from ExecLogic import ExecLogic
from TradeMethod import TradeMethod




def position():
    api_key = Apikey.api_key
    api_secret = Apikey.api_secret

    base_url = "https://api.bitflyer.jp"
    path_url = "/v1/me/getchildorders?product_code=BTC_JPY&child_order_state=COMPLETED"
    method = "GET"

    timestamp = str(datetime.today())
    message = timestamp + method + path_url

    signature = hmac.new(bytearray(api_secret.encode('utf-8')), message.encode('utf-8') , digestmod = hashlib.sha256 ).hexdigest()

    headers = {
        'ACCESS-KEY' : api_key,
        'ACCESS-TIMESTAMP' : timestamp,
        'ACCESS-SIGN' : signature,
        'Content-Type' : 'application/json'
    }

    response = requests.get( base_url + path_url , headers = headers)
    pprint(response.json()[0]["id"])
    return response.json()

# def check_open_orders(bitflyer):
#     try:
#         orders = bitflyer.fetch_open_orders(
#             symbol = "BTC/JPY",
#             params = { "product_code" : "BTC_JPY" })
#         pprint(orders)
        
#     except ccxt.BaseError as e:
#         print("BitflyerのAPIで問題発生 : ",e)
#     else:
#         return orders
    
def jsontest():
    aaa = "hi"
    bbb = None
    ccc = 120
    m = {
            "aaa" : aaa,
            "bbb" : bbb
        }
    n = {
            "ccc" : ccc,
            "ddd" : [m]
        }

    pprint(n)

def wraptest():
    wr = WrapperAPI()
    pprint(wr.get_my_balance())
    res=wr.get_my_balance()
    JPY=res[0]
    BTC=res[1]
    if JPY["currency_code"] != "JPY":
        raise Exception("Illegal balance")
    if BTC["currency_code"] != "BTC":
        raise Exception("Illegal balance")
    pprint(JPY)
    pprint(BTC)

def logictest():
    ExecLogic().get_price(900,4)

if __name__ == "__main__":
    # position()
    # bitflyer = ccxt.bitflyer({
    #             'apiKey': Apikey.api_key,
    #             'secret': Apikey.api_secret,
    #             })
    
    # check_open_orders(bitflyer)
    trader = TradeMethod()
    trader.d_message("aaaaaaaa\nbbbbbbbbbb")
    print("aaaaaaaaa\nbbbbbb")