import six






def to_str(s, encoding=None, errors="strict", normalize=False):
    """
    Given str, bytes, bytearray, or unicode (py2), return str
    """

    def _normalize(s):
        try:
            return unicodedata.normalize("NFC", s) if normalize else s
        except TypeError:
            return s

    if encoding is None:
        # Try utf-8 first, and fall back to detected encoding
        encoding = ("utf-8", __salt_system_encoding__)
    if not isinstance(encoding, (tuple, list)):
        encoding = (encoding,)

    if not encoding:
        raise ValueError("encoding cannot be empty")

    # This shouldn't be six.string_types because if we're on PY2 and we already
    # have a string, we should just return it.
    if isinstance(s, str):
        return _normalize(s)

    exc = None
    if six.PY3:
        if isinstance(s, (bytes, bytearray)):
            for enc in encoding:
                try:
                    return _normalize(s.decode(enc, errors))
                except UnicodeDecodeError as err:
                    exc = err
                    continue
            # The only way we get this far is if a UnicodeDecodeError was
            # raised, otherwise we would have already returned (or raised some
            # other exception).
            raise exc  # pylint: disable=raising-bad-type
        raise TypeError("expected str, bytes, or bytearray not {}".format(type(s)))
    else:
        if isinstance(s, bytearray):
            return str(s)  # future lint: disable=blacklisted-function
        # pylint: disable=incompatible-py3-code,undefined-variable
        if isinstance(s, unicode):
            for enc in encoding:
                try:
                    return _normalize(s).encode(enc, errors)
                except UnicodeEncodeError as err:
                    exc = err
                    continue
            # The only way we get this far is if a UnicodeDecodeError was
            # raised, otherwise we would have already returned (or raised some
            # other exception).
            raise exc  # pylint: disable=raising-bad-type
        # pylint: enable=incompatible-py3-code,undefined-variable
        raise TypeError("expected str, bytes, or bytearray not {}".format(type(s)))


def to_unicode(s, encoding=None, errors="strict", normalize=False):
    """
    Given str or unicode, return unicode (str for python 3)
    """

    def _normalize(s):
        return unicodedata.normalize("NFC", s) if normalize else s

    if encoding is None:
        # Try utf-8 first, and fall back to detected encoding
        encoding = ("utf-8", __salt_system_encoding__)
    if not isinstance(encoding, (tuple, list)):
        encoding = (encoding,)

    if not encoding:
        raise ValueError("encoding cannot be empty")

    exc = None
    if six.PY3:
        if isinstance(s, str):
            return _normalize(s)
        elif isinstance(s, (bytes, bytearray)):
            return _normalize(to_str(s, encoding, errors))
        raise TypeError("expected str, bytes, or bytearray not {}".format(type(s)))
    else:
        # This needs to be str and not six.string_types, since if the string is
        # already a unicode type, it does not need to be decoded (and doing so
        # will raise an exception).
        # pylint: disable=incompatible-py3-code
        if isinstance(s, unicode):  # pylint: disable=E0602
            return _normalize(s)
        elif isinstance(s, (str, bytearray)):
            for enc in encoding:
                try:
                    return _normalize(s.decode(enc, errors))
                except UnicodeDecodeError as err:
                    exc = err
                    continue
            # The only way we get this far is if a UnicodeDecodeError was
            # raised, otherwise we would have already returned (or raised some
            # other exception).
            raise exc  # pylint: disable=raising-bad-type
        # pylint: enable=incompatible-py3-code
        raise TypeError("expected str, bytes, or bytearray not {}".format(type(s)))
