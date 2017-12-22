"""
A state machine for the bot
"""

__author__ = 'Luis Serazo'
__email__ = 'lserazo.projects@gmail.com'

from collections import defaultdict
import logging


class Automaton (object):

	def __init__(self, states, transitions, init_state, during=None, on_enter=None, on_exit=None):
		"""
		Initialize an Automaton
		:param states: a list containing the states of the machine
		:param transitions: a list of dictionaries containing the transition functions and conditions.
		Dictionaries contain the key value pair x:y (source and destination). Can also have 'condition
		and reaction' keys. These are functions that are executed to check a condition and react to the
		condition, respectively.
		:param init_state: the initial state of the machine
		"""

		"""
		Initialization errors:
		"""
		if list(sorted(set(states))) != sorted(states):
			raise AutomatonException('List Of States contains duplicates. \n{}'.format(states))
		if init_state not in states:
			raise AutomatonException('Initial State not found in List of States. \nInitial: {}\nStates{}'.format(init_state, states))

		if during is None:
			during = {}
		if on_enter is None:
			on_enter = {}
		if on_exit is None:
			on_exit = {}

		# Setting the states. 
		self.__states = {}

		for state in states:
			self.__states[state] = State(state, during.get(state, None), on_enter.get(state, None), on_exit.get(state, None))

		# initial state:
		if init_state not in self.__states:
			raise AutomatonException('Invalid initial state: {0}'.format(init_state))
		# Setting up the current state of the Automaton (the initial state)
		self.current = self.__states[init_state]

		# Setting the transitions
		self.__transitions = defaultdict(list)

		# creating the transition function list.
		for transition in transitions:
			# All transition functions must be a mapping x :-> y such that x,y are in the states list. 
			if transition['x'] not in self.__states:
				raise AutomatonException('Transition takes in a state {} not in the List of States'.format(transition['x']))

			if transition['y'] not in self.__states:
				raise AutomatonException('Transition Outputs a state {} not in the List of States'.format(transition['y']))

			x = self.__states[transition['x']]
			y = self.__states[transition['y']]

			# Setting the transition list
			self.__transitions[transition['x']].append(Transition(x, y, transition.get('condition', None), transition.get('action', None)))

	def move(self):

		self.current.during()
		
		for transition in self.__transitions[self.current.name]:
			if transition.condition():
				logging.debug('Transitioning: {0}'.format(transition))
				transition.action()
				self.current.on_exit()
				self.current = transition.x
				self.current.on_enter()
				break


class State(object):

	def __init__(self, name, during, on_enter, on_exit):
		self.name = name
		self.__during = during
		self.__on_enter = on_enter
		self.__on_exit = on_exit

	def __repr__(self):
		return "State({0}, {1}, {2}, {3})".format(self.name, self.__during, self.__on_enter, self.__on_exit)

	def __str__(self):
		return self.name

	def during(self):
		if self.__during is not None:
			self.__during()

	def on_enter(self):
		if self.__on_enter is not None:
			self.__on_enter()

	def on_exit(self):
		if self.__on_exit is not None:
			self.__on_exit()


class Transition(object):

	def __init__(self, x, y, cond, action):
		self.x = x
		self.y = y
		self.__condition = cond
		self.__action = action

	def __repr__(self) -> str:
		return "transition({0},{1},{2},{3})".format(repr(self.x), repr(self.y), self.__condition, self.__reaction)

	def __str__(self) -> str:
		return "{0} :-> {1}".format(self.x, self.y)

	def condition(self):
		return True if self.__condition is None else self.__condition()

	def action(self):
		if self.__action is not None:
			self.__action()


class AutomatonException(Exception):
	pass
