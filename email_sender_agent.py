import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_shortlist_email(receiver_email, subject, job_role):
    sender_email = "sindhur2004@gmail.com"  # Replace with your email
    app_password = "jymi gyya kcxa zwik"  # Replace with your App Password

    # Email body with realistic details
    body = f"""
    <html>
    <body>
        <p>Dear Candidate,</p>
        <p>Congratulations! We are pleased to inform you that you have been <b>shortlisted</b> for the interview process for the role of <b>{job_role}</b> at <b>Tata Consultancy Services (TCS), Bengaluru</b>.</p>

        <h3>Interview Details:</h3>
        <ul>
            <li><b>Date:</b> March 5, 2025</li>
            <li><b>Time:</b> 10:00 AM IST</li>
            <li><b>Mode:</b> Offline</li>
            <li><b>Venue:</b> TCS Innovation Park, Whitefield, Bengaluru, Karnataka</li>
        </ul>

        <p>Please bring a copy of your <b>resume, valid ID proof, and academic certificates</b> for verification.</p>

        <p>Kindly confirm your availability by replying to this email at the earliest. If you have any queries, feel free to contact us at <b><a href="mailto:hr@tcs.com">hr@tcs.com</a></b>.</p>

        <p>Looking forward to meeting you!</p>

        <p><b>Best Regards,</b><br>
        <b>HR Team</b><br>
        <b>Tata Consultancy Services (TCS), Bengaluru</b><br>
         <a href="mailto:hr@tcs.com">hr@tcs.com</a> |  +91-80-1234-5678
        </p>
    </body>
    </html>
    """

    # Setup email headers
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        # Connect to SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Change SMTP server if needed
        server.starttls()  # Secure connection
        server.login(sender_email, app_password)  # Authenticate

        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f" Email sent successfully to {receiver_email}")

        # Close the server connection
        server.quit()

    except Exception as e:
        print(f" Error: {e}")

job_role="Software Engineer"
send_shortlist_email("jastennison227@gmail.com", "TCS Interview Shortlisting - "+ job_role, job_role )
