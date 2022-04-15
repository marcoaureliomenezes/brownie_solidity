# Tutorial about ETHEREUM networks, simulated environments and the framework Brownie.

## What's brownie?



## Install Ganache-cli

    sudo npm install --global yarn
    sudo apt install nodejs
    sudo apt install npm
    yarn global add ganache-cli

## Brownie framework

### Installation

    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    pipx install eth-brownie

### Brownie Structure

The basic structure of a brownie application, after the command brownie init seems like this:

    _ build
        |_ contracts
        |_ deployments
        |_ interfaces
    
    _ contracts
    _ interfaces
    _ reports
    _ scripts
    _ tests (Python tests for testing the smart contract)
    _ brownie-config.yaml



### Start a project with Brownie
    $ brownie init
    The command above initializes a basic structure containing:
        - build: Low level folder that tracks the contract folder
            - contracts: 
            - deployments
            - interfaces
        - contracts
        - interfaces: Where can be saved any interface
        - scripts: Where tasks can be automated (deploys, utils, etc.)
        - tests: Where the tests are located.


### Creating a new account
    brownie accounts new freecodecamp-account
        - enter a private key
        - a secret (123)

### Compile contracts in a brownie project
    $ brownie compile


### Run a python script
    $ brownie run scripts/script.py
    $ brownie run scripts/deploy.py --network rinkeby


### Test a python script
    $ brownie test
    $ brownie test -k test_you_wish

### List networks
    $ brownie networks list

### Brownie console
    $ brownie console


### Criar mainnet fork com novas contas mocadas
Com INFURA:
    $ brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127/0.0.1 fork='https://mainnet.infura.io/v3/$WEB3_INFURA_PROJECT_ID'
$ brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127/0.0.1 fork='https://eth-mainnet.alchemyapi.io/v2/$WEB3_ALCHEMY_PROJECT_ID' accounts=10 mnemonic=brownie port=8545
Com ALCHEMY:


Networks running:
    defaultganache: 
    ganache_local: deploy fundMe e make some fund and withDraw Actions from many accounts
    rinkeby: deploy fundMe e make some fund and withDraw Actions from many accounts
    mainnet-fork-dev: Doen't deploy the contract. Running forever.
