from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams,
)

"""
algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
print(dispenser.address)

creator = algorand.account.random()
#print(creator.address)
#print(algorand.account.get_information(creator.address))

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)

#print(algorand.account.get_information(creator.address))

sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=222,
        asset_name="BUILDH3R",
        unit_name="HER"
    )
)

asset_id = sent_txn["confirmation"]["asset-index"]
#print(asset_id)

reciver_acct = algorand.account.random()
#print(reciver_acct.address)

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=reciver_acct.address,
        amount=10_000_000
    )
)

algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=reciver_acct.address,
        asset_id=asset_id

    )
)

asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver= reciver_acct.address,
        asset_id=asset_id,
        amount=22
    )
)

print(algorand.account.get_information(reciver_acct.address))

"""
#Algoran task
"""Task: Create an Algorand Standerd Asset (Token/Asset). Then send the asset to three Algorand Accounts.

Screenshot proof: Print out the information of the three accounts that you sent the asset too."""


algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
#print(dispenser.address)
creator = algorand.account.random()
#print(creator.address)
#print(algorand.account.get_information(creator.address))

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)
#print(algorand.account.get_information(creator.address))

# Create the token
sent_token = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=648,
        asset_name="BUILDHER",
        unit_name="HER"
    )
)

asset_id = sent_token["confirmation"]["asset-index"]
#print(asset_id)

# Create three receiver accounts
receiver = [algorand.account.random() for _ in range(3)]


for receiver_acct in receiver:
    algorand.send.payment(
        PayParams(
            sender=dispenser.address,
            receiver=receiver_acct.address,
            amount=10_000_000
        )
    )

#opt in to asset so don't get spammed
    algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=receiver_acct.address,
            asset_id=asset_id
        )
    )

    asset_transfer =AssetTransferParams(
            sender=creator.address,
            receiver=receiver_acct.address,
            asset_id=asset_id,
            amount=210,
            last_valid_round=100 
        )
    
    algorand.send.asset_transfer(asset_transfer)

    print(f"Account address------> {receiver_acct.address} \nInformation after sending:")
    print(algorand.account.get_information(receiver_acct.address) , " \n")
