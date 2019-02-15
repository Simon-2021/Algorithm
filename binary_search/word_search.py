# 输入：一个正向有序词汇列表，一个单词
# 输出：该单词在列表中的下标，或NULL（当列表中不存在该单词时）

def leftthan(item1, item2):
    for i in range(len(item1)):
        if i+1 > len(item2):
            return False
        if item1[0:i+1] != item2[0:i+1]:
            if direct[item1[i]] > direct[item2[i]]:
                return False
            else:
                return True
    return True

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        print(guess, mid)
        if guess == item:
            return mid
        elif leftthan(item, guess):
            high = mid -1
        else:
            low = mid + 1
    return None

direct = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

word_list = ['abandon','ability','able','abnormal','aboard','abolish','abortion','about','above','abroad','abrupt','absence','absent','absolute','absorb','abstract','absurd','abundant','abuse','academic','academy','accelerate','accent','accept','access','accessible','accident','accommodation','accompany','accomplish','accordingto','account','accountant','accumulate','accuracy','accuse','accustomed','ache','achieve','achievement','acid','acknowledge','acquaintance','acquire','acquisition','acre','across','act','action','active','activity','actor','actress','actual','acute','ad','adapt','adaptation','add','addicted','addition','address','adequate','adjust','adjustment','administration','admirable','admire','admission','admit','adolescence','adolescent','adopt','adore','adult','advance','advantage','adventure','advertise','advertisement','advice','advise','advocate','aeroplane','affair','affect','affection','afford','afraid','after','afternoon','afterward','again','against','age','agency','agenda','agent','aggression','aggressive','ago','agree','agreement','agricultural','agriculture','ahead','aid','aim','air','aircraft','airmail','airplane','airport','airspace','alarm','album','alcohol','alcoholic','algebra','alike','alive','all','allergic','alley','allocate','allow','allowance','almost','alone','along','alongside','aloud','alphabet','already','also','alternative','although','altitude','altogether','aluminium','always','am']
print(binary_search(word_list, 'abandon'))