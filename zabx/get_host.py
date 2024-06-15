from .make_rest_api_call import MakeRestApiCall


def get_host(config: dict, params: dict) -> dict:
    method = "host.get"
    prms = params.get("params")
    MK = MakeRestApiCall(config=config)
    response = MK.make_request(method=method, prms=prms)
    return response