import sqlite3

def connect_db():
    return sqlite3.connect("job_screening.db")

# Insert a job description
def insert_job(title, required_skills, experience, responsibilities, qualifications):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO job_descriptions (title, required_skills, experience, responsibilities, qualifications)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, required_skills, experience, responsibilities, qualifications))
    connection.commit()
    connection.close()

# Insert a resume
def insert_resume(name, education, experience, skills, certifications):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO resumes (name, education, experience, skills, certifications)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, education, experience, skills, certifications))
    connection.commit()
    connection.close()

# Insert match result
def insert_match_result(job_id, resume_id, match_score):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO match_results (job_id, resume_id, match_score)
        VALUES (?, ?, ?)
    ''', (job_id, resume_id, match_score))
    connection.commit()
    connection.close()

# Retrieve all job descriptions
def get_all_jobs():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM job_descriptions")
    jobs = cursor.fetchall()
    connection.close()
    return jobs

# Retrieve all resumes
def get_all_resumes():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM resumes")
    resumes = cursor.fetchall()
    connection.close()
    return resumes

# Retrieve match results
def get_match_results():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM match_results")
    results = cursor.fetchall()
    connection.close()
    return results
