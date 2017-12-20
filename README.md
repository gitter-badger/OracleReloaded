# *Oracle Reloaded*
[![Build Status](https://travis-ci.org/luserazo/OracleReloaded.svg?branch=first-branch)](https://travis-ci.org/luserazo/OracleReloaded)

## Branches
   - a) Master
     	- structure of project. 

   - b) dev
     	- work in progress.

## Descrition:
Oracle Reloaded cryptocurrency trading bot which focuses on an arbitrage strategy. Therefore, executions must be *fast* and seemless. The main component of the bot is the **Trader**. The Trader is responsible for communicating with the various exchanges and scraping data. In order for there to be little error in execution. The Trader is designed to be a Finite State Machine. Therefore it can only be in one of several predetermined states at once. The bot should fail silently and when it does fail, it should no longer execute any more trades. 

## Persistance
Uses PostgreSQL for persistance. 

