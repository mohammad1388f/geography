import tkinter as tk
import requests
from tkinter import messagebox
from geopy.geocoders import Nominatim
import folium

def find_nearest_country():
    degree_lat = float(degree_lat_entry.get())
    minute_lat = float(minute_lat_entry.get())
    second_lat = float(second_lat_entry.get())
    degree_lon = float(degree_lon_entry.get())
    minute_lon = float(minute_lon_entry.get())
    second_lon = float(second_lon_entry.get())
    
    lat = degree_lat + minute_lat/60 + second_lat/3600
    lon = degree_lon + minute_lon/60 + second_lon/3600
    
    api_key = "yor api in (opencagedata.com)"
    base_url = f"https://api.opencagedata.com/geocode/v1/json?key={api_key}&q={lat},{lon}&pretty=1"
    
    try:
        response = requests.get(base_url)
        data = response.json()
        if data.get("results"):
            country = data["results"][0]["components"]["country"]
            city = data["results"][0]["components"]["city"]
            
            messagebox.showinfo("نزدیک‌ترین اطلاعات جغرافیایی", 
                                f"نزدیک‌ترین کشور: {country}\nشهر: {city}")
            
            m = folium.Map(location=[lat, lon], zoom_start=10)
            folium.Marker([lat, lon], popup=city).add_to(m)
            m.save('map.html')
        else:
            messagebox.showerror("خطا", "اطلاعاتی یافت نشد.")
    except Exception as e:
        messagebox.showerror("خطا", f"خطا در دریافت اطلاعات: {str(e)}")

window = tk.Tk()
window.title("پیدا کردن نزدیک‌ترین اطلاعات جغرافیایی")

degree_lat_label = tk.Label(window, text="درجه عرض:")
degree_lat_label.pack()
degree_lat_entry = tk.Entry(window)
degree_lat_entry.pack()

minute_lat_label = tk.Label(window, text="دقیقه عرض:")
minute_lat_label.pack()
minute_lat_entry = tk.Entry(window)
minute_lat_entry.pack()

second_lat_label = tk.Label(window, text="ثانیه عرض:")
second_lat_label.pack()
second_lat_entry = tk.Entry(window)
second_lat_entry.pack()

degree_lon_label = tk.Label(window, text="درجه طول:")
degree_lon_label.pack()
degree_lon_entry = tk.Entry(window)
degree_lon_entry.pack()

minute_lon_label = tk.Label(window, text="دقیقه طول:")
minute_lon_label.pack()
minute_lon_entry = tk.Entry(window)
minute_lon_entry.pack()

second_lon_label = tk.Label(window, text="ثانیه طول:")
second_lon_label.pack()
second_lon_entry = tk.Entry(window)
second_lon_entry.pack()

find_button = tk.Button(window, text="پیدا کردن نزدیک‌ترین اطلاعات جغرافیایی", command=find_nearest_country)
find_button.pack()

window.mainloop()
