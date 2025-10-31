"""
Module mahasiswa: berisi kelas Mahasiswa
"""
class Mahasiswa:
    """
    Representasi data mahasiswa.
    Atribut publik: nim, nama
    Atribut privat: _hadir_persen
    Gunakan property hadir_persen untuk validasi 0-100.
    """
    def __init__(self, nim, nama, hadir_persen=0):
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0
        self.hadir_persen = hadir_persen

    @property
    def hadir_persen(self):
        """Mengembalikan persentase kehadiran."""
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        """Set dan validasi kehadiran: harus antara 0 dan 100."""
        try:
            val = float(value)
        except Exception:
            raise ValueError("hadir_persen harus berupa angka (0-100).")
        if val < 0 or val > 100:
            raise ValueError("hadir_persen harus antara 0 dan 100.")
        self._hadir_persen = val

    def info(self):
        """Mengembalikan string singkat profil mahasiswa."""
        return f"{self.nim} - {self.nama} (Hadir: {self.hadir_persen}%)"
