from scripts.helpful_scripts import get_account
from brownie import FundMe

def fund(gambler):
    fund_me = FundMe[-1]
    account = get_account(gambler)
    entrance_fee = fund_me.getEntranceFee()
    print(f"Current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    
def withDraw():
    fund_me = FundMe[-1]
    account = get_account('kandao')
    fund_me.withDraw({"from": account})
    
def get_balance():
    fund_me = FundMe[-1]
    account = get_account('kandao')
    print(fund_me.addressToAmountFunded(account.address))


def main():
    # for i in range(5):
    #     fund('dadaia')
    withDraw()
    get_balance()