"""
This file is part of Python Twofish
a Python bridge to the C Twofish library by Niels Ferguson

Released under The BSD 3-Clause License
Copyright (c) 2013 Keybase

Python module
"""

from _twofish_cffi import ffi, lib

__all__ = ["Twofish"]

lib.Twofish_initialise()


def _ensure_bytes(data: bytes) -> None:
    if not isinstance(data, bytes):
        raise TypeError("can not encrypt/decrypt str objects")


class Twofish:
    def __init__(self, key: bytes) -> None:
        if not (0 < len(key) <= 32):
            raise ValueError("invalid key length")
        _ensure_bytes(key)

        self.key = ffi.new("Twofish_key *")
        lib.Twofish_prepare_key(key, len(key), self.key)

    def encrypt(self, data: bytes) -> bytes:
        if not len(data) == 16:
            raise ValueError("invalid block length")
        _ensure_bytes(data)

        buf = ffi.new("Twofish_Byte[]", len(data))
        lib.Twofish_encrypt(self.key, data, buf)
        return bytes(buf)

    def decrypt(self, data: bytes) -> bytes:
        if not len(data) == 16:
            raise ValueError("invalid block length")
        _ensure_bytes(data)

        buf = ffi.new("Twofish_Byte[]", len(data))
        lib.Twofish_decrypt(self.key, data, buf)
        return bytes(buf)


# Repeat the test on the same vectors checked at runtime by the library
def self_test() -> None:
    import binascii

    # 128-bit test is the I=3 case of section B.2 of the Twofish book.
    t128 = (
        "9F589F5CF6122C32B6BFEC2F2AE8C35A",
        "D491DB16E7B1C39E86CB086B789F5419",
        "019F9809DE1711858FAAC3A3BA20FBC3",
    )

    # 192-bit test is the I=4 case of section B.2 of the Twofish book.
    t192 = (
        "88B2B2706B105E36B446BB6D731A1E88EFA71F788965BD44",
        "39DA69D6BA4997D585B6DC073CA341B2",
        "182B02D81497EA45F9DAACDC29193A65",
    )

    # 256-bit test is the I=4 case of section B.2 of the Twofish book.
    t256 = (
        "D43BB7556EA32E46F2A282B7D45B4E0D57FF739D4DC92C1BD7FC01700CC8216F",
        "90AFE91BB288544F2C32DC239B2635E6",
        "6CB4561C40BF0A9705931CB6D408E7FA",
    )

    for t in (t128, t192, t256):
        k = binascii.unhexlify(t[0])
        p = binascii.unhexlify(t[1])
        c = binascii.unhexlify(t[2])

        T = Twofish(k)
        if not T.encrypt(p) == c or not T.decrypt(c) == p:
            raise ImportError("the Twofish library is corrupted")


self_test()
