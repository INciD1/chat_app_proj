
# 💬 Chat App Proj

โปรเจกต์นี้เป็นแอปพลิเคชันแชทแบบเรียลไทม์ที่พัฒนาด้วย Python และ Flask โดยมีเป้าหมายเพื่อให้ผู้ใช้งานสามารถสื่อสารกับเพื่อน ๆ ได้ตั้งแต่ 2 คนขึ้นไป ผ่านอินเทอร์เฟซที่ใช้งานง่ายและสะดวกสบาย

## 🔗 ลิงก์ทดลองใช้งาน

👉 [https://flask-chat-gxhb.onrender.com/](https://flask-chat-gxhb.onrender.com/)

## 🚀 ฟีเจอร์หลัก

- รองรับการแชทแบบกลุ่มและส่วนตัว
- อินเทอร์เฟซที่เรียบง่ายและใช้งานง่าย
- พัฒนาอย่างต่อเนื่องเพื่อเพิ่มฟีเจอร์ใหม่ ๆ ในอนาคต

## 🛠️ เทคโนโลยีที่ใช้

- Python
- Flask
- HTML
- CSS

## 📁 โครงสร้างโปรเจกต์

```
chat_app_proj/
├── static/
│   └── css/
|      └── style.css
├── templates/
|      └── base.html
|      └── home.html
|      └── room.html
├── main.py
├── requirements.txt
├── render.yaml
├── runtime.txt
└── README.md
```

## ⚙️ การติดตั้งและใช้งาน

1. คลอนโปรเจกต์จาก GitHub:
   ```bash
   git clone https://github.com/INciD1/chat_app_proj.git
   cd chat_app_proj
   ```

2. สร้างและเปิดใช้งาน virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # สำหรับ Unix หรือ MacOS
   venv\Scripts\activate     # สำหรับ Windows
   ```

3. ติดตั้ง dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. รันแอปพลิเคชัน:
   ```bash
   python main.py
   ```

5. เปิดเบราว์เซอร์และไปที่ `http://localhost:5000` เพื่อเริ่มใช้งาน

## 📌 หมายเหตุ

โปรเจกต์นี้ยังอยู่ในระหว่างการพัฒนา ฟีเจอร์ใหม่ ๆ จะถูกเพิ่มเข้ามาในอนาคต หากคุณมีข้อเสนอแนะหรือพบปัญหา สามารถเปิด issue หรือ pull request ได้เลยครับ 😊
