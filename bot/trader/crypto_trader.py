"""
File: cypto_trader

Description: the actual trader bot
"""

__author__ = 'Luis Serazo'
__email__ = 'lserazo.projects@gmail.com'

from bot.trader.state_machine import Automaton
from bot.trader.trader import Trader


class CryptoBot(Automaton, Trader):

	def __init__(self, exg_config, bot_config):

		self._dbpath = bot_config['dbpath']

		self._exchanges = exg_config['exchanges']

		initilize_exchanges(self._exchanges)

		self._open_trades = {}

		self._states = ['error', 'idle', 'analyzing', 'trading']

		self._transitions = [

			{
				'x': 'idle',
				'y': 'analyzing',
				'condition': self._timeout()
			},

			{
				'x': 'analyzing',
				'y': 'idle',
				'condition': self._no_opportunity(),
				'action': self._start_timer()  # different thread.
			},

			{
				'x': 'analyzing',
				'y': 'trading',
				'condition': self._opportunity()
			},

			{
				'x': 'trading',
				'y': 'idle',
				'condition': self._trade_terminated(),
				'action': self._start_timer()
			},

			{
				'x': 'trading',
				'y': 'error',
				'condition': self._error(),
				'action': self._alert_admin()
			},

			{
				'x': 'analyzing',
				'y': 'error',
				'condition': self._error(),
				'action': self._alert_admin()
			},

			{
				'x': 'idle',
				'y': 'error',
				'condition': self._error(),
				'action': self._action_admin()
			}
		]


