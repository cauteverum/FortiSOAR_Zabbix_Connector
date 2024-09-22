from .make_rest_api_call import MakeRestApiCall


def _check_health(config: dict) -> bool:
    try:
        method = "host.get"
        prms = {}
        MK = MakeRestApiCall(config=config)
        response = MK.make_request(method=method, prms=prms)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        raise Exception(e)
