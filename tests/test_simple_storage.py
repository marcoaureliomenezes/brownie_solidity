from brownie import SimpleStorage, accounts



def test_deploy():
    account = accounts[0]                                           # Arrange
    simple_storage = SimpleStorage.deploy({"from": account})        # Arrange
    real_value, expected_value = (simple_storage.retrieve(), 0)     # Act
    assert real_value == expected_value                             # Assert
    
    
def test_updating_storage():
    account = accounts[0]                                                   # Arrange
    simple_storage = SimpleStorage.deploy({"from": account})                # Arrange
    expected_value = 15                                                     # Act
    simple_storage.store(expected_value, {"from": account})                 # Act
    assert expected_value == simple_storage.retrieve()                      # Assert
    