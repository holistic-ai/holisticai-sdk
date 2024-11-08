import json

import requests


class NYCBiasAudit:
    """
    {
        "tenant_id": "",
        "apikey": ""
    }
    """

    nyc_bias_audit_url = ""
    onboard_system_endpoint = ""
    run_bias_audit_endpoint = ""
    get_systems_endpoint = ""

    def __init__(self, config):
        self.config = config
        self._validate_config(config)

    @staticmethod
    def _validate_config(config):
        if "apikey" not in config:
            raise Exception("Expected apikey does not exist in the provided config")

    def prepare_request(self, json_data, endpoint):
        url = self.nyc_bias_audit_url + endpoint
        headers = {
            "x-hai-nyc-bias-audit-key": self.config["apikey"],
            "apikey": "",
        }
        json_data["tenant_id"] = self.config["tenant_id"]
        return url, headers, json_data

    def onboard_system(self, json_data):
        url, headers, json_data = self.prepare_request(
            json_data, self.onboard_system_endpoint
        )
        response = requests.post(url=url, headers=headers, json=json_data)
        if response.status_code != 200:
            raise Exception(
                f"Onboarding system failed with status code {response.status_code}"
            )
        return json.loads(response.content)["system_id"]

    def run_bias_audit(self, json_data):
        url, headers, json_data = self.prepare_request(
            json_data, self.run_bias_audit_endpoint
        )
        response = requests.post(url=url, headers=headers, json=json_data)
        if response.status_code != 200:
            raise Exception(
                f"Running bias audit failed with status code {response.status_code}"
            )

    def get_systems(self):
        url, headers, json_data = self.prepare_request({}, self.get_systems_endpoint)
        response = requests.post(url=url, headers=headers, json=json_data)
        if response.status_code != 200:
            raise Exception(
                f"Retrieving systems failed with status code {response.status_code}"
            )

        return json.loads(response.content)
