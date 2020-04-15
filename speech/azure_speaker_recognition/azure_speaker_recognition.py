import json

import requests


class AzureSpeakerIdentificationAPIHelper:

    def __init__(
        self,
        api_key: str,
        endpoint: str
    ):
        self._API_KEY = api_key
        self._ENDPOINT = endpoint

    def get_profile_id_list(self):
        """[summary]

        Raises:
            e: [description]

        Returns:
            [type]: [description]
        """
        URL = f'{self._ENDPOINT}/spid/v1.0/identificationProfiles'
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self._API_KEY,
        }

        try:
            res = requests.get(URL, headers=headers)
            json_data_list = res.json()
            profile_ids = [data['identificationProfileId'] for data in json_data_list]
        except Exception as e:
            raise e

        return profile_ids

    def delete_profile(self, profile_id: str):
        """[summary]

        Args:
            profile_id (str): [description]

        Raises:
            e: [description]

        Returns:
            [type]: [description]
        """
        URL = f'{self._ENDPOINT}/spid/v1.0/identificationProfiles/{profile_id}'
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self._API_KEY,
        }

        try:
            res = requests.delete(URL, headers=headers)
        except Exception as e:
            raise e

        return res

    def delete_all_profile(self) -> None:
        """[summary]
        """
        profile_ids = self.get_profile_id_list()
        for pi in profile_ids:
            print(f'deleting {pi}')
            self.delete_profile(pi)

    def create_profile(self, locale: str = 'zh-CN') -> str:
        """[summary]

        Args:
            locale (str, optional): [description]. Defaults to 'zh-CN'.

        Raises:
            e: [description]

        Returns:
            [type]: [description]
        """
        URL = f'{self._ENDPOINT}/spid/v1.0/identificationProfiles'
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self._API_KEY,
        }

        body = {
            'locale': locale,
        }
        json_data = json.dumps(body).encode("utf-8")

        try:
            res = requests.post(URL, data=json_data, headers=headers)
            json_data = res.json()
            profile_id = json_data['identificationProfileId']
        except Exception as e:
            raise e

        return profile_id

    def create_enrollment(
        self,
        profile_id: str,
        wav_path: str
    ):
        URL = f'{self._ENDPOINT}/spid/v1.0/identificationProfiles/{profile_id}/enroll?shortAudio=true'
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self._API_KEY,
        }

        data = open(wav_path, 'rb').read()

        try:
            res = requests.post(URL, data=data, headers=headers)
        except Exception as e:
            raise e

        return res
