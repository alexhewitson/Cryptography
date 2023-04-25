# Cryptography

These attacks were executed against servers set up for the purpose and consent was given.

Length Extension Attack

The len_ext_attack.py file accepts a valid URL to an imaginary bank website and adds the command 'UnlockAllSafes' while maintaining the token value, so the server still accepts and executes the command after verifying the token. This proves that MD5 hashes are susceptible to such attacks.

Hash Collision

The good.py and evil.py files have the same md5 hash but different SHA-256 hashes, yet they print different messages when run. These files demonstrate the integrity risks to relying on outdated hashing functions like MD5.

Signatures

The bleichenbacher.py file is an example of a Bleichenbacher attack on a poorly-implemented checking function on a server that ignores the last bytes, allowing room to forge signatures.
