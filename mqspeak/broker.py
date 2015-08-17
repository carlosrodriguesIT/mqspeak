class Broker:

    def __init__(self, name, host="127.0.0.1", port=1883):
        self.name = name
        self.host = host
        self.port = port

    def setCredentials(self, user, password):
        self._checkUserAndPass(user, password)
        self.user = user
        self.password = password

    def isAuthenticationRequired(self):
        return hasattr(self, "user") and hasattr(self, "password")

    def _checkUserAndPass(self, user, password):
        if type(user) is not str or len(user) <= 0:
            raise AttributeError("User must be non-zero length string")
        if type(password) is not str or len(password) <= 0:
            raise AttributeError("Password must be non-zero length string")

    def __hash__(self):
        return hash((self.name, self.host, self.port))

    def __str__(self):
        return "<{0} - {1}:{2}>".format(self.name, self.host, self.port)
