import requests


class HttpRequest:
    @classmethod
    def send(cls, method, url, data=None, headers=None, json=True, params=None):
        request_method = getattr(requests, method)
        response = request_method(
            **{
                "url": url,
                "headers": headers,
                "json" if json else "data": data,
                "params": params,
            }
        )

        return response

    @classmethod
    def get(cls, url, data=None, headers=None, json=True, params=None):
        return cls.send("get", url, data, headers, json, params)

    @classmethod
    def post(cls, url, data=None, headers=None, json=True, params=None):
        return cls.send("post", url, data, headers, json, params)

    @classmethod
    def patch(cls, url, data=None, headers=None, json=True, params=None):
        return cls.send("patch", url, data, headers, json, params)

    @classmethod
    def put(cls, url, data=None, headers=None, json=True, params=None):
        return cls.send("put", url, data, headers, json, params)

    @classmethod
    def delete(cls, url, data=None, headers=None, json=True, params=None):
        return cls.send("delete", url, data, headers, json, params)


http_request = HttpRequest()
