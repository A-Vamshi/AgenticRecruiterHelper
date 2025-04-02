import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

job_desc_path = os.getenv("JOB_DESCRIPTION_PATH")
job_desc_df = pd.read_csv(job_desc_path, encoding="cp1252")
job_desc_df = job_desc_df.drop("Unnamed: 2", axis=1)