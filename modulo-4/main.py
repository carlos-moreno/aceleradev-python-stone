import jwt


def create_token(payload: dict, key="acelera", algorithm="HS256") -> bytes:
    """Return a JSON Web Token.

    :param:
    payload (dict): Payload to be encoded
    key (str): Key suitable for the chosen algorithm
    algorithm (str): Algorithm to sign the token (HS256 is default)

    :return:
    bytes: a JSON Web Token

    :except:
    TypeError
    """
    try:
        encode_payload = jwt.encode(payload, key, algorithm)
    except TypeError as t:
        return t
    return encode_payload


def verify_signature(jwt_: bytes, key="acelera", algorithms=["HS256"]) -> dict:
    """Verify the jwt token signature and return the token claims.

    :param:
    jwt_ (str|bytes): The token to be decoded
    key (str): The key suitable for the allowed algorithm
    algorithm (list): Allowed algorithms

    :return:
    dict: the JWT claims

    :except:
    jwt.InvalidSignatureError
    jwt.DecodeError
    """
    try:
        decode_jwt_ = jwt.decode(jwt_, key, algorithms)
    except jwt.InvalidSignatureError:
        return {"error": 2}
    except jwt.DecodeError:
        return "Invalid crypto padding"
    return decode_jwt_
