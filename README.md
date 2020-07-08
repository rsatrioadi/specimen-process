Langkah-langkah:

1. Spesimen di-_crop_ manual menggunakan aplikasi lain sampai dalam satu file gambar hanya ada 1 tanda tangan dan tidak ada coretan/garis lain.

2. Jalankan `python3 spec.py <namafile>.jpg` untuk membuat file ttd yang background-nya transparan. Hasilnya jadi `<namafile>.out.png`

3. Jalankan `python3 crop.py <namafile>.out.png` untuk membuang _padding_ pixel kosong di kanan-kiri atas-bawah ttd. Hasilnya jadi `<namafile>.out.crp.png`

ATAU

3.2. Jalankan `python3 resize.py <x> <y> <namafile>.out.png` untuk me-_resize_ gambar menjadi berukuran `x` pixel × `y` pixel. Hasilnya jadi `<namafile>.out.rsz.png`