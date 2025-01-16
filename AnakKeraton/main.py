import streamlit as st
import json
import os

# Judul Halaman
st.set_page_config(page_title="Login - Rekomendasi Diet Diabetes", page_icon=":lock:")

# Path ke file datapasien.json (pastikan path ini benar)
json_path = os.path.join(os.getcwd(), "datapasien.json")  # Path relatif

# Fungsi untuk membaca data dari JSON
def load_user_data(json_path):
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        st.error(f"File {json_path} tidak ditemukan.")
        return None
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON dari file {json_path}. Pastikan format JSON benar.")
        return None
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        return None


user_data = load_user_data(json_path)

if user_data: #cek apakah data berhasil di load
    # Judul
    st.title("Login")

    # Input Username dan Password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Tombol Login dan Logika
    if st.button("Login"):
        if username == user_data.get("username") and password == user_data.get("password"):
            st.success(f"Selamat Datang {user_data.get('nama')}!")
            st.set_query_params(login_success=True, nama=user_data.get('nama')) # Redirect dengan parameter nama
        else:
            st.error("Username atau password salah.")
else:
    st.stop() # menghentikan eksekusi jika data tidak berhasil di load