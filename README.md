Langkah-langkah:

1. Spesimen di-_crop_ manual menggunakan aplikasi lain sampai dalam satu file gambar hanya ada 1 tanda tangan dan tidak ada coretan/garis lain.
2. Jalankan `python3 spec.py <namafile>.jpg` untuk membuat file ttd yang background-nya transparan. Hasilnya jadi `<namafile>.out.png`
3. Jalankan `python3 crop.py <namafile>.out.png` untuk membuang padding pixel kosong di kanan-kiri atas-bawah ttd. Hasilnya jadi `<namafile>.out.crp.png`
