import streamlit as st 
from utils.getJds import getJobDescriptions
from utils.getResumeInfo import getResumeInfo
from utils.computeWeight import compute_weighted_score
from langchain_ollama import OllamaLLM
import json

jd_file = st.file_uploader("Upload JD CSV", type=["csv"])
resume_files = st.file_uploader("Upload PDF Resumes", type=["pdf"], accept_multiple_files=True)
llm = OllamaLLM(model="llama3.2")
all_matches = dict()

if st.button("Get resume details"):
    info = getResumeInfo(resume_files)
    st.write(info)

if st.button("Get jd details"):
    info = getJobDescriptions(jd_file)
    st.write(info)

if st.button("Parse data: "):
    if jd_file and resume_files:
        jds, resumes = getJobDescriptions(jd_file), getResumeInfo(resume_files)
        for jd in jds:
            id = jd["id"]
            desc = jd["desc"]
            jd_matches = []
            for resume in resumes:
                judge_prompt = """
                                    You are an expert technical recruiter. Analyze how well the candidate fits the given job description. Output a JSON object with:

                                    - match_score: A number between 0 and 10 representing overall fit.
                                    - matched_skills: List of skills required by the job that are present in the resume.
                                    - missing_skills: List of required skills that are not clearly mentioned in the resume.
                                    - experience_fit: One of "Excellent", "Good", "Fair", or "Poor" based on relevance and years of experience.
                                    - education_fit: One of "Excellent", "Good", "Fair", or "Poor" based on alignment with the job's education requirements.
                                    - overqualification_flag: true if the candidate seems significantly overqualified, false otherwise.
                                    - fit_summary: A 2-3 sentence explanation of the fit.

                                    Return only valid JSON. Do not include explanations or formatting. No code fences (like ```), and no introductory sentences.
                                    Job Description:
                                    {}

                                    Candidate Resume:
                                    {}
                                """
                results = llm.invoke(judge_prompt.format(resume["text"], desc))
                res = json.loads(results)
                weight = compute_weighted_score(res)
                if weight > 0.5:
                    jd_matches.append(resume["id"])
            all_matches[id] = jd_matches
        st.write(all_matches)
