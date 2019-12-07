#LOAD LIBRARIES 
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import numpy as np 

#IMPORT DATA
raw_data = pd.read_csv('./survey.csv')
raw_data.head()

#CREATE GROUPBY (COUNTRY) ON SUM OF TREATEMENT 
def country_function(data):
    country_treatment = data.groupby("Country")["treatment"].count()
    country_treatment = country_treatment.reset_index()
    country_treatment = country_treatment.sort_values("treatment", ascending = False)
    country_treatment = country_treatment.reset_index()
    return country_treatment

print(country_function(raw_data))

#UNITED STATES RAW DATA
us_raw_data = raw_data[raw_data["Country"] == "United States"]
print(us_raw_data)

#GATHERING ALL REQUIRED COLUMNS OF DATA FOR FURTHER ANALYSIS:
us_analysis_state = us_raw_data[["state","treatment", "benefits", "wellness_program",
                                         "seek_help", "leave", "mental_health_consequence",
                                         "work_interfere"]]
print(us_analysis_state)

#FUNCTION: STATE AND RETURN COUNT OF TREATMENT FOR YES & NO
def us_count_treatment(treatment): 
    us_count_treatment = treatment.groupby(["state", "treatment"]).size()
    us_count_treatment = us_count_treatment.reset_index()
    us_count_treatment = us_count_treatment.sort_values("treatment", ascending = False)
    us_count_treatment = us_count_treatment.reset_index()
    us_count_treatment.columns = ["index", "state", "treatment", "Total_Count"]
    return us_count_treatment

us_individual_count_treatment = us_count_treatment(us_analysis_state)

#COUNT OF US TREATMENT
total_us_count_treatment = us_individual_count_treatment.drop('index', axis=1)
print(total_us_count_treatment)

#WHICH STATE SEEKED TREATMENT THE MOST? 
us_count_treatment_yes = total_us_count_treatment[total_us_count_treatment["treatment"] == "Yes"]
print(us_count_treatment_yes)

#WHICH STATE DID NOT SEEK TREATMENT THE MOST? 
us_count_treatment_no = total_us_count_treatment[total_us_count_treatment["treatment"] == "No"]
print(us_count_treatment_no)

#BAR CHART: SOUGHT TREATMENT THE MOST 
fig, ax = plt.subplots()
ax.bar(x=us_count_treatment_yes.state, height=us_count_treatment_yes.Total_Count)

plt.title('Treatment by State')
plt.xticks(rotation='vertical')
plt.xlabel('State')
plt.ylabel('Number of Those Who Sought Treatment')
plt.tight_layout(h_pad=100)

#BAR CHART: DID NOT SEEK TREATMENT THE MOST
fig, ax = plt.subplots()
ax.bar(x=us_count_treatment_no.state, height=us_count_treatment_no.Total_Count)

plt.title('Lack of Treatment by State')
plt.xticks(rotation='vertical')
plt.xlabel('State')
plt.ylabel('Number of Those Who Did Not Seek Treatment')
plt.tight_layout(h_pad=100)

#FOCUS MORE ON THE FOLLOWING STATES, AS THEY HAVE THE MOST VOLUME FOR TREATENT YES/NO:CA,WA,NY
us_target_ca = us_analysis_state[us_analysis_state["state"] == "CA"]
us_target_wa = us_analysis_state[us_analysis_state["state"] == "WA"]
us_target_ny = us_analysis_state[us_analysis_state["state"] == "NY"]
print(us_target_ca)
print(us_target_wa)
print(us_target_ny)

#BENEFITS VS TREATMENT BY STATE: CA 
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="benefits", hue_order = ["Don't know", "No", "Yes"], data = us_target_ca)
plt.title("Benefits vs. Treatment: California", fontsize=20)
plt.suptitle("Having Mental Health Benefits Lead to Treatment", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#BENEFITS VS TREATMENT BY STATE: WA 
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="benefits", hue_order = ["Don't know", "No", "Yes"], data = us_target_wa)
plt.title("Benefits vs. Treatment: Washington", fontsize=20)
plt.suptitle("Having Mental Health Benefits Lead to Treatment", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#BENEFITS VS TREATMENT BY STATE: NY 
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="benefits", hue_order = ["Don't know", "No", "Yes"], data = us_target_ny)
plt.title("Benefits vs. Treatment: New York", fontsize=20)
plt.suptitle("Having Mental Health Benefits Lead to Treatment", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#WELLNESS PROGRAM VS TREATMENT: CA 
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="wellness_program", hue_order = ["Don't know", "No", "Yes"], data = us_target_ca)
plt.title("Wellness Program's vs. Treatment: California", fontsize=20)
plt.suptitle("Do Mental Health Wellness Programs at Work Lead to Treatment", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#WELLNESS PROGRAM VS TREATMENT: WA 
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="wellness_program", hue_order = ["Don't know", "No", "Yes"], data = us_target_wa)
plt.title("Wellness Program's vs. Treatment: Washington", fontsize=20)
plt.suptitle("Do Mental Health Wellness Programs at Work Lead to Treatment", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#WELLNESS PROGRAM VS TREATMENT: NY 
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="wellness_program", hue_order = ["Don't know", "No", "Yes"], data = us_target_ny)
plt.title("Wellness Program's vs. Treatment: New York", fontsize=20)
plt.suptitle("Do Mental Health Wellness Programs at Work Lead to Treatment", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#EMPLOYEER PROVIDE RESOURCES TO SEEK HELP VS TREATMENT: CA
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="mental_health_consequence", hue_order = ["Don't know", "No", "Yes"], data = us_target_ca)
plt.title("Consequences of Mental Health vs. Treatment: California", fontsize=20)
plt.suptitle("Does Discussing Mental Health Issues with Your Employer Have Negative Consequences", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#EMPLOYEER PROVIDE RESOURCES TO SEEK HELP VS TREATMENT: WA
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="mental_health_consequence", hue_order = ["Don't know", "No", "Yes"], data = us_target_wa)
plt.title("Consequences of Mental Health vs. Treatment: Washington", fontsize=20)
plt.suptitle("Does Discussing Mental Health Issues with Your Employer Have Negative Consequences", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()

#EMPLOYEER PROVIDE RESOURCES TO SEEK HELP VS TREATMENT: NY
plt.figure(figsize=(10,9))
sns.countplot(x="treatment", hue="mental_health_consequence", hue_order = ["Don't know", "No", "Yes"], data = us_target_ny)
plt.title("Consequences of Mental Health vs. Treatment: New York", fontsize=20)
plt.suptitle("Does Discussing Mental Health Issues with Your Employer Have Negative Consequences", fontsize=24)
plt.xlabel("")
plt.ylabel("")
plt.show()