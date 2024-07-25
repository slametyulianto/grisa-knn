import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Set page configuration
st.set_page_config(page_title="Klasifikasi Jurusan",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
with open('jurusan.pkl', 'rb') as file:
    loaded_knn = pickle.load(file)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('GrisaTech',
                           ['Klasifikasi Jurusan', 'About Me'],
                           menu_icon='hospital-fill',
                           icons=['heart', 'person'],
                           default_index=0)

# Klasifikasi Jurusan Page
if selected == 'Klasifikasi Jurusan':

    # Page title
    st.title('Klasifikasi Jurusan - SMK PGRI 1 Ngawi')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        MTK = st.text_input('Nilai Matematika')

    with col2:
        IPA = st.text_input('Nilai Ilmu Pengetahuan Alam')

    with col1:
        IPS = st.text_input('Nilai Ilmu Pengetahuan Sosial')

    with col2:
        BIG = st.text_input('Nilai Bahasa Inggris')

    # Code for Prediction
    jurusan_predict = ''

    # Creating a button for Prediction
    if st.button('Klasifikasi Jurusan'):
        try:
            # Convert input values to numeric
            user_input = [float(MTK), float(IPA), float(IPS), float(BIG)]

            # Predict the jurusan
            cabor_hasil = loaded_knn.predict([user_input])[0]

            if cabor_hasil == 0:
                jurusan_adalah = "Desain Komunikasi Visual"
            elif cabor_hasil == 1:
                jurusan_adalah = "Desain Pemodelan dan Informasi Bangunan"
            elif cabor_hasil == 2:
                jurusan_adalah = "Perhotelan"
            elif cabor_hasil == 3:
                jurusan_adalah = "Teknik Instalasi Tenaga Listrik"
            elif cabor_hasil == 4:
                jurusan_adalah = "Teknik Komputer dan Jaringan"
            elif cabor_hasil == 5:
                jurusan_adalah = "Teknik Sepeda Motor"
            elif cabor_hasil == 6:
                jurusan_adalah = "Teknik Pemesinan"
            elif cabor_hasil == 7:
                jurusan_adalah = "Teknik Kendaraan Ringan"
            else:
                jurusan_adalah = "Tidak ada Jurusan yang sesuai"

            st.success(f"Jurusan yang sesuai untuk Anda adalah: {jurusan_adalah}")
        except ValueError:
            st.error("Masukkan nilai numerik yang valid untuk semua mata pelajaran.")

# About Me
if selected == "About Me":

    # Page title
    st.title("SMK PGRI 1 Ngawi")

    # Sejarah SMK PGRI 1 Ngawi
    sejarah = """
    SMK PGRI 1 Ngawi berdiri dan menerima siswa baru kelas I pada Juli 1964 dengan nama “STM Persiapan” Ngawi bertempat di Aula milik Pemda Kab. Ngawi selama 2 tahun. Kepala sekolah pertama yaitu Bapak. R. Samsirmihardjo juga sebagai Kepala sekolah Teknik Negeri (Sederajat SMP) Ngawi dengan guru – gurunya sebagian besar dari guru STN tersebut.

    Dari tahun ke tahun minat masyarakat untuk menyekolahkan anak-anaknya meningkat, sehingga mulai tahun 1968 bekerja sama dengan SMA Negeri 1 Ngawi untuk kegiatan Belajar Mengajar STM Persiapan pada siang sampai sore hari. Untuk Ketenagaan mengajar, STM Persiapan bekerja sama dengan Jawatan PUK, Jawatan Pengairan, PLN disamping dari guru STN Ngawi.

    Pada waktu kegiatan Belajar Mengajar (KBM) di SMA Negeri 1 Ngawi, Kepala Sekolah dirangkap oleh Kepala SMA Negeri 1 Ngawi yaitu Bapak Martono, BA, sedangkan Bapak R. Samsirmihardjo menjadi Wakil Kepala Sekolah.

    Pada saat itu Jurusan yang ada adalah Bangunan Gedung (BG), Bangunan Air (BA). Dan beberapa tahun kemudian seiring dengan animo masyarakat Akan Jurusan Listrik maka STM Persiapan membuka Jurusan Listrik.

    Pada Tahun 1985 Kepala Sekolah (Bapak Martono B.A) diangkat menjadi pengawas DIKMENUM, maka diganti Bapak R. Samsirmihardjo dan Wakil Kepala Sekolahnya Bapak Drs. Warsun Warsono.

    Tahun 1988 ada pergantian nama Sekolah dari “STM Persiapan” menjadi “STM PGRI Ngawi”. Pada tahun 1989 ada peraturan bahwa Sekolah Negeri (SMAN) tidak boleh ditempati Sekolah Swasta pada siang hari. Dengan demikian KBM Siswa STM PGRI Ngawi pindah tempat ke SDN Jururejo I, SDN Jururejo II, ada 6 kelas, SDN Jururejo IV ada 5 kelas sedangkan di lokasi sekolah sendiri (yang berada di jalan rajawali 32 beran ngawi) ada 3 kelas, Sehingga jumlah total rombel ada 14 kelas.

    Dengan Pimpinan Bapak Drs. Warsun Warsono mulai ada peningkatan jumlah siswa dengan Jurusan Bangunan dan jurusan Listrik kemudian Sekolah membuka jurusan baru yaitu Mesin Mekanik Umum (MU), sedangkan Jurusan Bangunan yang semula ada Bangunan Air dan Bangunan Gedung, untuk jurusan Bangunan Air ditutup karena tidak ada pendaftar atau peminatnya.

    Pada saat itu Rombongan belajar mencapai 18 kelas hanya saja sarana praktek dirasakan sangat kurang, hal tersebut mengingat lahan tanah dan ruang belum berkembang preaktek siswa menyewa di BLP Madiun. Dalam perjalanan dan perkembangannya mulai bulan Juli 1991 Bapak Drs. Warsun Warsono diangkat menjadi Kepala SMA Negeri Sine, kemudian ada peraturan bahwa Kepala Negeri dilarang merangkap Kepala Sekolah Swasta meskipun Sore ataupun siang hari.

    Maka dari itu Bapak Drs. Karjan di tunjuk menjadi Kepala Sekolah di STM PGRI Ngawi sejak tahun 1996. Bapak Drs. Karjan memiliki latar belakang Teknik dari STN Bangunan Gedung, STM N Jurusan Bangunan Gedung dan terakhir sarjana pendidikan. Dalam perkembangan, SMK PGRI 1 Ngawi berkembang menjadi Sekolah berstandar Nasional Dengan SK No 0026/C5.2/MN/ 2005 tanggal 2 Januari 2005 dan berdasarkan No 0418/C5.2/LL/2006 tanggal 4 April 2006 mendapat predikat SMK BESAR karena memiliki siswa lebih dari 2.500 siswa. Pada tahun 2012 SMK PGRI 1 Ngawi juga meraih sertifikat manajeman mutu ISO 9001: 2008.

    Pada tahun 2015 SMK PGRI 1 Ngawi Kepala Sekolah selanjutnya adalah Bapak Drs. H. Hidayat Machruf, M.Pd dan beliau melanjutkan program manajemen ISO sertifikat manajeman mutu ISO 9001: 2015. Berbagai program juga diwujudkan diantaranya pembentukan lembaga sertifikasi profesi yang dinaungi oleh BNSP (LSP P1), kelas industri AXIOO, Program BCA CMA dan lain sebagainya. Pada tahun 2020 dibawah kepemimpinan Bapak Drs. H. Hidayat Machruf, M.Pd, SMK PGRI 1 Ngawi menjadi sekolah Center of excellent (COE) bidang Hospitality dan kemudian berlanjut menjadi SMK Pusat Keunggulan. Estafet kepemimpinan di SMK PGRI 1 Ngawi dilanjutkan oleh Bapak Farid Samsul Hadi, MPd sejak tahun 2022.

    Dalam perjalanan dari masa ke masa nama STM PGRI berubah dari “ STM PGRI Ngawi “ Menjadi SMK PGRI 1 Ngawi. Terjadi perubahan istilah dari “ Jurusan “ sekarang menjadi “ Kompetensi Keahlian “ antara lain:

    1. Bangunan Gedung sekarang menjadi Desain Pemodelan dan Informasi Bangunan (DPIB) 
    2. Listrik Instalasi sekarang menjadi Teknik Instalasi Tenaga Listrik (TITL)
    3. Mekanik Umum sekarang menjadi Teknik Pemesinan (TPm)
    4. Mekanik Otomotif sekarang menjadi Teknik Kendaraan Ringan (TKR)
    5. Teknik Bisnis Sepeda Motor (TBSM)
    6. Teknik Jaringan dan Komputer Telekomunikasi (TJKT)
    7. Perhotelan (Ph)
    8. Multimedia (MM)/ Desain Komunikasi Visual (DKV)
    """

    # Menampilkan sejarah
    st.write(sejarah)
