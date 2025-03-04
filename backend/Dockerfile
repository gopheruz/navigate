# Python 3.13 bazaviy image
FROM python:3.13-slim

# Ishlash uchun asosiy katalog
WORKDIR /app

# Zarur kutubxonalarni to'g'ridan-to'g'ri o'rnatamiz
RUN pip install fastapi uvicorn librosa numpy scipy pydub

# Backend papkasini konteynerga nusxalash
COPY . /app  
# Bu joriy papkada mavjud barcha fayllarni, shu jumladan backend papkasini, konteynerga kochiradi

# Port ochish
EXPOSE 8000

# FastAPI serverni ishga tushirish
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
