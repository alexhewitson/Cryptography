#!/usr/bin/env python3
# coding: iso-8859-1
   
MSG = bytes(r"""                                                             q�
8��$�St���o@�_C"8A�8!Np�nr��obn&O1�u���|�oH؎��[p�I����)X#:a������@�����qy�z��g�c����."GB���8�q����m�
""", "iso-8859-1")
from hashlib import sha256
if (sha256(MSG).hexdigest().startswith("f")):
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")