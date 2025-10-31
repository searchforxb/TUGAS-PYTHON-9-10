"""
app.py - CLI utama student_performance_tracker
Jalankan: python app.py
"""

import os
import csv
from tracker.rekap_kelas import RekapKelas
from tracker.report import build_markdown_report, save_text, export_html

DATA_DIR = "data"
OUT_DIR = "out"


def prompt(msg):
    return input(msg + " ").strip()


def load_sample_data(rk):
    """Helper: load from data CSVs bila ada."""
    att = os.path.join(DATA_DIR, "attendance.csv")
    grd = os.path.join(DATA_DIR, "grades.csv")

    # Cegah error jika data sudah dimuat
    if rk._records:
        print("⚠️  Data sudah dimuat sebelumnya, tidak perlu memuat ulang.")
        return

    rk.load_from_csv(attendance_csv_path=att, grades_csv_path=grd)
    print("✅ Data dimuat dari CSV (jika file ada).")



# ======================
# 🔹 AUTO SAVE FUNCTIONS
# ======================

def save_attendance_to_csv(rk):
    """Simpan semua data ke data/attendance.csv."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, "attendance.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nim", "nama", "hadir_persen"])
        for nim, rec in rk._records.items():
            mhs = rec["mhs"]
            writer.writerow([mhs.nim, mhs.nama, mhs.hadir_persen])


def save_grades_to_csv(rk):
    """Simpan semua data ke data/grades.csv."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, "grades.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nim", "quiz", "tugas", "uts", "uas"])
        for nim, rec in rk._records.items():
            nilai = rec["nilai"]
            writer.writerow([nim, nilai.quiz, nilai.tugas, nilai.uts, nilai.uas])


def auto_save_all(rk):
    """Helper: simpan presensi + nilai sekaligus."""
    save_attendance_to_csv(rk)
    save_grades_to_csv(rk)


def show_menu():
    print("=== Student Performance Tracker ===")
    print("1) Muat data dari CSV")
    print("2) Tambah mahasiswa")
    print("3) Ubah presensi")
    print("4) Ubah nilai")
    print("5) Lihat rekap")
    print("6) Simpan laporan Markdown")
    print("7) Export HTML")
    print("8) Filter: tampilkan nilai < 70")
    print("9) Keluar")


def input_nim():
    return prompt("Masukkan NIM:")


def main():
    rk = RekapKelas()
    while True:
        show_menu()
        choice = prompt("Pilih nomor")
        if choice == "1":
            load_sample_data(rk)

        elif choice == "2":
            nim = prompt("NIM:")
            nama = prompt("Nama:")
            hadir = prompt("Hadir (%) [0-100] (kosong=0):")
            try:
                rk.tambah_mahasiswa(nim, nama, float(hadir) if hadir else 0)
                auto_save_all(rk)
                print("✅ Mahasiswa ditambahkan dan disimpan ke data/attendance.csv")
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            nim = input_nim()
            hadir = prompt("Masukkan hadir (%) baru:")
            try:
                rk.set_hadir(nim, float(hadir))
                save_attendance_to_csv(rk)
                print("✅ Presensi diperbarui dan disimpan.")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            nim = input_nim()
            quiz = prompt("Quiz (kosong untuk lewati):")
            tugas = prompt("Tugas (kosong untuk lewati):")
            uts = prompt("UTS (kosong untuk lewati):")
            uas = prompt("UAS (kosong untuk lewati):")
            kwargs = {}
            if quiz != "": kwargs['quiz'] = float(quiz)
            if tugas != "": kwargs['tugas'] = float(tugas)
            if uts != "": kwargs['uts'] = float(uts)
            if uas != "": kwargs['uas'] = float(uas)
            try:
                rk.set_penilaian(nim, **kwargs)
                save_grades_to_csv(rk)
                print("✅ Nilai diperbarui dan disimpan ke data/grades.csv.")
            except Exception as e:
                print("Error:", e)

        elif choice == "5":
            recs = rk.rekap()
            if not recs:
                print("Belum ada data.")
            else:
                print("| NIM | Nama | Hadir (%) | Nilai Akhir | Predikat |")
                for r in recs:
                    print(f"| {r['nim']} | {r['nama']} | {r['hadir']:.1f} | {r['nilai_akhir']:.2f} | {r['predikat']} |")

        elif choice == "6":
            recs = rk.rekap()
            md = build_markdown_report(recs)
            outpath = os.path.join(OUT_DIR, "report.md")
            save_text(outpath, md)
            print("📄 Laporan Markdown disimpan di", outpath)

        elif choice == "7":
            recs = rk.rekap()
            outpath = os.path.join(OUT_DIR, "report.html")
            export_html(recs, outpath)
            print("🌐 Laporan HTML disimpan di", outpath)

        elif choice == "8":
            recs = rk.rekap(filter_below_70=True)
            if not recs:
                print("Tidak ada mahasiswa dengan nilai < 70.")
            else:
                print("Mahasiswa dengan nilai < 70:")
                for r in recs:
                    print(f"{r['nim']} - {r['nama']} -> {r['nilai_akhir']:.2f} ({r['predikat']})")

        elif choice == "9" or choice.lower() in ("q", "exit"):
            print("Keluar. Sampai jumpa! 👋")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
