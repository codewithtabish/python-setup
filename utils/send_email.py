import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "tabish169000@gmail.com"
SENDER_PASSWORD = "lisryxexmzsoxjot"  # Your generated app password

def send_email(user_name, recipient_email):
    try:
        # HTML email content with inline CSS for styling
        subject = f"Welcome to Our Platform, {user_name}!"
        body = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                .header {{
                    text-align: center;
                    padding: 20px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 8px 8px 0 0;
                }}
                .content {{
                    margin: 20px 0;
                    line-height: 1.6;
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
                    color: #4CAF50;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Welcome to CodeWithTabish, {user_name}!</h1>
                </div>
                <div class="content">
                    <p>Hi {user_name},</p>
                    <p>We're thrilled to have you on board. Here are a few things you can do next:</p>
                    <ul>
                        <li>Explore your dashboard to see the amazing features we offer.</li>
                        <li>If you have any questions, feel free to reach out to our support team.</li>
                        <li>Stay tuned for updates and announcements directly to your inbox.</li>
                    </ul>
                    <p>We're excited to see what you'll achieve with us!</p>
                </div>
                <div class="footer">
                    <p>Best regards,</p>
                    <p>The CodeWithTabish Team</p>
                    <p>Powered by <a href="https://www.codewithtabish.com">CodeWithTabish</a></p>
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


