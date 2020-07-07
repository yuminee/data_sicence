import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.

allowed = df['status'] == 'allowed'

#같은 크기의 강의실이 필요한 과목에 대해 알파벳 순서대로 방 번호를 배정하세요.
#예를 들어 Auditorium이 필요한 과목으로 “arts”, “commerce”, “science” 세 과목이 있다면,
#“arts”는 “Auditorium-1”, “commerce”는 “Auditorium-2”, “science”는 “Auditorium-3” 순서로 방 배정이 되어야 합니다.

“status” column이 “not allowed”인 수강생은 “room assignment” column을 그대로 “not assigned”로 남겨둡니다.

“room assignment” column의 이름을 “room number”로 바꿔주세요.
course_counts = df.loc[allowed, "course name"].value_counts()

auditorium_course = list(course_counts[course_counts >=80 ].index)
large_course = list(course_counts[(course_counts <80) & (course_counts>=40) ].index)
medium_course = list(course_counts[(course_counts <40) & (course_counts>=15) ].index)
small_course = list(course_counts[(course_counts <15) & (course_counts>=5) ].index)
df.rename(columns={'room assignment':'room number'}, inplace = 'True')

d =sorted(auditorium_course)

a =sorted(large_course)
b = sorted(medium_course)
c =sorted(small_course)


for i in range(0, len(auditorium_course)):
    df.loc[(df['course name']== d[i]) & allowed, "room number"] = 'Auditorium-'+str(i+1)
    
for i in range(0, len(large_course)):
    df.loc[(df['course name']== a[i]) & allowed, "room number"] = 'Large-'+str(i+1)
    
for i in range(0, len(medium_course)):
    df.loc[(df['course name']== b[i]) & allowed, "room number"] = 'Medium-'+str(i+1)
        
for i in range(0, len(small_course)):
    df.loc[(df['course name']== c[i]) & allowed, "room number"] = 'Small-'+str(i+1)        
 
 

df
