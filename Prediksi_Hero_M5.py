import os
import pickle
import streamlit as st

# Memuat model
model_path = 'prediksi_.sav'
if not os.path.exists(model_path):
    st.error(f"File model '{model_path}' tidak ditemukan.")
    st.stop()

try:
    model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    st.error(f"Gagal memuat model: {str(e)}")
    st.stop()

# Data nama hero dan kode hero
hero_data = {
    'Valentina': 1,
    'Fredrinn': 2,
    'Terizla': 3,
    'Edith': 4,
    'Irithel': 5,
    'Martis': 6,
    'Beatrix': 7,
    'Bruno': 8,
    'Paquito': 9,
    'Baxia': 10,
    'Novaria': 11,
    'Claude': 12,
    'Khufra': 13,
    'Brody': 14,
    'Grock': 15,
    'Yu Zhong': 16,
    'X.Borg': 17,
    'Kaja': 18,
    'Lancelot': 19,
    'Faramis': 20,
    'Kadita': 21,
    'Angela': 22,
    'Pharsa': 23,
    'Chou': 24,
    'Yve': 25,
    'Franco': 26,
    'Joy': 27,
    'Akai': 28,
    'Uranus': 29,
    'Minotaur': 30,
    'Karrie': 31,
    'Lapu-Lapu': 32,
    'Lylia': 33,
    'Gord': 34,
    'Rafaela': 35,
    'Mathilda': 36,
    'Arlott': 37,
    'Ixia': 38,
    'Fanny': 39,
    'Lesley': 40,
    'Valir': 41,
    'Gloo': 42,
    'Clint': 43,
    'Ling': 44,
    'Khaleed': 45,
    'Hayabusa': 46,
    'Wanwan': 47,
    'Floryn': 48,
    'Esmeralda': 49,
    'Diggie': 50,
    'Benedetta': 51,
    'Harith': 52,
    'Ruby': 53,
    'Dyrroth': 54,
    'Alpha': 55,
    'Melissa': 56,
    'Lolita': 57,
    'Bane': 58,
    'Helcurt': 59,
    'Lunox': 60,
    'Hilda': 61,
    'Cecilion': 62,
    'Guinevere': 63,
    'Estes': 64,
    'Atlas': 65,
    'Barats': 66,
    'Xavier': 67,
    'Leomord': 68,
    'Hylos': 69,
    'Phoveus': 70,
    'Badang': 71,
    'Kagura': 72,
    'Gusion': 73,
    'Nolan': 74,
    'Hanzo': 75,
    'Minsitthar': 76,
    'Karina': 77,
    'Luo Yi': 78,
    'Natalia': 79,
    'Thamuz': 80,
    'Balmond': 81,
    'Alice': 82,
    'Popol and Kupa': 83,
    'Masha': 84,
    'Jawhead': 85,
    'Harley': 86,
    'Yin': 87,
    'Cyclops': 88,
    'Granger': 89,
    'Julian': 90,
    'Chang\'e': 91,
    'Roger': 92,
    'Aamon': 93,
    'Yi Sun-Shin': 94,
    'Carmilla': 95,
    'Natan': 96,
    'Selena': 97,
    'Belerick': 98,
    'Nana': 99,
    'Hanabi': 100,
    'Freya': 101,
    'Aldous': 102,
    'Aulus': 103,
    'Tigreal': 104,
    'Kimmy': 105,
    'Moskov': 106,
    'Saber': 107,
    'Alucard': 108,
    'Silvanna': 109,
    'Sun': 110,
    'Vale': 111,
    'Vexana': 112,
    'Zilong': 113,
    'Layla': 114,
    'Miya': 115
}

# Judul
st.title('Prediksi Hero M5 World Championship')

# Menambahkan deskripsi aplikasi
st.write("""
Aplikasi ini memprediksi performa Hero pada kejuaraan M5 World Championship berdasarkan beberapa parameter yang diinputkan. 
Silakan masukkan data pada kolom-kolom yang disediakan di sebelah kiri dan tekan tombol Submit untuk melihat hasil prediksi.
""")

# Menggunakan sidebar untuk input
st.sidebar.title('Input Parameter')

# Input dengan keterangan dan tipe numerik
hero_names = list(hero_data.keys())
Hero_Encoded = st.sidebar.selectbox('Nama Hero', hero_names, help="Pilih hero yang ingin diprediksi")
T_Picked = st.sidebar.text_input('Total Pick', help="Masukkan total pick untuk hero ini")
BS_Picked = st.sidebar.text_input('BS Pick', help="Masukkan jumlah pick di Battle State")
RS_Picked = st.sidebar.text_input('RS Pick', help="Masukkan jumlah pick di Ranking State")
T_Banned = st.sidebar.text_input('T Ban', help="Masukkan total ban untuk hero ini")
T_PicksBans = st.sidebar.text_input('Total Pick Ban', help="Masukkan total pick dan ban untuk hero ini")

if st.sidebar.button('Submit'):
    try:
        # Ambil kode hero dari nama hero
        Hero_Encoded = hero_data[Hero_Encoded]
        
        # Validasi dan konversi input lainnya menjadi float
        try:
            T_Picked = float(T_Picked)
            BS_Picked = float(BS_Picked)
            RS_Picked = float(RS_Picked)
            T_Banned = float(T_Banned)
            T_PicksBans = float(T_PicksBans)
        except ValueError:
            st.error('Harap masukkan nilai numerik yang valid.')
            st.stop()
        
        # Lakukan prediksi
        MSE = model.predict([[Hero_Encoded, T_Picked, BS_Picked, RS_Picked, T_Banned, T_PicksBans]])

        # Asumsi: Normalisasi hasil prediksi jika berada dalam rentang 0 hingga 1000
        prediksi_persen = (MSE[0] / 1000) * 100

        # Tampilkan hasil prediksi dengan penjelasan
        st.write(f"Prediksi: {prediksi_persen:.2f}%")
        st.write("""
        Hasil prediksi menunjukkan estimasi performa M5 berdasarkan parameter-parameter yang telah dimasukkan.
        Nilai prediksi ini dapat digunakan untuk memahami potensi performa hero dalam pertandingan mendatang.
        """)
    except KeyError:
        st.error('Hero yang dipilih tidak ditemukan dalam data.')
    except Exception as e:
        st.error(f'Error: {str(e)}')

# Menambahkan footer
st.markdown("""
<style>
footer {
    visibility: hidden;
}
footer:after {
    content:'Dibuat dengan Streamlit'; 
    visibility: visible;
    display: block;
    position: relative;
    padding: 5px;
    top: 2px;
}
</style>
""", unsafe_allow_html=True)
