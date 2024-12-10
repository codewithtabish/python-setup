import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "tabish169000@gmail.com"
SENDER_PASSWORD = "lisryxexmzsoxjot"  # Your generated app password

def send_email(user_name, recipient_email, random_number):
    try:
        # HTML email content with inline CSS for styling
        subject = f"Welcome to CodeWithTabish, {user_name}!"
        body = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                .header {{
                    text-align: center;
                    padding: 20px;
                    background-color: #007bff;
                    color: white;
                    border-radius: 10px 10px 0 0;
                    font-size: 24px;
                    font-weight: bold;
                }}
                .content {{
                    padding: 20px;
                    line-height: 1.6;
                }}
                .content h2 {{
                    color: #007bff;
                }}
                .footer {{
                    text-align: center;
                    font-size: 12px;
                    color: #888;
                    margin-top: 20px;
                    border-top: 1px solid #eee;
                    padding-top: 10px;
                }}
                .footer a {{
                    color: #007bff;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    Welcome to CodeWithTabish!
                </div>
                <div class="content">
                    <p>Dear {user_name},</p>
                    <p>We are delighted to welcome you to <strong>CodeWithTabish</strong>. Your journey towards mastering coding and technology begins here, and we are thrilled to be part of it.</p>
                    <h2>Your One-Time Passcode (OTP): {random_number}</h2>
                    <p>Please use this code to complete your account setup. For your security, do not share this code with anyone.</p>
                    <p>Here’s what you can do next:</p>
                    <ul>
                        <li>Log in to your dashboard and explore our features.</li>
                        <li>Access tutorials, resources, and support to accelerate your learning.</li>
                        <li>Stay updated with our latest news and announcements.</li>
                    </ul>
                    <p>If you have any questions or need assistance, our support team is here to help you at every step.</p>
                </div>
                <div class="footer">
                    <p>Warm regards,</p>
                    <p>The <strong>CodeWithTabish</strong> Team</p>
                    <p><a href="https://www.codewithtabish.com">Visit our website</a></p>
                </div>
            </div>
        </body>
        </html>
        """

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html"))  # Send as HTML email

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login using app password
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        
        print(f"Welcome email sent to {user_name} ({recipient_email}) successfully!")
        return True
    except Exception as e:
        print("Failed to send email:", str(e))
        return False
