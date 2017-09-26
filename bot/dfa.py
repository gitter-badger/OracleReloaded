"""
A state machine for the bot
"""

__author__ = 'Luis Serazo'
__email__ = 'lserazo.projects@gmail.com'

from collections import defaultdict
import logging


class Automaton (object):

	def __init__(self, states, delta_l, init_state):
		"""
		Initialize an Automaton
		:param states: a list containing the states of the machine
		:param delta_l: a dictionary containing the transition functions
		:param init_state: the initial state of the machine
		"""
		# Error Handling
		if list(sorted(set(states))) != sorted(states):
			raise AutomatonException('List Of States contains duplicates. \n{}'.format(states))
		if init_state not in states:
			raise AutomatonException('Initial State not found in List of States. \nInitial: {}\nStates{}'.format(init_state, states))

		# Setting the states. 
		self.__states = states
		# Setting up the current state of the Automaton (the initial state)
		self.__current = init_state
		# Setting the delta_l
		self.__delta_l = defaultdict(list)

		# creating the transition function list.
		for delta in delta_l:
			# All transition functions must be a mapping x :-> y such that x,y are in the states list. 
			if delta['x'] not in self.__states:
				raise AutomatonException('Transistion takes in a state {} not in the List of States'.format(delta['x']))

			if delta['y'] not in self.__states:
				raise AutomatonException('Transition Outputs a state {} not in the List of States'.format(delta['y']))

			x = self.__states[delta['x']]
			y = self.__states[delta['y']]

			# Setting the delta list
			self.__delta_l[delta['source_x']].append(Delta(x, y))

	def next_state(self):
		for delta in self.__delta_l[self.__current]:
			if delta.can_move():
				logging.debug('Transitioning: {0}'.format(delta))
				delta.make_move()
				self.__current = delta.get_x()
				break


class Delta(object):
	"""
	Transition function class
	"""
	def __init__(self, x, y, condition, reaction):
		# (state val, state val, Callable[...,bool], Callable[..., None]) -> None
		"""
		Arguments:
		:param x:
		:param y:
		:param condition:
		:param reaction:
		"""
		self.x = x
		self.y = y
		self.__condition = condition
		self.__reaction = reaction

	def __repr__(self) -> str:
		return "Delta({0},{1},{2},{3})".format(repr(self.x), repr(self.y), self.__condition, self.__reaction)

	def __str__(self) -> str:
		return "{0} :-> {1}".format(self.x, self.y)

	def make_move(self):
		if self.__reaction is not None:
			self.__reaction()

		
class AutomatonException(Exception):
	pass
