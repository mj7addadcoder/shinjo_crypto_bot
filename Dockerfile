# استخدام صورة بايثون الرسمية
FROM python:3.10

# إنشاء مجلد للتطبيق
WORKDIR /app

# نسخ جميع الملفات
COPY . .

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل السكربت
CMD ["python", "crypto_bot.py"]
