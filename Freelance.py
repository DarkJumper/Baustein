from typing import List, Dict, Tuple, Union
from help_dec import *


class FreelanceBase:
    """
    Zerlegen der "Base" Elementen aus Freelance in ihre einzelteile.
    """

    def __init__(self) -> None:
        """
        __init__ Initalisieren alle default werte
        """
        self._status = 0
        # Fester wert weil es immer nur 16 bzw. 17 bereiche gibt.
        self.default_area_size = 17
        self._proj = dict()
        self._user = list()
        self._area = dict()
        # Wird genutzt um funktions name bei bedarf mit exit code auszugeben.
        self._func = ""

    def __str__(self) -> str:
        """
        __str__ Ausgabe des Exit Codes "Status" Informationen

        Returns:
            str: Übergabe Status String
        """
        return f'{__class__.__name__} :{self._func}: wurde mit Exit Code {self._status} Ausgeführt!'

    @property
    def Status(self) -> int:
        """
        Status Status der Letzten Funktion ausgeben
                    Bedeutung der Werte:
                                                        -> -4 Exception Value Error Verweist auf falsche übergabe Parameter 
                                                        -> -3 Länge der Parameter stimmen nicht 
                                                        -> -2 Daten Abschnitte passen nicht überein 
                                                        -> -1 Keine Daten 
                                                        -> 0 Nicht ausgeführt
                                                        -> 1 Erfolgreich Bearbeitet

        Returns:
            int: Ausgabe des Status Wertes 
        """
        return self._status

    @property
    def Projekt(self) -> Dict[str, str]:
        """
        Projekt Rückgabe der funktion _get_Projekt

        Returns:
            Dict[str]: Rückgabe des Projekt Dicts. 
        """
        return self._get_Projekt()

    @Projekt.setter
    def Projekt(self, new_data: Union[List[str], str]) -> None:
        """
        Projekt Wird nach None der unteren Funktion eingefügt

        Args:
            new_data (Union[List[str], str]): Übergabe einer Liste mit BEGIN_PROJECTHEADER daten, diese werden Kopiert und weiter übergeben oder String wird zur liste und dann übergeben.
        """
        self._func = "Projekt"
        if new_data == None:
            self._status = -1
        elif type(new_data) == str:
            self._status = 0
            splitted_new_data = new_data.split(";")
            self._set_Projekt(splitted_new_data)
        else:
            self._status = 0
            copyed_data = new_data.copy()
            self._set_Projekt(copyed_data)

    @Projekt.deleter
    def Projekte(self) -> None:
        """
        Projekte Aufrufen Unterfunktion zum löschen vom Status
        """
        self._clear_Projekt()

    def _get_Projekt(self) -> Dict[str, str]:
        """
        _get_Projekt Unterfunktion für übergabe der werte

        Returns:
            Dict[str]: Rückgabe von self.proj bei None wird ein leeres Dict returned
        """
        return self._proj

    def _set_Projekt(self, new_data: List[str]) -> None:
        """
        _set_Projekt Setzten des self.proj dicts.
                            Im Dict befindet sich der Name -> Komentar -> Creator -> Company -> Version -> CreatDatum 
                            Diese Daten werden aus der Eingegeben Header Liste Ausgelesen

        Args:
            new_data (List[str]): Übergabe der vorher copierten daten
        """
        creation_date = f'{new_data[9]}.{new_data[8]}.{new_data[7]}'
        version = new_data[33]
        self._proj = {
            "Name": new_data[1],
            "Komi": new_data[2],
            "Creator": new_data[3],
            "Company": new_data[14],
            "Version": version,
            "CDate": creation_date
            }
        self._status = 1

    def _clear_Projekt(self) -> None:
        """
        _clear_Projekt Leeren von self.proj und zurücksetzten Status
        """
        self._func = ""
        self._proj.clear()
        self._status = 0

    @property
    def User(self) -> Tuple[str]:
        """
        User Daten aus self.user werden ausgegeben 

        Returns:
            Tuple[str]: Es wird ein Tuple ausgeben von self.user
        """
        return tuple(self._get_User())

    @User.setter
    def User(self, new_data: Union[List[str], str]) -> None:
        """
        User Wird nach None und summe an daten gesucht, wenn was gefunden wird es von der unteren Funktion eingefügt

        Args:
            new_data (Union[List[str], str]): Übergabe einer Liste mit ACC:NODE daten, diese werden Kopiert und Übergeben oder String wird zur liste und dann übergeben.
        """
        if new_data == None:
            self._status = -1
        elif type(new_data) == str:
            self._status = 0
            splitted_new_data = new_data.split(";")
            self._set_User(splitted_new_data)
        else:
            self._status = 0
            copy_new_data = new_data.copy()
            self._set_User(copy_new_data)

    @User.deleter
    def User(self) -> None:
        """
        User Bei Ausführen wird Unterfunktion ausgeführt
        """
        self._clear_User()

    def _get_User(self) -> List[str]:
        """
        _get_User Unterklasse für get funktion.

        Returns:
            List[str]: Rückgabe der self.user enthalten daten
        """
        return self._user

    def _set_User(self, new_data: List[str]) -> None:
        """
        _set_User Falls noch keine Daten bekannt wird self.user befüllt ansonsten wird nach gesehen ob bereits ein eintrag vorhanden ist.

        Args:
            new_data (List[str]): Es wird eine Liste von Strings übergeben

        Returns:
            None: Es wird nichts übergeben. Es wird nur der status geändert da ein falscher wert übergeben worden ist.
        """
        try:
            self._func = "User"
            if int(new_data[1]) == 0:
                self._status = 1
            elif int(new_data[1]) != len(new_data[2:]) / 2:
                self._status = -3
            elif len(self._user) == 0:
                self._user = new_data[2::2].copy()
                self._status = 1
            elif len(self._user) > 0:
                for user in range(2, (int(new_data[1]) + 1) * 2, 2):
                    if new_data[user] in self._user:
                        continue
                    else:
                        self._user.append(new_data[user])
                        self._status = 1
        except ValueError:
            self._user.clear()
            self._status = -4
            print("Value Error")
            return None

    def _clear_User(self) -> None:
        """
        _clear_User Daten werden gelöscht und status zurück gesetzt.
        """
        self._func = ""
        self._user.clear()
        self._status = 0

    @property
    def Area(self) -> Dict[int, tuple]:
        """
        Area Übergeordnete Funktion zuständig für die Rückgabe unterfunktion

        Returns:
            Dict[int, tuple]: Es wird ein Dict übergeben mit folgendem aufbau Dict{int: (str,str)}
        """
        return self._get_Area()

    @Area.setter
    def Area(self, new_data: List[list[str]]) -> None:
        """
        Area Übergeordnete Funktion. Auswertung der Input Liste.

        Args:
            new_data (List[list[str]]): Liste wird angepasst falls listen größe nicht stimmt wird status geändert
        """
        if new_data is None:
            self._status = -1
        elif len(new_data) == self.default_area_size + 2:
            copyed_new_data = new_data[1:-1].copy()
            self._set_Area(copyed_new_data)
        elif len(new_data) != self.default_area_size:
            self._status = -3
        else:
            copyed_new_data = new_data.copy()
            self._set_Area(copyed_new_data)

    @Area.deleter
    def Area(self) -> None:
        """
        Area Bei Ausführen wird Unterfunktion ausgeführt
        """
        self._clear_Area()

    def _get_Area(self) -> Dict[int, tuple]:
        """
        _get_Area Untergeordnete funktion returned self.area

        Returns:
            Dict[int, tuple]: Es wird ein Dict übergeben mit folgendem aufbau Dict{int: (str,str)}
        """
        return self._area

    def _set_Area(self, new_data: List[list[str]]) -> None:
        """
        _set_Area Daten werden hier gespiltet und ins dict richtig eingefügt.
                        Key ist in Zweier Potenz abwärts geordnert
                        Dict -> {65536 : ("Area", "Name)}

        Args:
            new_data (List[list[str]]): Wenn parameter stimmen werden diese vorher kopiert.

        Returns:
            None: Es wird nichts übergeben. Es wird nur der status geändert da ein falscher wert übergeben worden ist.
        """
        self._func = "Area"
        try:
            for count, areas in enumerate(new_data, start=-self.default_area_size + 1):
                splitted_areas = areas.split(";")
                if int(splitted_areas[-2]) != len(splitted_areas[-1]) or int(splitted_areas[1]) == 0:
                    self._status = -2
                else:
                    self._area[2**abs(count)] = (splitted_areas[-3], splitted_areas[-1])
                    self._status = 1
        except ValueError:
            self._area.clear()
            self._status = -4
            print("Value Error")
            return None

    def _clear_Area(self) -> None:
        """
        _clear_Area Daten werden gelöscht und der Status wird zurück gesetzt
        """
        self._func = ""
        self._area.clear()
        self.area_size = 16
        self._status = 0


