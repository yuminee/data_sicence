import pandas as pd

#status칼럼을추가
#information_technology과목은_1학년은_들을_수_없다
#commerce과목은_4학년은_들을_수_없다
#수강인원이_5보다작으면_폐강된다

df = pd.read_csv('data/enrolment_1.csv')
df["status"] = "allowed"

# 조건 1
boolean1 = df["course name"] == "information technology"
boolean2 = df["year"] == 1
df.loc[boolean1 & boolean2, "status"] = "not allowed"

# 조건 2
boolean3= df["course name"] == "commerce"
boolean4= df["year"] == 4
df.loc[boolean3& boolean4, "status"] = "not allowed"

# 조건 3
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
    df.loc[df["course name"] == course, "status"] = "not allowed"

# 정답 확인
df
