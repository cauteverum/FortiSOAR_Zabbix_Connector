import requests
import time
from connectors.core.connector import get_logger, ConnectorError
from connectors.core.utils import update_connnector_config
from pyzabbix import ZabbixAPI

error_msg = {
    401: 'Authentication failed due to invalid credentials',
    429: 'Rate limit was exceeded',
    403: 'Token is invalid or expired',
    "ssl_error": 'SSL certificate validation failed',
    'time_out': 'The request timed out while trying to connect to the remote server',
}

logger = get_logger("zabx")


class MakeRestApiCall:
    def __init__(self, config):
        self.username = config.get("username")
        self.password = config.get("password")
        self.url = config.get("url")
        self.verify = config.get("verify_ssl",False)
        if (not self.url.startswith("http://")) and (not self.url.startswith("https://")):
            self.url = "http://"+self.url


    def make_request(self, method, prms):
        try:
            zapi = ZabbixAPI(server=self.url,use_authenticate=self.verify)
            zapi.login(self.username, self.password)

            if not prms:
                prms = {}

            response = zapi.do_request(method=method, params=prms)["result"]
            zapi.do_request("user.logout")

            return response
        except Exception as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(error_msg.get('ssl_error')))
