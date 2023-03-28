import heapq

import heapq


def str_to_int(strtime):
    (hour, minu) = strtime.split(':')
    hour, minu = int(hour), int(minu)    
    return hour * 100 + minu

def add10min(strtm):
    hour, minu = strtm//100, strtm%100
    minu += 10
    if minu >= 60:
        minu %= 60
        hour += 1        
    return hour * 100 + minu
    

def solution(book_time):
    if len(book_time) == 1: return 1
    
    answer = 1
    book_time.sort(key=lambda x: x[0])
    end_times = [ str_to_int(book_time[0][1]) ]
    
    for book_tm in book_time[1:]:
        crnt_stt_tm = str_to_int(book_tm[0])        
        result_val = add10min(end_times[0])
        
        if crnt_stt_tm < result_val:
            heapq.heappush(end_times, str_to_int(book_tm[1]))
            answer += 1
        else:
            # heapq.heappop(end_times)
            # while(len(end_times) and crnt_stt_tm >= result_val):
            heapq.heappop(end_times)
            result_val = add10min(end_times[0])
                
    return answer


if __name__ == "__main__":
    # book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
    # ["14:10", "23:59"], ["18:20", "21:20"]]
    book_time = [["00:00","00:10"],["00:20", "00:30"],["00:40","00:50"]]
    print(solution(book_time))