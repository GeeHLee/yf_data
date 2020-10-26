import requests
import datetime
from utils import diff_seconds
from bs4 import BeautifulSoup as bs

class spyder:
    def __init__(self):
        conn = requests.session()
        send_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"}
        conn.headers.update(send_headers)
        self.conn = conn
    
    @staticmethod
    def date_seconds(nb, unit):
        assert unit in ["year", "day", "max"], "unit take only year or day or max"
        period2 = diff_seconds(datetime.datetime.now().date())
        if unit == "year":
            base = 365*24*60*60*nb
        elif unit == "day":
            base = 1*24*60*60*nb
        else:
            base = period2*2
        
        period1 = period2 - base
        return (period1, period2)
    
    def get_history(self, code, nb, unit):
        code = code.upper()
        p1, p2 = self.date_seconds(nb, unit)
        history_url = """
        https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true
        """.format(code, p1, p2) 
        response = self.conn.get(history_url)
        return response.text.split("\n")
    
    def get_history_bulk(self, file):
        ##TODO, read a csv file and get history of each share code.
        pass
    
    def push_to_base(self):
        ##TODO push to sql base.
        pass