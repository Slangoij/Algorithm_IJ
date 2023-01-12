from datetime import date, timedelta

def solution(today, terms, privacies):
    answer = []
    
    target_data_map = {}
    for i in range(len(terms)):
        crnt_term_name = terms[i].split()[0]
        crnt_term_prid = terms[i].split()[1]

        target_data_map[crnt_term_name] =\
            date.fromisoformat(today) - timedelta(month=crnt_term_prid)
        
    for i in range(len(privacies)):
        crnt_datetime = privacies.split()[0]
        crnt_term = privacies.split()[1]

    
    return answer

if __name__ == "__main__":
    _today = 
    _terms = 
    _privacies = 
    print(solution(_today, _terms, _privacies))