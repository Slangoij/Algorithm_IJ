from datetime import datetime, date, timedelta

def solution(today, terms, privacies):
    answer = []
    
    datetime.strptime(today, "%Y.%m.%d")
    due_date_map = {}
    for term in terms:
        (alpha, delta_time) = term.split()
        due_date_map[alpha] = today_dt + timedelta(months=int(delta_time))
        
    for i in range(len(privacies)):
        (crnt_date, crnt_priv) = privacies[i + 1].split()
        crnt_date_dt = datetime.strptime(crnt_date, "%Y.%m.%d")
        
        if crnt_date_dt >= due_date_map[crnt_priv]:
            answer.append(i+1)
    
    return answer

if __name__ == "__main__":
    today = "2022.05.19"
    terms = ["A 6", "B 12", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    solution(today, terms, privacies)