class MsrData:
    """
    Zerlegen der Para-Data Daten in ihre einzelteile.
    """

    def __init__(self) -> None:
        """
        __init__ Initalisieren der leeren Daten Dicts.
        """
        self._para_analyse = dict()
        self._msr_acc = dict()
        self._msr_rec = dict()
        self._status = 0
        # Wird genutzt um funktions name bei bedarf mit exit code auszugeben.
        self._func = ""

    def __str__(self) -> str:
        """
        __str__ Ausgabe des Exit Codes "Status" Informationen

        Returns:
            str: Übergabe Status String
        """
        return f'{__class__.__name__} :{self._func}: wurde mit Exit Code {self._status} Ausgeführt!'

    @property
    def Status(self) -> int:
        """
        Status Status der Letzten Funktion ausgeben
                    Bedeutung der Werte:
                                                        -> -4 Exception Value Error Verweist auf falsche übergabe Parameter 
                                                        -> -3 Länge der Parameter stimmen nicht 
                                                        -> -2 Daten Abschnitte passen nicht überein 
                                                        -> -1 Keine Daten 
                                                        -> 0 Nicht ausgeführt
                                                        -> 1 Erfolgreich Bearbeitet

        Returns:
            int: Ausgabe des Status Wertes 
        """
        return self._status

    @property
    def Parameter(self) -> Dict[str, tuple]:
        """
        Sections Die daten aus read_out wird Ausgegeben.

        Returns:
            _get_Sections (dict): Es wird das keywort mit den dazu gehörigen 4 angaben zurückgegeben.
        """
        return self._get_Parameter()

    @Parameter.setter
    def Parameter(self, new_para_data: Union[List[str], str]) -> None:
        """
        Sections Eine setter funktion zum einlesen der dateien ins dict read_out

        Args:
            new_para_data (Union[List[str], str]): Übergabe einer Liste mit Para Data daten, diese werden Kopiert und Übergeben oder String wird zur liste und dann übergeben.
        """
        if new_para_data is None:
            self._status = -1
        elif type(new_para_data) == str:
            self._status = 0
            splitted_new_para_data = new_para_data.split(";")
            self._set_Parameter(splitted_new_para_data)
        else:
            self._status = 0
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
            
        Returns:
            None: Es wird nichts übergeben. Es wird nur der status geändert da ein falscher wert übergeben worden ist.
        """
        self._func = "Parameter"
        try:
            if int(new_para_data[1]) != len(new_para_data[2::5]):
                self._status = -3
            else:
                para_data = tuple(new_para_data[2:])
                for count, element in enumerate(para_data, start=0):
                    if count % 5 == 0:
                        self._para_analyse[element] = para_data[count:count + 5]
                self._status = 1
        except ValueError:
            self._para_analyse.clear()
            print("ValueError")
            self._status = -4
            return None

    def _get_Parameter(self) -> Dict[str, tuple]:
        """
        _get_Parameter Eine getter funktion für die rückgabe der daten.

        Returns:
            read_out (dict): Ausgabe dict wird ein klassen dict returned dieses kann nur über die setter methode geändert werden.
        """
        return self._para_analyse

    def _clean_Parameter(self) -> None:
        """
        _clean_Parameter Das dict wird bereinigt.
        """
        self._func = ""
        self._para_analyse.clear()
        self._status = 0

    @property
    def Access(self) -> Dict[str, int]:
        """
        Access Ausgabe der Zusammen gefassten Daten wenn keine Daten vorher übergeben worden wird ein leeres Dict übergeben.

        Returns:
            Dict[str, int]: Es wird ein Dict übergeben wo der Value den Zugriff zu weist 1= nur sehen und 3= steuern und sehen.
        """
        return self._get_Access()

    @Access.setter
    def Access(self, new_acc_msr: Union[List[str], str]) -> None:
        """
        Access Print befehl zum schnellen erkennen der Ausführung und übergabe in unter funktionen zum beschreiben des self.msr_acc

        Args:
            new_acc_msr (Union[List[str], str]): Übergabe einer Liste mit acc daten, diese werden Kopiert und Übergeben oder String wird zur liste und dann übergeben.
        """
        if new_acc_msr is None:
            self._status = -1
        elif type(new_acc_msr) == str:
            self._status = 0
            splitted_new_acc_msr = new_acc_msr.split(";")
            self._set_Access(splitted_new_acc_msr)
        else:
            self._status = 0
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
        return self._msr_acc

    def _set_Access(self, new_acc_msr: List[str]) -> None:
        """
        _set_Access Zerlegen des Access und beschreiben des Dicts!

        Args:
            new_acc_msr (List[str]): liste von ACCMSR muss übergeben werden.

        Returns:
            None: Es wird nichts übergeben. Es wird nur der status geändert da ein falscher wert übergeben worden ist.
        """
        self._func = "Access"
        try:
            if int(new_acc_msr[1]) != len(new_acc_msr[2::2]):
                self._status = -2
            else:
                acc_msr = tuple(new_acc_msr[2:])
                for count, element in enumerate(acc_msr, start=0):
                    if count % 2 == 0:
                        self._msr_acc[element] = int(acc_msr[count + 1])
                self._status = 1
        except ValueError:
            self._msr_acc.clear()
            print("ValueError")
            self._status = -4
            return None

    def _clean_Access(self) -> None:
        """
        _clean_Access Bereinigen des self.msr_acc Dicts.
        """
        self._func = ""
        self._msr_acc.clear()
        self._status = 0

    @property
    def Record(self) -> Dict[str, str]:
        """
        Record Ausgabe der zusammengefassten Daten des MSR Record in einem Dict

        Returns:
            Dict[str, str]: Rückgabe des Daten string.
        """
        return self._get_Record()

    @Record.setter
    def Record(self, new_msr_rec: Union[List[str], str]) -> None:
        """
        Record Übergabe in unterfunktionen daten (Liste) wird vorher kopiert

        Args:
            new_msr_rec (Union[List[str], str]): Es wird eine Liste mit Strings erwartet ,dieser wird Kopiert und übergeben. Falls ein String übergeben wird, wird dieser umgeandelt und übergeben. 
        """
        if new_msr_rec is None:
            self._status = -1
        elif type(new_msr_rec) == str:
            self._status = 0
            splitted_new_msr_rec = new_msr_rec.split(";")
            self._set_Record(splitted_new_msr_rec)
        else:
            self._status = 0
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
        return self._msr_rec

    def _set_Record(self, new_msr_rec: List[str]) -> None:
        """
        _set_Record [summary]

        Args:
            new_msr_rec (List[str]): Es wird eine Liste mit Strings erwartet.  Hier sollte nur eine Liste übergeben werden von MSR:RECORD

        Returns:
            None: Es wird nichts übergeben. Es wird nur der status geändert da ein falscher wert übergeben worden ist.
        """
        self._func = "Record"
        try:
            if int(new_msr_rec[1]) != 1:
                self._status = -2
            else:
                rec_msr = tuple(new_msr_rec[2:])
                self._msr_rec["MN"] = rec_msr[0]
                self._msr_rec["LB"] = rec_msr[1]
                self._msr_rec["BT"] = rec_msr[2]
                self._msr_rec["KT"] = rec_msr[3]
                self._msr_rec["LT"] = rec_msr[4]
                self._msr_rec["AB"] = rec_msr[6]
                self._msr_rec["ST"] = rec_msr[7]
                self._status = 1
        except ValueError:
            self._msr_rec.clear()
            print("ValueError")
            self._status = -4
            return None

    def _clean_Record(self) -> None:
        """
        _clean_Record Bereinigen der Daten self.msr_rec
        """
        self._func = ""
        self._msr_rec.clear()
        self._status = 0
