from brownie import accounts, config, SimpleStorage, network


def get_account():
    test_account =  accounts.add(config["wallets"]["from_key"]["dadaia"])
    return accounts[0] if network.show_active() == "development" else test_account


def deploy_simple_storage():
    account = get_account()
    # account = accounts.load("freecodecamp-account")
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

    
def main():
    deploy_simple_storage()