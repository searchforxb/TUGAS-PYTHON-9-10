class Penilaian:
    """Menyimpan nilai dan menghitung nilai akhir dengan validasi property."""

    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        self._quiz = 0
        self._tugas = 0
        self._uts = 0
        self._uas = 0
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    @property
    def quiz(self):
        return self._quiz

    @quiz.setter
    def quiz(self, value):
        val = float(value)
        if val < 0 or val > 100:
            raise ValueError("Nilai quiz harus antara 0–100")
        self._quiz = val

    @property
    def tugas(self):
        return self._tugas

    @tugas.setter
    def tugas(self, value):
        val = float(value)
        if val < 0 or val > 100:
            raise ValueError("Nilai tugas harus antara 0–100")
        self._tugas = val

    @property
    def uts(self):
        return self._uts

    @uts.setter
    def uts(self, value):
        val = float(value)
        if val < 0 or val > 100:
            raise ValueError("Nilai UTS harus antara 0–100")
        self._uts = val

    @property
    def uas(self):
        return self._uas

    @uas.setter
    def uas(self, value):
        val = float(value)
        if val < 0 or val > 100:
            raise ValueError("Nilai UAS harus antara 0–100")
        self._uas = val

    def nilai_akhir(self):
        """Hitung nilai akhir dari semua komponen"""
        return (self.quiz * 0.15) + (self.tugas * 0.25) + (self.uts * 0.25) + (self.uas * 0.35)
