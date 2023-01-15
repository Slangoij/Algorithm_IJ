from datetime import datetime, timedelta

def solution(today, terms, privacies):
    answer = []
    
    today_dt = datetime.strptime(today, "%Y.%m.%d")
    new_date = None
    due_date_map = dict({})
    
    for term in terms:
        (alpha, delta_time_str) = term.split()
        
        delta_mth_val = int(delta_time_str)

        new_yr, delta_yr, delta_mth, new_date = 0, 0, 0, None
        
        if delta_mth_val > 12:
            delta_yr = delta_mth_val // 12
            delta_mth = ((delta_mth_val-1) % 12) + 1
            
        new_yr = int(today_dt.year+delta_yr)
        new_mth = int(today_dt.month + delta_mth)

        new_date = today_dt.replace(year=new_yr, month=new_mth)
        
        # print("set : " + alpha)
        due_date_map[alpha] = new_date
        
    print(due_date_map)

    for i in range(len(privacies)):
        (crnt_date, alpha) = privacies[i].split()
        crnt_date_dt = datetime.strptime(crnt_date, "%Y.%m.%d")
        
        # print("get : " + alpha)
        
        print(crnt_date_dt, due_date_map[alpha], crnt_date_dt >= due_date_map[alpha])
        if crnt_date_dt >= due_date_map[alpha]:
            answer.append(i+1)
    
    return answer

if __name__ == "__main__":
    today = "2022.05.19"
    terms = ["A 6", "B 12", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    solution(today, terms, privacies)