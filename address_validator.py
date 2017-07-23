# from https://gist.github.com/pipermerriam/f7633dc2657b1292860c
# https://github.com/ethereum/EIPs/issues/55

import sha3

LOWER_CHARS = {'0', '1', '2', '3', '4', '5', '6', '7'}


def checksum(address):
    normalized_address = address.lower().replace('0x', '')
    address_hash = sha3.sha3_256(normalized_address.encode('utf-8')).hexdigest()
    checksum_address = '0x' + ''.join((
        c.lower() if address_hash[idx] in LOWER_CHARS else c.upper()
        for idx, c in enumerate(normalized_address)
    ))
    return checksum_address


def check(address, strict=False):
    normalized_address = address.lower().replace('0x', '')

    if len(normalized_address) != 40:
        return False
    elif address.replace('0x', '') == checksum(normalized_address).replace('0x', ''):
        return True
    elif strict:
        return False
    elif normalized_address.lower() == normalized_address or normalized_address.upper() == normalized_address:
        return True
    else:
        return False


if __name__ == "__main__":
    vectors = (
        # All UPPER
        (
            '0x52908400098527886e0f7030069857d2e4169ee7',
            '0x52908400098527886E0F7030069857D2E4169EE7',
        ),
        (
            '0x8617e340b3d01fa5f11f306f4090fd50e238070d',
            '0x8617E340B3D01FA5F11F306F4090FD50E238070D',
        ),
        # All Lower
        (
            '0xde709f2102306220921060314715629080e2fb77',
            '0xde709f2102306220921060314715629080e2fb77',
        ),
        (
            '0x27b1fdb04752bbc536007a920d24acb045561c26',
            '0x27b1fdb04752bbc536007a920d24acb045561c26',
        ),
        # Mixed
        (
            '0x9cf3ed8e75f1db20bcedfadab0966fa58bc8b0ef',
            '0x9CF3Ed8E75F1dB20BceDfaDab0966FA58BC8b0ef',
        ),
        (
            '0xa30490a10d3ad0a1bcd97528d24d2f5070dbcb60',
            '0xa30490a10D3ad0A1bcD97528D24D2F5070dBcb60',
        ),
    )
    for a, b in vectors:
        assert checksum(a) == b
        assert check(b, True)

    # strict mode non-checksummed
    assert not check('0x9cf3ed8e75f1db20bcedfadab0966fa58bc8b0ef', True)
    assert check('0x9cf3ed8e75f1db20bcedfadab0966fa58bc8b0ef', False)
    # All lower checksummed
    assert check('0xde709f2102306220921060314715629080e2fb77', True)
    assert check('0xde709f2102306220921060314715629080e2fb77', False)
    # All upper checksummed
    assert check('0x8617E340B3D01FA5F11F306F4090FD50E238070D', True)
    assert check('0x8617E340B3D01FA5F11F306F4090FD50E238070D', False)