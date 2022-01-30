from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    password: str
    email: str

    def update(self, username: str, password: str, email: str):
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
