import json
def compute_weighted_score(llm_json):
    weights = {
        "match_score": 0.4,
        "experience_fit": 0.3,
        "education_fit": 0.2,
        "overqualification_penalty": 0.1
    }
    experience_map = {"Excellent": 1.0, "Good": 0.75, "Fair": 0.5, "Poor": 0.25}
    education_map = {"Excellent": 1.0, "Good": 0.75, "Fair": 0.5, "Poor": 0.25}

    score = (
        weights["match_score"] * (llm_json["match_score"] / 10) +
        weights["experience_fit"] * experience_map[llm_json["experience_fit"]] +
        weights["education_fit"] * education_map[llm_json["education_fit"]] -
        (weights["overqualification_penalty"] if llm_json["overqualification_flag"] else 0)
    )
    return round(score, 3)