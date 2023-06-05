from dataclasses import dataclass


@dataclass
class Users:
    nickname: str
    old: int
    birth: str
    state: str


def showUser(u):
    print("Users{")
    print("nickname:", u.nickname)
    print("old:", str(u.old))
    print("birth:", u.birth)
    print("state:", u.state)
    print("}")


user = Users("kirishima kyoko", 20, "04/27", "tokyo")
showUser(user)
