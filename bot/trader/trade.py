"""
File: trade.py

Description: enumerable type to represent
            a trade type.

"""


__author__ = 'Luis Serazo'
__email__ = 'lserazo.projects@gmail.com'

from enum import Enum


class TradeType(Enum):

	BUY = 'buy'
	SELL = 'sell'
	SHORT = 'short'

	def __init__(self, t_type):
		self._t_type = t_type

	def get_type(self):
		return self._t_type


"""
No standard for exchanges so raw_order is not
too elegant. 
"""


class Trade(object):

	def __init__(self, raw_order, trade_id):

		self.TID = trade_id

		self.exchange = raw_order.get('exchg', None)
		if not self.exchange:
			TradeException('No exchange specified')

		order_t = raw_order.get('type', None)

		if order_t:
			if order_t.lower() == 'buy':
				self.t_type = TradeType.BUY

			elif order_t.lower() == 'sell':
				self.t_type = TradeType.SELL

			elif order_t.lower() == 'short':
				self.t_type = TradeType.SHORT

			else:
				TradeException('Order type: {0} unrecognized'.format(order_t))
		else:
			TradeException('No trade type specified')

		self._t_open = True

		self.quantity = raw_order.get('quant', None)

		if not self.exchange:
			TradeException('No quantity specified')

	def close_trade(self):
		self._t_open = False

	def trade_status(self):
		if self._t_open:
			return 'Trade Open'
		return 'Trade Closed'


class TradeException(Exception):
	pass

