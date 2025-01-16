#Student Name: Mengxi Li, Student ID: 24194872
#define the cosine similarity function with parameter A and B
def sim(A,B):
    #calculate the dividend
    div1 = sum(a * b for a,b in zip(A,B))
    #calculate the divisor
    div2_1 = sum(a ** 2 for a in A) ** 0.5
    div2_2 = sum(b ** 2 for b in B) ** 0.5
    if div2_1 != 0 and div2_2 != 0:
        co_sim = div1 / (div2_1 * div2_2)
    else:
        #return 0 for ZeroDivision
        co_sim = 0
    return co_sim
#define standard deviation function with parameter list
def standard_deviation(L):
    #return 0 for an empty list and ZeroDivision
    if len(L) == 0 or len(L) == 1:
        return 0
    else:
        xp = sum(L) / len(L)
        sum1 = 0
        for xi in L:
            sum1 += (xi - xp) **2
        s = (sum1 / (len(L)-1)) ** 0.5
    return s
#define Cohen's d test function with parameter G1 and G2
def cohen(G1,G2):
    div1 =  (len(G1)-1) * (standard_deviation(G1) ** 2) + (len(G2)-1) * (standard_deviation(G2) ** 2)
    div2 = len(G1) + len(G2) - 2
    #return 0 for ZeroDivision
    if div2 == 0:
        return 0
    else:
        s = (div1 / div2) ** 0.5
        #return 0 for ZeroDivision
        if s == 0:            
            return 0
        else:
            d1 = sum(G1) / len(G1) - sum(G2) / len(G2)
            return (d1 / s)
def main(csvfile):    
    #read CSV file
    try:
        with open(csvfile, 'r') as file:        
            # Read the header row-first row
            headers = next(file).strip().split(',')
            # lower all the headers' names
            header = [header.lower() for header in headers]
            # Determine the index of each column
            id_index = header.index('id')
            age_index = header.index('age')
            time_spent_index = header.index('time_spent_hour')
            engagement_index = header.index('engagement_score')
            platform_index = header.index('platform')
            profession_index = header.index('profession')
            income_index = header.index('income')
            lines = file.readlines()
        unique_ids = {}
        id_count = {}
        #process each line of the file
        for line in lines:
            #split each line into fields
            fields = line.strip().split(',')
            #extract ID from the fields
            user_id = fields[id_index].lower()
            key = user_id
            value = [fields[age_index],fields[time_spent_index],fields[engagement_index],fields[platform_index],fields[profession_index],fields[income_index]]
            #update id_count and unique_ids dictionary
            if key in id_count:
                # if so, increment the count of occurrences
                id_count[key] += 1
                #if this ID is already present in unique_ids,delete it to disregard all occurences of this ID
                if key in unique_ids:
                    del unique_ids[key]
            else:
                #if this is the first occurence of this ID, add it to unique_ids
                id_count[key] = 1
                unique_ids[key] = value                  
        #initialize dictionaries and lists to store data
        students1 = {}
        non_students1 = {}
        platform_engagement = {}
        students3 = []
        non_students3 = []
        students4 = []
        non_students4 = []      
        #retrieve data from the updated dictionary unique_ids, which key is valid user_id and value is other columns' values
        for k,v in unique_ids.items():
            try:
                #if age is not numeric, entire row will be ignored
                age = float(v[0])
                #if time_spent_hour is not numeric, entire row will be ignored
                time_spent_hour = float(v[1])
                #if engagement_score is not numeric, entire row will be ignored
                engagement_score = float(v[2])
                #if income is not numeric, entire row will be ignored
                income = float(v[5])
                if age < 0:
                    #if age is negative, entire row will be ignored
                    continue                   
                if time_spent_hour < 0:
                    #if time_spent_hour is negative,entire row will be ignored
                    continue
                if engagement_score < 0:
                    #if engagement_score is negative,entire row will be ignored
                    continue
                if not k.isalnum() or k == '':
                    #skip this line if user_id is not alphanumeric or empty
                    continue 
            except:
               continue
            platform = v[3].lower()
            if platform == '':
            #skip the line if platform is empty
                continue
            profession = v[4].lower()
            if profession == '':
                #skip the line if profession is empty
                continue
            #calculate engagement time
            engagement_time = (time_spent_hour * engagement_score) / 100
            #group the engagement times by platform
            if platform in platform_engagement:
                platform_engagement[platform].append(engagement_time)
            else:
                platform_engagement[platform] = [engagement_time]              
            #determine the value in a list
            data1 = [int(age), int(time_spent_hour), engagement_score]
            #check OP1 condition ,OP3 condition and OP4 condition
            if profession == 'student':
                students1[k] = data1
                students3.append((age,income))
                students4.append(engagement_time)
            else:
                non_students1[k] = data1
                non_students3.append((age,income))
                non_students4.append(engagement_time)
        #OP1 is a list of two dictionary:students and non_students
        OP1 = [students1, non_students1]
        #calculate total,average and standard deviation of engagement time for each platform
        OP2 = {}
        for platform, engagement_times in platform_engagement.items():
            total_engagement = round(sum(engagement_times),4)
            average_engagement = round((total_engagement / len(engagement_times)),4)
            standard_deviation_engagement = round(standard_deviation(engagement_times),4)
            OP2[platform] = [total_engagement, average_engagement, standard_deviation_engagement]     
        #calculate cosine similarity between age and income for students and non_students
        co_students = round(sim(*zip(*students3)),4)
        co_non_students = round(sim(*zip(*non_students3)),4)
        OP3 = [co_students,co_non_students]
        #A numeric value for Cohen’s d test for engagement time to find the difference between students and non_students
        OP4 = round(cohen(students4,non_students4),4)
    except:
        #graceful termination in case of any exception
        return ([{},{}],{},[],0)
    return (OP1,OP2,OP3,OP4)



