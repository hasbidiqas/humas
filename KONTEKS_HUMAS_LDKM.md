# Konteks & Panduan Kerja Divisi Humas LDKM BEM 2026

> **Cara Pakai di PC/Laptop Rumah (Antigravity / AI Lainnya):**
> Cukup buka folder ini atau *copy-paste* isi file ini ke chat AI di rumah, maka AI akan langsung paham seluruh konteks pekerjaan Humas dan bisa langsung membaca/mengedit Google Sheets secara otomatis.

---

## 1. Koneksi Otomatis Google Sheets (Apps Script Webhook)
File Google Sheets Tim Humas sudah dipasangi jembatan Google Apps Script sehingga AI bisa **membaca (`GET`)** dan **mengubah/menulis (`POST`)** langsung ke Google Sheets.

- **Web App URL**:
  `https://script.google.com/macros/s/AKfycbzf2qp0zjRl0Q6B4qtqSU2cStOANYKk3FC1sn9P2iMzYWGStw6BMpiMOv9SZj-2uKDK/exec`
- **Script Helper Python**: `gsheet_sync.py` (ada di folder ini).

### Format Request ke Web App:
- **Baca Semua Sheet (`GET`)**:
  Buka/fetch URL di atas $\rightarrow$ mengembalikan JSON berisi semua nama sheet dan matriks baris/kolomnya:
  - `1. Opsi Kandidat`
  - `2. Pemateri Fix`
  - `3. Template Chat`
- **Tulis/Update Sel (`POST` JSON)**:
  - Set 1 sel: `{"sheet": "3. Template Chat", "action": "setCell", "range": "A10", "value": "Teks"}`
  - Set banyak sel/baris: `{"sheet": "1. Opsi Kandidat", "action": "setValues", "startRow": 12, "startCol": 4, "values": [["Nama", "Jabatan"]]}`
  - Tambah baris baru di paling bawah: `{"sheet": "3. Template Chat", "action": "appendRow", "row": ["Bagian", "Target", "Isi Chat"]}`

---

## 2. Ringkasan Konteks Divisi Humas LDKM BEM 2026
- **Waktu Pelaksanaan LDKM**: 29–31 Oktober 2026 (3 Hari).
- **Koordinator Humas**: Dina | **PIC Peminjaman Ruangan**: Tilka.
- **Konsep & Alokasi Narasumber**:
  - Total ada **4 Topik Materi**: **2 Topik diisi Pemateri Internal** & **2 Topik diisi Pemateri Eksternal**.
  - Pada tahap pencarian (*brainstorming*), anggota Humas menyiapkan **4 opsi kandidat (`Opsi 1` s.d. `Opsi 4`) untuk setiap topik**.
  - Indikator *filtering* kandidat: kecocokan dengan topik, rekam jejak, dan anggaran (RAB Bendahara).
  - Untuk kandidat **Eksternal Profesional/Praktisi**, boleh melakukan *cek ombak (tanya rate card)* di awal sebelum difilter. Untuk **Internal (Dosen/Kampus)** tidak menanyakan *rate card* melainkan mengikuti plafon RAB.

### Daftar 4 Subtema & Topik Pematerian:
1. **Fondasi — *Kepemimpinan dan Manajemen Organisasi (KMO)***
   - Fokus: Prinsip kepemimpinan, fungsi organisasi, pembagian peran, tanggung jawab, dan pengelolaan kerja tim.
2. **Mindset — *Self-Awareness & Critical Thinking***
   - Fokus: Mengenali potensi dan nilai diri, membangun pola pikir kritis, menganalisis persoalan, serta memahami alasan dan tujuan instruksi.
3. **Kolaborasi — *Collaboration, Solidarity & Conflict Management***
   - Fokus: Membangun empati dan kepercayaan, memahami perbedaan, mengelola konflik, serta menyelesaikan masalah bersama.
4. **Ekspresi dan Aksi — *Effective Communication, Assertiveness & Public Speaking***
   - Fokus: Menyampaikan ide dengan jelas, menyusun argumentasi, berani berbeda pendapat secara konstruktif, dan menyuarakan aspirasi dengan bertanggung jawab.

---

## 3. Tenggat Waktu Kunci Humas (Dari Timeline Utama)
- **12–16 Okt 2026**: Mengumpulkan opsi narasumber & mengunci *shortlist* (4 opsi per topik $\rightarrow$ filter jadi Utama & Cadangan).
- **12–16 Okt 2026**: Pengajuan surat peminjaman ruangan (PIC: Tilka, koordinasi Sekretaris) untuk kepastian awal.
- **13–18 Okt 2026**: Menghubungi calon narasumber terpilih.
- **19 Okt 2026 (Maks. 21 Okt)**: Fix ke-4 Narasumber.
- **21 Okt 2026**: Pengumpulan CV/Biodata, Foto formal, & PPT pemateri + konfirmasi teknis (waktu, lokasi, durasi, format sesi).
