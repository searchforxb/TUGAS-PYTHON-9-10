from .mahasiswa import Mahasiswa
from .penilaian import Penilaian
import csv

class RekapKelas:
    """Mengelola kumpulan Mahasiswa dan Penilaian mereka."""

    def __init__(self):
        self._records = {}

    def tambah_mahasiswa(self, nim, nama, hadir_persen=0):
        if nim in self._records:
            raise KeyError(f"Mahasiswa dengan NIM {nim} sudah ada.")
        self._records[nim] = {"mhs": Mahasiswa(nim, nama, hadir_persen), "nilai": Penilaian()}

    def set_hadir(self, nim, persen):
        if nim not in self._records:
            raise KeyError("NIM tidak ditemukan.")
        self._records[nim]["mhs"].hadir_persen = persen

    def set_penilaian(self, nim, quiz=None, tugas=None, uts=None, uas=None):
        if nim not in self._records:
            raise KeyError("NIM tidak ditemukan.")
        p = self._records[nim]["nilai"]
        if quiz is not None: p.quiz = quiz
        if tugas is not None: p.tugas = tugas
        if uts is not None: p.uts = uts
        if uas is not None: p.uas = uas

    def predikat(self, nilai):
        if nilai >= 85: return "A"
        elif nilai >= 75: return "B"
        elif nilai >= 65: return "C"
        elif nilai >= 50: return "D"
        else: return "E"

    def rekap(self, filter_below_70=False):
        hasil = []
        for nim, d in self._records.items():
            nilai_akhir = d["nilai"].nilai_akhir()
            data = {
                "nim": nim,
                "nama": d["mhs"].nama,
                "hadir": d["mhs"].hadir_persen,
                "nilai_akhir": round(nilai_akhir, 2),
                "predikat": self.predikat(nilai_akhir)
            }
            if not filter_below_70 or nilai_akhir < 70:
                hasil.append(data)
        return hasil

    def load_from_csv(self, attendance_csv_path, grades_csv_path):
        try:
            with open(attendance_csv_path, newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    self.tambah_mahasiswa(row["nim"], row["nama"], float(row["hadir_persen"]))
        except FileNotFoundError:
            pass
        try:
            with open(grades_csv_path, newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    self.set_penilaian(row["nim"], float(row["quiz"]), float(row["tugas"]),
                                       float(row["uts"]), float(row["uas"]))
        except FileNotFoundError:
            pass
