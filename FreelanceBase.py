from typing import List, Tuple


class FreelanceBase:

    def __init__(self) -> None:
        self.status = 0
        self.user = list()

    @property
    def User(self) -> Tuple[str]:
        return tuple(self._get_User())

    @User.setter
    def User(self, new_data: List[str]) -> None:
        if new_data == None:
            self.status = -1
        elif int(new_data[1]) == 0:
            self.status = 1
        else:
            self._set_User(new_data)

    @User.deleter
    def User(self) -> None:
        self._clear_User

    def _get_User(self) -> List[str]:
        return self.user

    def _set_User(self, new_data: List[str]) -> None:
        if len(self.user) == 0:
            self.user = new_data[2::2].copy()
            self.status = 1
        elif len(self.user) > 0:
            for user in range(2, (int(new_data[1]) + 1) * 2, 2):
                if new_data[user] in self.user:
                    continue
                else:
                    self.user.append(new_data[user])
                    self.status = 1
        print(f'{__class__.__name__}: wurde mit Exit Code {self.status} Ausgeführt!')

    def _clear_User(self) -> None:
        self.user.clear()
        self.status = 0