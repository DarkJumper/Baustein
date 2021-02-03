from typing import List, Dict


class ParaData:
    """
    Zerlegen der eingegebenen Daten in ihre einzelteile.
    Es wird immer in 4 paare zerteilt.
    """

    def __init__(self) -> None:
        self.read_out = dict()

    @property
    def Sections(self) -> Dict[str, tuple]:
        """
        Sections Die daten aus read_out wird Ausgegeben.

        Returns:
            _get_Sections (dict): Es wird das keywort mit den dazu gehörigen 4 angaben zurückgegeben.
        """
        return self._get_Sections()

    @Sections.setter
    def Sections(self, new_para_data: List[str]) -> Dict[str, tuple]:
        """
        Sections Eine setter funktion zum einlesen der dateien ins dict read_out

        Args:
            new_para_data (list): Para_data wird eingegeben dies wird direkt in der funktion copiert.

        Returns:
            _set_Sections (dict): Rückgabe des Setter werts
        """
        return self._set_Sections(new_para_data)

    @Sections.deleter
    def Sections(self) -> Dict[str, tuple]:
        """
        Sections Es wird der read_out gecleart.

        Returns:
            None: Das gesetzt signal wird gelöscht.
        """
        return self._clean_Sections()

    def _set_Sections(self, new_para_data: List[str]) -> Dict[str, tuple]:
        """
        _set_Sections Die Liste wird in einzelnen Teile zerleft dies sind immer 4 lang.

        Args:
            new_para_data (list): para data wird eingegeben dies wird direkt in der funktion Kopiert.
            Startpunkt der Liste muss von außen vorgegeben werden. 
            Es sollte am besten eine Kopie übergeben werden.

        Returns:
            read_out (dict): Setter wird zurück gegeben.
        """
        if new_para_data is None:
            return self.read_out
        else:
            para_data = tuple(new_para_data)
        for count, element in enumerate(para_data, start=0):
            if count % 5 == 0:
                self.read_out[element] = para_data[count:count + 5]
        return self.read_out

    def _get_Sections(self) -> Dict[str, tuple]:
        """
        _get_Sections Eine getter funktion für die rückgabe der daten.

        Returns:
            read_out (dict): Ausgabe dict wird ein klassen dict returned dieses kann nur über die setter methode geändert werden.
        """
        return self.read_out

    def _clean_Sections(self) -> Dict[str, tuple]:
        """
        _clean_Sections Das dict wird bereinigt.

        Returns:
            None: Es wird das dict gecleart.
        """
        return self.read_out.clear()
