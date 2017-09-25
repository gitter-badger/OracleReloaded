# *Oracle Reloaded*
[![Build Status](https://travis-ci.org/luserazo/OracleReloaded.svg?branch=first-branch)](https://travis-ci.org/luserazo/OracleReloaded)

## Branches
   - a) Master
     	- No product ready code yet! 

   - b) First_Branch
     	- This is the first dev-branch.

## Descrition:
Oracle Reloaded cryptocurrency trading bot which focuses on an arbitrage strategy. Therefore, executions must be *fast* and seemless. The main component of the bot is the **Trader**. The Trader is responsible for communicating with the various exchanges and scraping data. In order for there to be little error in execution. The Trader is designed to be a Finite State Machine. Therefore it can only be in one of several predetermined states at once. The bot should fail silently and when it does fail, it should no longer execute any more trades. 

## Persistance
Uses PostgreSQL for persistance. 

## Current progress in design:
I've just set up the backbone of the design. The design is subject to change! It was simply created to get my feet off the floor. 

