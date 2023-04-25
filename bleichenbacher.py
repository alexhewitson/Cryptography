from roots import *
import hashlib
import sys

message = sys.argv[1]
ARBITRARY_BYTES = 217
EXPONENT = 3

# start of the forged RSA message plus the "magic" bytes
forged_sig_start = "0001FF003021300906052B0E03021A05000414"

# get the hex digest of the provided message
digest = hashlib.sha1()
digest.update(message.encode())
hex_digest = digest.hexdigest()

# temporarily fill in the remaining 217 bytes at the end with 00
arbitrary_bytes = "00" * 217

# build the initial RSA message
starting_signature_bytes = forged_sig_start + hex_digest + arbitrary_bytes
# convert the hex RSA message to an integer
signature_integer = int(starting_signature_bytes, 16)
# find the perfect cube of the message, rounding up, resulting in the signature
cube = integer_nthroot(signature_integer, EXPONENT)[0]
is_perfect_cube = integer_nthroot(signature_integer, EXPONENT)[1]

forged_signature = cube
# if it was not a perfect cube and the above method rounded down, round it up instead
if (not is_perfect_cube):
    forged_signature += 1

print(integer_to_base64(forged_signature))