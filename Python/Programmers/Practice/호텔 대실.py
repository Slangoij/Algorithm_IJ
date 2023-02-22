import heapq


def str_to_inttime(strtime):
    spl_time = strtime.split(':')
    hour = int(spl_time[0])
    minu = int(spl_time[1])
    year = int(spl_time[-1])
    
    if minu >= 60:
        minu %= 60
        hour += 1

    if hour >= 24:
        hour %= 24
        year += 1
        
    return year * 10000 + hour * 100 + minu


def solution(book_time):
    if len(book_time) == 1: return 1
    
    answer = 1
    book_time_addyr = [[i[0] + ":0", i[-1] + ":0"] for i in book_time]
    book_time_addyr.sort(key=lambda x: x[0])
    end_times = [ book_time_addyr[0][1] ]
    
    print(book_time)
    
    for book_tm in book_time_addyr[1:]:
        
        pop_end_tm = heapq.heappop(end_times)
        
        crnt_stt_tm = str_to_inttime(book_tm[0])
        
        (hr, mn, yr) = pop_end_tm.split(':')
        tmp_add_val = str(int(mn) + 10)
        
        result_val = str_to_inttime( f"{hr}:{tmp_add_val}:{yr}" )
        
        print()
        print(f"{crnt_stt_tm} {result_val}")
        
        # int_tgt_pop_end_tm = str_to_inttime(pop_end_tm) + 10
        # ret_str_pop_end_tm = f"{int_tgt_pop_end_tm//100}:{int_tgt_pop_end_tm%100}"
        
        if crnt_stt_tm < result_val:
            heapq.heappush(end_times, book_tm[1])
            answer += 1
            print(" added")
        
        heapq.heappush(end_times, pop_end_tm)
                
    return answer


if __name__ == "__main__":
    book_time =\
        [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
        ["14:10", "19:20"], ["18:20", "21:20"]]
    print(solution(book_time))