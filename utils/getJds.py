import pandas as pd

def getJobDescriptions(file):
    jd_df = pd.read_csv(file)
    jds = []
    for i, row in jd_df.iterrows():
        jds.append({
            "id": i,
            "desc": row["Job Description"]
        })
    return jds

