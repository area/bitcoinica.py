import json
import urllib
import urllib2
import time
import base64


class Bitcoinica:
	"""Bitcoinica API"""
	def __init__(self, user, password):
		self.user = user
		self.password = password
		self.URI = "https://www.bitcoinica.com/api/"
		self.timeout = 10

	def get_quotes(self, pair):
		return self.perform("quotes/"+pair+".json")
	
	def get_hist_quotes(self, pair, n=100): 
		return self.perform("quotes/"+pair+"/history.json",n=str(n))

	def get_compatable_quotes(self, pair):
		return self.perform("quotes/"+pair+"/compatible.json")

	def get_error(self):
		return self.perform("none.json")

	def get_candlesticks(self, pair="BTCUSD", n=100, period=900):
		return self.perform("candlesticks/"+pair+".json",n=str(n), period=str(period))

	def get_orders(self, n=100):
		return self.perform("orders.json","GET", True, n=str(n))
	
	def get_active_orders(self, n=100):
		return self.perform("orders/active.json","GET",True, n=str(n))

	def show_order(self, id):
		return self.perform("orders/"+str(id)+".json","GET", True)

	def place_order(self, price, amount,type="MARKET",pair="BTCUSD"):
		return self.perform("orders.json","POST", True, price=str(price), amount=str(amount), type=str(type), pair=str(pair))

	def delete_order(self, id):
		return self.perform("orders/"+str(id)+".json", "DELETE", True)
	
	def get_positions(self, n=100):
		return self.perform("positions.json", "GET", True, n=str(n))
	
	def get_active_positions(self, n=100):
		return self.perform("positions/active.json", "GET", True, n=str(n))
	def get_account_info(self):
		return self.perform("account.json", "GET", True)

	def perform(self, method, httpmethod="GET", auth=False, **kwargs):
		url = self.URI+method
		req = urllib2.Request(url)
    		if kwargs:
			if httpmethod=="GET":
			        url += '?' + urllib.urlencode(kwargs)
				req = urllib2.Request(url)
       			else:	
				req.add_data(urllib.urlencode(kwargs))
		print url
		if auth:
    			auth = 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (self.user, self.password))
    			req.add_header('Authorization', auth)
		opener = urllib2.build_opener()
		if httpmethod=="DELETE":
			req.get_method = lambda: 'DELETE'
		try:
			f = opener.open(req)
			k = json.load(f)
			status = f.getcode()
		except urllib2.URLError, e: 
			k = json.dumps(dict(Error=e.read()))
			status = e.code
		#Get status of k
		return status, k

    # req.get_method() -> 'POST'

