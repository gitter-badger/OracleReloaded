'''
The internals of the trader. Defines a core structure 
called Trader which aggregates strategies and manages
behavior of the bot.
'''

__author__ = 'Luis Serazo'
__email__ = 'serazo.luis@gmail.com'


from abc import ABCMeta, abstractmethod


class Trader(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	def initialize_trade(self, raw_data):
		pass

	@abstractmethod
	def finish_trade(self, trade):
		pass

	@abstractmethod
	def alert_admin(self):
		pass

	@abstractmethod
	def lookup_ttable(self):
		pass

	@abstractmethod
	def make_trade(self, exchg, request):
		pass

	@abstractmethod
	def request_exchg_data(self, exchg):
		pass
