from typing import Tuple


class ReadFile:
    """
     Klasse zum Auslesen verschiedener Files
    """

    def __init__(self) -> None:
        """
        __init__ Initalisieren aller benötigten Variablen
        """
        self._status = 0
        self.func = ""
        self._file_data = tuple()

    @property
    def Status(self) -> int:
        """
        Status Status der Letzten Funktion ausgeben
                    Bedeutung der Werte:
                                                        -> -4 Exception FileNotFound
                                                        -> -2 Daten stimmen nicht überein
                                                        -> -1 Keine Daten 
                                                        -> 0 Nicht ausgeführt
                                                        -> 1 Erfolgreich Bearbeitet

        Returns:
            int: Ausgabe des Status Wertes 
        """
        return self._status

    def __str__(self) -> str:
        """
        __str__ Ausgabe des Exit Codes "Status" Informationen

        Returns:
            str: Übergabe Status String
        """
        return f'{__class__.__name__} :{self._func}: wurde mit Exit Code {self._status} Ausgeführt!'

    @property
    def readFile(self) -> Tuple[str]:
        """
        readFile Get funktion unter funktion wird ausgeführt und wert zurück gegeben

        Returns:
            Tuple[str]: Es wird ein Tuple Returned. Daten ist bereits gestripped.
        """
        return self._get_file_data()

    @readFile.setter
    def readFile(self, path_and_encoding: str) -> None:
        """
        readFile [summary]

        Args:
            path_and_encoding (str): Es werden zwei Daten erwartet und diese werden hier aufgeteilt.
                                                     Muss wie Folgt übergeben werden -> readFile = (path,encoding)

        Returns:
            None: Nur bei einer expetion wird return ausgeführt damit nichts weiteres ausgeführt wird.
        """
        self._status = 0
        self._func = ""
        self._file_data = list(self._file_data).clear()
        try:
            path, encoding = path_and_encoding
        except ValueError:
            self._status = -2
            print("Es müssen zwei Parameter übergeben werden/ Anzahl stimmt nicht")
            return None
        if path is None:
            self._status = -1
        elif encoding == "utf-16":
            self._func = "readFile_utf16"
            self._set_File_data_utf16(path)
        else:
            self._status = -1
            print("Kein Encoding angegeben")

    @readFile.deleter
    def readFile(self) -> None:
        """
        readFile Unterfunktion wird ausgeführt.
        """
        self._clear_readFile()

    def _set_File_data_utf16(self, path: str) -> None:
        """
        _set_File_data_utf16 [summary]

        Args:
            path (str): Datei Pfad wird übegeben um file auszulesen.

        Returns:
            None: Nur bei einer expetion wird return ausgeführt damit nichts weiteres ausgeführt wird.
        """
        try:
            with open(path, "r", newline="", encoding="utf-16") as file:
                self._file_data = tuple(map(lambda x: x.strip(), file))
            self._status = 1
        except FileNotFoundError:
            self._file_data = list(self._file_data.clear())
            print("FileNotFoundError")
            self.status = -4
            return None

    def _get_file_data(self) -> Tuple[str]:
        """
        _get_file_data Unterfunktion zum übergeben der Daten

        Returns:
            Tuple[str]: Tuple mit strings.
        """
        return self._file_data

    def _clear_readFile(self) -> None:
        """
        _clear_readFile Daten werden zurück gesetzt.
        """
        self._file_data = list(self._file_data.clear())
        self._status = 0
        self._func = ""


class writeFile:
    pass