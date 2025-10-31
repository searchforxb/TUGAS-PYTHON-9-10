Student Performance Tracker

Aplikasi Python berbasis OOP dan modularisasi untuk mengelola data mahasiswa, presensi, dan
nilai.
Struktur Folder
student_performance_tracker/
student_performance_tracker/ 
├─ app.py 
├─ README.md 
├─ requirements.txt           # opsional 
├─ data/ 
│  ├─ attendance.csv 
│  └─ grades.csv 
├─ out/ 
│  └─ report.md 
└─ tracker/ 
├─ __init__.py              
├─ mahasiswa.py 
├─ penilaian.py 
├─ rekap_kelas.py 
└─ report.py



Cara Menjalankan Program
Opsi 1: Jalankan app.py langsung
Opsi 2: Jalankan lewat package (bonus) dengan perintah python -m tracker


Data Input
File CSV contoh ada di folder data/


Output Laporan
Setelah pilih menu 6 (Markdown) atau 7 (HTML), laporan akan tersimpan otomatis di folder out/.

Pengujian Stabilitas
1 Copy seluruh folder ke komputer lain.
2 Buka terminal di dalam folder tersebut.
3 Jalankan perintah python -m tracker.
4 Pilih menu 1, 5, dan 6 untuk memastikan laporan otomatis muncul di out/report.md.


Konsep OOP yang Digunakan
• Encapsulation: atribut mahasiswa & penilaian disimpan dalam class.
• Composition: class RekapKelas menggabungkan Mahasiswa dan Penilaian.
• Modularization: logika dipisah ke dalam package tracker.
• File I/O: membaca CSV & menulis laporan Markdown/HTML.
• CLI: menu interaktif di terminal.
