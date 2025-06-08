import streamlit as st 
from utils.getJds import getJobDescriptions
from utils.getResumeInfo import getResumeInfo
jd_file = st.file_uploader("Upload JD CSV", type=["csv"])
resume_files = st.file_uploader("Upload PDF Resumes", type=["pdf"], accept_multiple_files=True)

if st.button("Get resume details"):
    info = getResumeInfo(resume_files)
    st.write(info)

if st.button("Get jd details"):
    info = getJobDescriptions(jd_file)
    st.write(info)
