#Student Name: Mengxi Li, Student ID: 24194872
#define standard deviation function with parameter:list of income
def standard_deviation_income(List_income):
    if len(List_income) == 0 or len(List_income) == 1:
        #return 0 for an empty list and ZeroDivision
        return 0
    else:
        xp = sum(List_income) / len(List_income)
        sum1 = 0
        for xi in List_income:
            sum1 += (xi - xp) **2
        s = (sum1 / (len(List_income)-1)) ** 0.5
        return s

#define correlation coefficient function with parameter:age list and income list
def correlation(List_age,List_income):
    xp = sum(List_age) / len(List_age)
    yp = sum(List_income) / len(List_income)
    sum1 = 0
    div2_sum1 = 0
    div2_sum2 = 0
    for xi,yi in zip(List_age,List_income):
        div1 = (xi - xp) * (yi - yp)
        div2_sum1 += (xi - xp) **2
        div2_sum2 += (yi - yp) **2
        sum1 += div1
    sum2 = (div2_sum1 * div2_sum2) ** 0.5
    #return 0 for ZeroDivision
    if sum2 ==0:
        return 0
    else:
        r = sum1 / sum2
        return r
            
#define the main function with three parameters
def main(csvfile, age_group, country):
    #read the csv file line by line
    with open(csvfile,'r') as f:
        #skip the first row containg the headings
        next(f)
        #initialize a list to store results
        results_OP1= []
        #initialize a set to store results for adding non-repeating elements
        OP2 = set()
        time= []
        OP3_3 = None
        OP3_income = []
        average_time = 0
        demography = []
        OP4_platform = []
        #process each line of the file
        for line in f:
            #remove leading and trailing whitespace characters and split lines into individual values based on the comma separator
            column = line.strip().split(',')
            #name the columns
            ID,age,gender,time_spent_hour,platform,interests,Country,demographics,profession,income,indebt = str(column[0]),int(column[1]),column[2],int(column[3]),column[4],column[5],column[6],column[7],column[8],float(column[9]),column[10]
            sorted(ID)
            #check OP1 condition
            if Country.lower() == country.lower() and indebt.lower() == 'true' and time_spent_hour > 7 and profession.lower() == 'student':
                #append the required ID and income to the results_OP1 list
                results_OP1.append([str(ID),income])           
            #check OP2,OP3 condition
            if age_group[0] <= age <= age_group[1]:
                #append the required countries to the results_OP2 set
                OP2.add(Country.lower())
                #append the required time_spent_hour to the time list
                time.append(time_spent_hour)
                #get the average_time in the time list
                average_time = sum(time) / len(time)
                #append the required income to the OP3_income list
                OP3_income.append(income)
                #append two required elements to demography list
                demography.append([time_spent_hour,demographics.lower()])
                #create dictionaries to store total time and count for each demographic
                total_time = {}
                count = {}
                #iterate through demography to calculate total time spent and count for each demographic
                for t,d in demography:
                    if d not in total_time:
                        total_time[d]=0
                    if d not in count:
                        count[d]=0
                    total_time[d] += t
                    count[d] += 1
                #calculate average time spent for each demographic
                demo_average = {}
                for d in total_time:
                    if count[d] != 0:
                        demo_average[d] = total_time[d] / count[d]
                    else:
                        demo_average[d] = 0
                #select the demographic with the lowest average time spent
                #sort the demographics in alplabetical order
                OP3_list = sorted(demo_average.items(), key = lambda x: (x[1],x[0]))
                OP3_3 = OP3_list[0][0]
            #result for OP3 first element is rounded to four decimal places
            OP3_1 = float(f'{average_time:0.4f}')
            #call the standard_deviation_income function which has been defined
            #result is rounded to four decimal places
            OP3_2 = float(f'{standard_deviation_income(OP3_income):0.4f}')
            #append each platform which users use into the empty list
            #find OP4 condition:platform with highest number of users
            #sort in alphabetical order
            OP4_platform.append(platform)
            OP4_highest = max(sorted(OP4_platform), key=OP4_platform.count)
    with open(csvfile,'r') as f:
        next(f)
        OP4_age = []
        OP4_income = []  
        for line in f:
            column = line.strip().split(',')
            age,platform,income = int(column[1]),column[4],float(column[9])                     
            #check OP4 condition
            if platform == OP4_highest:
                #append the required age to OP4_age list
                OP4_age.append(age)               
                #append the required income to OP4_income list
                OP4_income.append(income)
        #call the correlation function which has been defined
        OP4 = correlation(OP4_age,OP4_income)
                           
        #sort the results list by ASC student ID
        results_OP1.sort(key=lambda x: x[0])
        #sort the results list by ASC country
        #switch set to list
        results_OP2 = sorted(list(OP2))
        results_OP3 = [OP3_1,OP3_2,OP3_3]
        results_OP4 = float(f'{OP4:0.4f}')
    return (results_OP1,results_OP2,results_OP3,results_OP4)
            




    



