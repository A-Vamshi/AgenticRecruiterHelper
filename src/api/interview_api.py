from fastapi import APIRouter
import sqlite3
from src.agents.interview_scheduler import InterviewScheduler

router = APIRouter()
DB_PATH = "job_screening.db"
scheduler = InterviewScheduler()

@router.post("/schedule_interviews")
def schedule_interviews():
    """Triggers the interview scheduling process."""
    scheduler.schedule_interviews()
    return {"message": "Interviews scheduled successfully"}

@router.get("/scheduled_interviews")
def get_scheduled_interviews():
    """Fetch all scheduled interviews."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scheduled_interviews")
    interviews = cursor.fetchall()
    conn.close()

    return {
        "interviews": [
            {
                "id": row[0],
                "candidate_name": row[1],
                "candidate_email": row[2],
                "job_title": row[3],
                "interview_date": row[4],
                "status": row[5],
            }
            for row in interviews
        ]
    }
