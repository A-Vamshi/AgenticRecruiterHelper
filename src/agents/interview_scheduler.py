import sqlite3
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

DB_PATH = "job_screening.db"

class InterviewScheduler:
    def __init__(self) -> None:
        self.db_path = DB_PATH
    
    def get_next_working_day(self):
        interview_date = datetime.today() +timedelta(days=7)
        if interview_date.weekday() == 5:
            interview_date+=timedelta(days=2)
        elif interview_date.weekday() == 6:
            interview_date+=timedelta(days=1)
        return interview_date.strftime("%Y-%m-%d")
    
    def fetch_shortlisted_candidates(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        SELECT r.name, r.education, j.title 
        FROM match_results m
        JOIN resumes r ON m.resume_id = r.id
        JOIN job_descriptions j ON m.job_id = j.id
        WHERE m.match_score >= 80
    ''')
        candidates = cursor.fetchall()
        conn.close()
        return candidates
    
    def store_interview_schedule(self,name,email,job_title,interview_date):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO scheduled_interviews (candidate_name, candidate_email, job_title, interview_date)
            VALUES (?, ?, ?, ?)
        """, (name, email, job_title, interview_date))
        conn.commit()
        conn.close()

    def send_email(self, candidate_email, candidate_name, job_title, interview_date):
        """Send interview email via SMTP."""
        sender_email = "your-email@gmail.com"
        sender_password = "your-password"

        subject = f"Interview Invitation for {job_title}"
        body = f"""
        Dear {candidate_name},

        You have been shortlisted for the {job_title} role.

        📅 Date: {interview_date}
        ⏰ Time: 10:00 AM
        🔗 Format: Online (Google Meet)

        Please confirm your availability by replying to this email.

        Regards,  
        Hiring Team
        """

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = candidate_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, candidate_email, msg.as_string())
            server.quit()
            print(f"✅ Email sent to {candidate_email}")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")

    def schedule_interviews(self):
        """Schedules interviews for shortlisted candidates."""
        candidates = self.fetch_shortlisted_candidates()
        interview_date = self.get_next_working_day()
        for name, email, job_title in candidates:
            self.store_interview_schedule(name, email, job_title, interview_date)
            self.send_email(email, name, job_title, interview_date)