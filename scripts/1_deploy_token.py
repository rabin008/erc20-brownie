from brownie import MyToken, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    my_token = MyToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Your token has been created")
