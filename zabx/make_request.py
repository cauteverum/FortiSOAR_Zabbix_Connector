from .make_rest_api_call import MakeRestApiCall


def make_request(config: dict, params: dict) -> dict:
    method = params.get("method")
    prms = params.get("params")
    MK = MakeRestApiCall(config=config)
    response = MK.make_request(method=method, prms=prms)
    return response