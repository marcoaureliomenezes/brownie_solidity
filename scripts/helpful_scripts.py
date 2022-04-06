from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
DECIMALS = 8
STARTING_PRICE = 2*10**11
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

CONTAS_TESTE = {
    'development': {
        'dadaia': 0,
        'menopausa': 1,
        'kandao': 2,
        'zeppelin': 3
    },
    'testnet': {
        'dadaia': config["wallets"]["from_key"]["dadaia"],
        'menopausa': config["wallets"]["from_key"]["menopausa"],
        'kandao': config["wallets"]["from_key"]["kandao"],
        'zeppelin': config["wallets"]["from_key"]["zeppelin"]
    }
}

def get_account(user):
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[CONTAS_TESTE['development'][user]]
    return accounts.add(CONTAS_TESTE['testnet'][user])


def deploy_mocks(user):
    print(f"The active network is {network.show_active()}\n\tDeployingMocks ...")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": accounts[CONTAS_TESTE['development'][user]]})
    print("Mocks Deployed!")