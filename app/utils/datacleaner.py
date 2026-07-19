def non_empty_payload(payload):
    non_empty_payload = dict()
    for k,v in payload.items():
        if v is not None:
            non_empty_payload[k] = v
    return non_empty_payload


def type_corrector(payload):
    payload["year"] = int(payload.get("year")) if payload.get("year") else None

    payload["kilometers"] = int(payload.get("kilometers").replace(",", "").replace(" Kms", "")) if payload.get("kilometers") else None
    print(payload)
    return payload

def etl(payload):
    payload = type_corrector(payload)
    return non_empty_payload(payload)
