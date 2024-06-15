from .make_rest_api_call import MakeRestApiCall


def get_groups(config: dict, params: dict) -> dict:
    method = "hostgroup.get"
    prms = params.get("params")
    MK = MakeRestApiCall(config=config)
    response = MK.make_request(method=method, prms=prms)
    return response