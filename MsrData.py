from typing import List, Dict
from help_dec import *


class MsrData:
    """
    Zerlegen der Para-Data Daten in ihre einzelteile.
    Status ->-2: Daten Abschnitte passen nicht überein. -1: Enthält keine Daten 1: Erfolgreich Bearbeitet.  0:Wurde noch nicht Bearbeitet  
    """

    def __init__(self) -> None:
        """
        __init__ Initalisieren der leeren Daten Dicts.
        """
        self.para_analyse = dict()
        self.msr_acc = dict()
        self.msr_rec = dict()
        self.status = 0

    @property
    def Parameter(self) -> Dict[str, tuple]:
        """
        Sections Die daten aus read_out wird Ausgegeben.

        Returns:
            _get_Sections (dict): Es wird das keywort mit den dazu gehörigen 4 angaben zurückgegeben.
        """
        return self._get_Parameter()

    @Parameter.setter
    def Parameter(self, new_para_data: List[str]) -> None:
        """
        Sections Eine setter funktion zum einlesen der dateien ins dict read_out

        Args:
            new_para_data (list): Para_data wird eingegeben dies wird direkt in der funktion copiert.
        """
        if new_para_data is None:
            self.status = -1
        else:
            new_para_data_copy = new_para_data.copy()
            self._set_Parameter(new_para_data_copy)

    @Parameter.deleter
    def Parameter(self) -> None:
        """
        Sections Es wird der read_out gecleart.
        """
        self._clean_Parameter()

    def _set_Parameter(self, new_para_data: List[str]) -> None:
        """
        _set_Parameter Die Liste wird in einzelnen Teile zerleft dies sind immer 4 lang.

        Args:
            new_para_data (list): para data wird eingegeben dies wird direkt in der funktion Kopiert.
            Startpunkt der Liste muss von außen vorgegeben werden. 
            Es sollte am besten eine Kopie übergeben werden.
        """
        if int(new_para_data[1]) == len(new_para_data[2::5]):
            para_data = tuple(new_para_data[2:])
            for count, element in enumerate(para_data, start=0):
                if count % 5 == 0:
                    self.para_analyse[element] = para_data[count:count + 5]
            self.status = 1
        else:
            self.status = -2
        print(f'{__class__.__name__}: wurde mit Exit Code {self.status} Ausgeführt!')

    def _get_Parameter(self) -> Dict[str, tuple]:
        """
        _get_Parameter Eine getter funktion für die rückgabe der daten.

        Returns:
            read_out (dict): Ausgabe dict wird ein klassen dict returned dieses kann nur über die setter methode geändert werden.
        """
        return self.para_analyse

    def _clean_Parameter(self) -> None:
        """
        _clean_Parameter Das dict wird bereinigt.
        """
        self.para_analyse.clear()
        self.status = 0

    @property
    def Access(self) -> Dict[str, int]:
        """
        Access Ausgabe der Zusammen gefassten Daten wenn keine Daten vorher übergeben worden wird ein leeres Dict übergeben.

        Returns:
            Dict[str, int]: Es wird ein Dict übergeben wo der Value den Zugriff zu weist 1= nur sehen und 3= steuern und sehen.
        """
        return self._get_Access()

    @Access.setter
    def Access(self, new_acc_msr: List[str]) -> None:
        """
        Access Print befehl zum schnellen erkennen der Ausführung und übergabe in unter funktionen zum beschreiben des self.msr_acc

        Args:
            new_acc_msr (List[str]): liste von ACCMSR muss übergeben werden.
        """
        if new_acc_msr is None:
            self.status = -1
        else:
            new_acc_msr_copy = new_acc_msr.copy()
            self._set_Access(new_acc_msr_copy)

    @Access.deleter
    def Access(self) -> None:
        """
        Access Ausführung wird im Terminal Angezeigt und das leeren des self.msr_acc dict wird in unter funktion ausgeführt.
        """
        self._clean_Access()

    def _get_Access(self) -> Dict[str, int]:
        """
        _get_Access Daten werden an Hauptfunktion übergeben.

        Returns:
            Dict[str, int]: Daten bestehen aus {User : index} index ist -> 1= Sehen  3= Bedienen und Sehen
        """
        return self.msr_acc

    def _set_Access(self, new_acc_msr: List[str]) -> None:
        """
        _set_Access Zerlegen des Access und beschreiben des Dicts!

        Args:
            new_acc_msr (List[str]): liste von ACCMSR muss übergeben werden.
        """
        if int(new_acc_msr[1]) == len(new_acc_msr[2::2]):
            acc_msr = tuple(new_acc_msr[2:])
            for count, element in enumerate(acc_msr, start=0):
                if count % 2 == 0:
                    self.msr_acc[element] = int(acc_msr[count + 1])
            self.status = 1
        else:
            self.status = -2
        print(f'{__class__.__name__}: wurde mit Exit Code {self.status} Ausgeführt!')

    def _clean_Access(self) -> None:
        """
        _clean_Access Bereinigen des self.msr_acc Dicts.
        """
        self.msr_acc.clear()
        self.status = 0

    @property
    def Record(self) -> Dict[str, str]:
        """
        Record Ausgabe der zusammengefassten Daten des MSR Record in einem Dict

        Returns:
            Dict[str, str]: Rückgabe des Daten string.
        """
        return self._get_Record()

    @Record.setter
    def Record(self, new_msr_rec) -> None:
        """
        Record Übergabe in unterfunktionen daten (Liste) wird vorher kopiert

        Args:
            new_msr_rec ([List]): Es wird eine Liste mit Strings erwartet. Diese wird direkt kopiert. Hier sollte nur eine Liste übergeben werden von MSR:RECORD
        """
        if new_msr_rec is None:
            self.status = -1
        else:
            new_msr_rec_copy = new_msr_rec.copy()
            self._set_Record(new_msr_rec_copy)

    @Record.deleter
    def Record(self) -> None:
        """
        Record Cleart den kompletten self.msr_rec Dict
        """
        self._clean_Record()

    def _get_Record(self) -> Dict[str, str]:
        """
        _get_Record Unterklasse für die Ausgabe der zusammengefassten Daten des MSR Record in einem Dict

        Returns:
            Dict[str, str]: Es wird self.msr_rec daten zurück gegeben dieses Dict enthält folgende keys
            -> MN: Messtellen Name
            -> LB: Baustellen Libary
            -> BT: Baustein Typ
            -> KT: Kurztext
            -> LT: Langtext
            -> AB: Anlagen Bereich
            -> ST: Bearbeitung / Status
        """
        return self.msr_rec

    def _set_Record(self, new_msr_rec) -> None:
        """
        _set_Record Unterfunktionen daten (Liste) wird vorher kopiert

        Args:
            new_msr_rec ([List]): Es wird eine Liste mit Strings erwartet.  Hier sollte nur eine Liste übergeben werden von MSR:RECORD
        """
        if int(new_msr_rec[1]) == 1:
            rec_msr = tuple(new_msr_rec[2:])
            self.msr_rec["MN"] = rec_msr[0]
            self.msr_rec["LB"] = rec_msr[1]
            self.msr_rec["BT"] = rec_msr[2]
            self.msr_rec["KT"] = rec_msr[3]
            self.msr_rec["LT"] = rec_msr[4]
            self.msr_rec["AB"] = rec_msr[6]
            self.msr_rec["ST"] = rec_msr[7]
            self.status = 1
        else:
            self.status = -2
        print(f'{__class__.__name__}: wurde mit Exit Code {self.status} Ausgeführt!')

    def _clean_Record(self) -> None:
        """
        _clean_Record Bereinigen der Daten self.msr_rec
        """
        self.msr_rec.clear()
        self.status = 0
