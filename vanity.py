
from algosdk import account
from algosdk import mnemonic
import time

# Desired prefix for address.
PREFIX = "AAA"

# Variables containing Private Key and Address
PRIVATE_KEY1 = ""
ADDRESS1 = ""

# Keep track of attempts and start time.
ATTEMPT = 0
TIME_START = time.time()

# Keep looping until desired address is found.
while (not ADDRESS1.startswith(PREFIX)):
    TIME_DIFF = time.time() - TIME_START
    print(f" {ATTEMPT} ({ATTEMPT / TIME_DIFF:.2f}/sec) ", end="\r")
    PRIVATE_KEY1, ADDRESS1 = account.generate_account()
    ATTEMPT += 1

print()
print(f"Found after {ATTEMPT} attempts and {TIME_DIFF:.2f} seconds")
print(ADDRESS1)
print(PRIVATE_KEY1)
print(mnemonic.from_private_key(PRIVATE_KEY1))
print(mnemonic)
print()