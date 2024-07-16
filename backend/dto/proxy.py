from backend.const import proxy as const


class ProxyDTO:
    def __init__(self, user_name: str, password: str, proxy_address: str, port: int):
        self.user_name = user_name
        self.password = password
        self.proxy_address = proxy_address
        self.port = port


# TODO: builder pattern refactoring
class ProxyDTOBuilder:
    @staticmethod
    def build(data: dict) -> ProxyDTO:

        user_name = data[const.FIELD_USERNAME]
        password = data[const.FIELD_PASSWORD]
        proxy_address = data[const.FIELD_PROXY_ADDRESS]
        port = data[const.FIELD_PORT]

        return ProxyDTO(
            user_name,
            password,
            proxy_address,
            port
        )
