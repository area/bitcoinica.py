#Bitcoinica.py

This is a Python interface for the Bitcoinica API, which 
is documented over at [Bitcoinica](https://bitcoinica.com/pages/api).

##Introduction and Disclaimers

This interface comes with no guarantees. I've done some basic testing with it,
and have used it to manage active trading in the past. However, should it cause
you to lose all your money, I accept no responsibility for your loss, and by
using this interface you accept these terms.

I wholeheartedly endorse the warnings Bitconica supplies when you sign up,
namely that leverage can be dangerous to use, and that you should never
speculate with money that you cannot afford to lose.

##Usage

	from bitcoinica import Bitcoinica

	exchange=Bitcoinica(username, password)
	account = exchange.get_account_info()
	print account

Output:

	(200, {u'tradable_balance': 0.58392404282117516, u'leverage': 2.5, u'margin_balance': 0.23356961712847005, u'maintenance': 0.0, u'unrealized_pl': 0, u'id': 3863, u'net_value': 0.23356961712847005})

The return from every call is a tuple. `Tuple[0]` is the http error code
returned. A '200' indicates that the call was successful. Another code
indicates that an error occurred. '401' suggests that your username and password
are invalid; '422' might suggest that while the call was legitimate, there was
some reason why it couldn't be executed - e.g. you asked for a list of your
positions, but you don't have any. 

`Tuple[1]` contains a
JSON element. On a successfull call, it will contain the JSON element returned
by the Bitcoinica API. On a failed call, it will contain an error message that
is hopefully helpful.

No inputs are checked for sanity. You should sanitize inputs while using this
API interface.

##Supported Methods

All methods documented under the Bitcoinica API are supported. The arguments
they each take can be easily seen by examining the methods at the start of the
Bitcoinica class.

A username and password are required to instantiate the class, but they won't
be verified until a call is made that requires authentication. This class can
therefore be used with fake credentials to be able to use `get_candlesticks()`
and similar calls that do not require authentication.

##Donations

If you find this interface useful and wish to donate, then you can donate spare bitcoins to 1svU3uB96irJ145gZD9yPjR52Pizft5s8.
