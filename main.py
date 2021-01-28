import sys

data1 = "[MSR:RECORD];1;G11000;BST_LIB_MSR;M_ANA;B-2;Hub P-10;;256;1;;;;2"
data2 = "[UID:ACCMSR];6;ADMIN;3;GUEST;1;NORMALER USER;3;BETRIEB;1;LYSE;1;SALZ;1"
data3 = "[LAD:BSINST];71;5;M_ANA;BST_LIB_EXT;5;18;12;9;0;0;1;1;13"
data4 = "[LAD:MSR_REF];G11000"
data5 = "[PARA:PARADATA];98;OScan;5;CHECK;1;j;Mba;5;FLOAT;3;0.0;Mbe;5;FLOAT;5;100.0;Dim;3;DIM;1;%;Gw1;5;FLOAT;0;;Hy1;5;FLOAT;3;3.0;Lf1;5;CHECK;1;n;Gw2;5;FLOAT;0;;Hy2;5;FLOAT;3;3.0;Lf2;5;CHECK;1;n;Gw3;5;FLOAT;0;;Hy3;5;FLOAT;3;3.0;Lf3;5;CHECK;1;n;Gw4;5;FLOAT;0;;Hy4;5;FLOAT;3;3.0;Lf4;5;CHECK;1;n;ResMon;5;CHECK;1;n;Gt1;13;CUSTSELLIST_1;1;0;Mp1;5;MPRIO;1;-;Mt1;5;MTEXT;0;;Gt2;13;CUSTSELLIST_1;1;0;Mp2;5;MPRIO;1;-;Mt2;5;MTEXT;0;;Gt3;13;CUSTSELLIST_1;1;0;Mp3;5;MPRIO;1;-;Mt3;5;MTEXT;0;;Gt4;13;CUSTSELLIST_1;1;0;Mp4;5;MPRIO;1;-;Mt4;5;MTEXT;0;;Wav1;5;HTEXT;0;;Ast1;5;ASTAT;0;;Ht1;5;HTEXT;0;;Bz1;3;BZO;0;;Wav2;5;HTEXT;0;;Ast2;5;ASTAT;0;;Ht2;5;HTEXT;0;;Bz2;3;BZO;0;;Wav3;5;HTEXT;0;;Ast3;5;ASTAT;0;;Ht3;5;HTEXT;0;;Bz3;3;BZO;0;;Wav4;5;HTEXT;0;;Ast4;5;ASTAT;0;;Ht4;5;HTEXT;0;;Bz4;3;BZO;0;;BEDSEL;5;CHECK;0;;ChgShw;5;CHECK;0;;Alex0;5;CHECK;0;;Alq0;5;CHECK;0;;Alex1;5;CHECK;0;;Alq1;5;CHECK;0;;Alex2;5;CHECK;0;;Alq2;5;CHECK;0;;Alex3;5;CHECK;0;;Alq3;5;CHECK;0;;Alex4;5;CHECK;0;;Alq4;5;CHECK;0;;Al_dh_ex;5;CHECK;0;;Al_dhh_ex;5;CHECK;0;;Al_dl_ex;5;CHECK;0;;Al_dll_ex;5;CHECK;0;;Aval1;5;FLOAT;0;;Aval2;5;FLOAT;0;;Aval3;5;FLOAT;0;;Aval4;5;FLOAT;0;;Lbg1;5;CHECK;0;;Lbg2;5;CHECK;0;;Lbg3;5;CHECK;0;;Lbg4;5;CHECK;0;;Lw;5;FLOAT;0;;CycleOne;5;CHECK;0;;Init;5;CHECK;0;;Acnt;4;WORD;0;;Align;4;WORD;0;;ATt1;7;DMSTIME;0;;ITt1;7;DMSTIME;0;;CAst1;4;BYTE;0;;OAst1;4;BYTE;0;;Nlst1;4;BYTE;0;;Align1;4;BYTE;0;;ATt2;7;DMSTIME;0;;ITt2;7;DMSTIME;0;;CAst2;4;BYTE;0;;OAst2;4;BYTE;0;;Nlst2;4;BYTE;0;;Align2;4;BYTE;0;;ATt3;7;DMSTIME;0;;ITt3;7;DMSTIME;0;;CAst3;4;BYTE;0;;OAst3;4;BYTE;0;;Nlst3;4;BYTE;0;;Align3;4;BYTE;0;;ATt4;7;DMSTIME;0;;ITt4;7;DMSTIME;0;;CAst4;4;BYTE;0;;OAst4;4;BYTE;0;;Nlst4;4;BYTE;0;;Align4;4;BYTE;0;"


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
        para_data = new_para_data[2:].copy()
        for count, element in enumerate(para_data, start=0):
            if count % 5 == 0:
                self.read_out.update({element: para_data[count:count + 5]})
        return self.read_out

    def _get_Sections(self):
        return self.read_out
