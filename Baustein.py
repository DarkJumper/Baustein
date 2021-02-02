class ParaData:

    def __init__(self) -> None:
        self.read_out = {}

    @property
    def Sections(self):
        return self._get_Sections()

    @Sections.setter
    def Sections(self, new_para_data):
        return self._set_Sections(new_para_data)

    def _set_Sections(self, new_para_data):
        self.read_out = {}
        para_data = tuple(new_para_data[2:].copy())
        for count, element in enumerate(para_data, start=0):
            if count % 5 == 0:
                self.read_out.update({element: para_data[count:count + 5]})
        return self.read_out

    def _get_Sections(self):
        return self.read_out