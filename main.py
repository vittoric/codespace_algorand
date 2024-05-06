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


# Connect to the Algorand client (default local network)
algorand = AlgorandClient.default_local_net()

# Get dispenser account for funding
dispenser = algorand.account.dispenser()

# Create a random account for the asset creator
creator = algorand.account.random()

# Fund the creator account with 10,000,000 microAlgos
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)

# Define asset creation parameters
asset_params = AssetCreateParams(
    sender=creator.address,
    total=222,  # Total number of your asset units
    asset_name="BUILDH3R",
    unit_name="HER"
)

# Create the Algorand Standard Asset (ASA)
sent_txn = algorand.send.asset_create(asset_params)

# Extract the asset ID from the confirmation
asset_id = sent_txn["confirmation"]["asset-index"]

# Define three random accounts to receive the asset
recipient_accounts = [algorand.account.random() for _ in range(3)]


# Print the addresses of the recipient accounts
for i, recipient in enumerate(recipient_accounts):
  print(f"Recipient Account {i+1} Address: {recipient.address}")

# Fund each recipient account with 10,000,000 microAlgos
for recipient in recipient_accounts:
    algorand.send.payment(
        PayParams(
            sender=dispenser.address,
            receiver=recipient.address,
            amount=10_000_000
        )
    )

# Print information for each recipient account after funding
for recipient in recipient_accounts:
    account_info = algorand.account.get_information(recipient.address)
    print(f"\nRecipient Account {recipient.address} Information:")
    print(account_info)


# Opt-in each recipient account to receive the asset
for recipient in recipient_accounts:
    algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=recipient.address,
            asset_id=asset_id
        )
    )

# Create separate AssetTransferParams objects for each transfer
transfer_params_list = []
for recipient in recipient_accounts:
    transfer_params = AssetTransferParams(
        sender=creator.address,
        receiver=recipient.address,  # Set directly here
        asset_id=asset_id,
        amount=22
    )
    transfer_params_list.append(transfer_params)


# Print information for each recipient account after receiving the asset
for recipient in recipient_accounts:
    account_info = algorand.account.get_information(recipient.address)
    print(f"\nRecipient Account {recipient.address} Information (After Transfer):")
    print(account_info)

