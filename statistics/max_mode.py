import statistics
def find_max_mode(list1):
    #statistics._counts(list1) return count of all max numbers
    list_table = statistics._counts(list1)
    #print(list_table)    [(1, 2), (2, 2)]
    len_table = len(list_table)

    if len_table == 1:
        max_mode = statistics.mode(list1)
    else:
        new_list = []
        for i in range(len_table):
            #print(list_table[i][0])
            new_list.append(list_table[i][0])
      
        #print(*new_list)  
        max_mode = max(new_list) # use the max value here
    return max_mode

if __name__ == '__main__':
    a = [1,1,2,2,3]
    print(find_max_mode(a)) # print 2