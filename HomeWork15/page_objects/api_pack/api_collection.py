import json

from HomeWork15.page_objects.api_pack._base_api import BaseApi


class UsersApi(BaseApi):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.__url = '/users'

    def get_all_users(self, headers):
        return self._get(url=self.__url, headers=headers)

    def get_one_user(self, user_id, headers):
        return self._get(url=f'{self.__url}/{user_id}', headers=headers)

    def post_new_user(self, user_data: dict, headers):
        return self._post(self.__url, data=json.dumps(user_data), headers=headers)

    def patch_user(self, user_id, payloads, headers):
        return self._patch(f'{self.__url}/{user_id}', payloads=json.dumps(payloads), headers=headers)

    def bad_patch_user(self, user_id, payloads, headers):
        return self._patch(f'{self.__url}/{user_id}', payloads=payloads, headers=headers)

    def delete_user(self, user_id, headers):
        return self._delete(f'{self.__url}/{user_id}', headers=headers)

    def put_user(self, user_id, payloads, headers):
        return self._put(f'{self.__url}/{user_id}', payloads=json.dumps(payloads), headers=headers)


    def too_many_requests(self, headers):
        resp = self._get(self.__url, headers=headers)
        while resp.status_code == 200:
            resp = self._get(self.__url, headers=headers)
            if resp.status_code == 429:
                return resp

