#TITLE SECTION
APP_TITTLE="Survey details- Prevalance and patterns of drug misuse in women of reproductive age group"
#OPTIONS SECTION
DEMOGRAPHIC_DETAILS_SUBHEADER ="Demographic Details"
YES ="Yes"
NEVER="Never"
YES_OR_NO_OPTIONS = ["No","Yes"]
DIET_OPTIONS = ["Veg", "Non-Veg"]
MARITAL_STATUS_OPTIONS = ["Married", "Unmarried"]
GAD_7_ANXIETY_OPTIONS = list({ "Not at all":0 , "Several Days" :1, "More than half the days" : 2 ," Nearly every day" : 3 }.items())
PHQ_OPTIONS= list({ "Not at all":0 , "Several Days" :1, "More than half the days" : 2 ," Nearly every day" : 3 }.items())

OPTIONS_OFTEN = list({"Never": 0, "Monthly or Less": 1, "2 to 4 times per month": 2, "2 to 3 times per week": 3,"4 or More times per week": 4}.items())
OPTIONS_UNITS = list({"0 to 2": 0, "3 to 4": 1, "5 to 6": 2, "7 to 8": 3,"10 or more": 4}.items())
OPTIONS_LAST_YEAR = list({"Never": 0, "Less than monthly": 1, "Monthly": 2, "Weekly": 3,"Daily or almost daily": 4}.items())
OPTIONS_CUT_DOWN = list({"No": 0, "Yes but not in the last year": 2, "Yes during the last year": 4}.items())

OPTIONS_Q2_OFTEN_SUBSTANCES = list({"Never": 0, "Once or Twice": 2, "Monthly": 3, "Weekly": 4,"Daily or Almost Daily": 6}.items())
OPTIONS_Q3_OFTEN_SUBSTANCES = list({"Never": 0, "Once or Twice": 3, "Monthly": 4, "Weekly": 5,"Daily or Almost Daily": 6}.items())
OPTIONS_Q4_OFTEN_SUBSTANCES =  list({"Never": 0, "Once or Twice": 4, "Monthly": 5, "Weekly": 6,"Daily or Almost Daily": 7}.items())
OPTIONS_Q5_OFTEN_SUBSTANCES =  list({"Never": 0, "Once or Twice": 5, "Monthly": 6, "Weekly": 7,"Daily or Almost Daily": 8}.items())
OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES =  list({"Never": 0, "Yes, in the past 3 months": 6, "Yes, but not in the past 3 months": 3}.items())

OPTIONS_DRUG_BY_INJECTION=list({"No,Never":"No,Never","Yes, in the past 3 months":"Yes, in the past 3 months","Yes, but not in the past 3 months":"Yes, but not in the past 3 months"}.items())
OPTIONS_MEDICATIONS_DURATION =list({"Past 1 Week":"Past 1 Week","Past 1 Month":"Past 1 Month","Past 3 Months":"Past 3 Months","Past 12 Months":"Past 12 Months","Past 2 - 5 Years":"Past 2 - 5 Years"}.items())

#DEMOGRAPHIC DETAILS SECTION

Q_PATIENT_NAME = "Name"
Q_AGE = "Age"
Q_LOCATION ="Location"
Q_OCCUPATION ="Occupation"
Q_EDUCATION ="Education"

PAST_MEDICAL_HISTORY_SUB_HEADER = "Past Medical History"
Q_ALLERGIES = "Allergies/Medications/Food/Environment/Others"
Q_ALLERGIES_DETAILS ="If Yes, What allergies you have ?"
Q_SURGICAL_HIST = "Surgical Procedures/Injuries"
Q_SURGICAL_PROCEDURE_DETAILS="If Yes, Please Give Surgical Procedure/Injuries Details"

Q_HYPER_TENSION_BP="Hyper Tension/High BP"
Q_DIABETES_MELLITUS="Diabetes Mellitus"
Q_HYPER_THYROID="Hyper Thyroid"
Q_HYPO_THYROID="Hypo Thyroid"
Q_COPD="COPD"
Q_PEPTIC_ULCER_DISEASE="Peptic Ulcer Disease"
Q_OTHER_MEDICAL_HIST="Other,Past Medical History"

#SOCIAL HISTORY SECTION
SOCIAL_HISTORY_SUB_HEADER = "Social History"
Q_SUBSTANCES_USE = "Any Substance Use ?"
Q_IS_SUBSTANCES_USED_YES = "What/Which substance using at present ?"
Q_SMOKING ="Smoking"
Q_ALCOHOL ="Alcohol"
Q_ALCOHOL_DETAILS ="Alcohol Details"
Q_DIET = "Diet"
Q_PHYSICAL_ACTIVITY = "Physical Activity"
Q_IS_PHYSICAL_ACTIVITY_YES ="If Yes , Give Physical activity details"
Q_NUMBER_OF_CHILDREN = "Number of Children"
Q_MARITAL_STS = "Marital Status"

# PAST 3 MONTHS PREVALENCE SECTION
Q_PAST_3_MONTHS_PREVALENCE = "Past 3 months Prevalence"
Q_PRESCRIPTION_MEDI="Any Physician Prescription Medications ?"
Q_PRESCRIPTION_MEDI_DETAILS ="Physician Prescription Medications"
Q_PRESCRIPTION_MEDI_DURATION ="Physician Prescription Medications Duration"

Q_NON_PRESCRIPTION_MEDI ="Any Non Prescription Medications ?"
Q_NON_PRESCRIPTION_MEDI_DETAILS = "Non Prescription Medications "
Q_NON_PRESCRIPTION_MEDI_DURATION = "Non Prescription Medications Duration"

Q_OTC_MEDI ="Any OTC Medications ?"
Q_OTC_MEDI_DETAILS = "OTC Medications Medications"
Q_OTC_MEDI_DURATION = "OTC Medications Medications Duration"


GAD_7_ANXIETY_HEADER= "GAD-7 Anxiety"
GAD_7_ANXIETY_OPTIONS_INFO ="0 → Not at all, \n 1 → Several Days, \n 2 → More than half the days, \n 3 → Nearly every day"
Q_FEELING_NERVOUS="Feeling nervous,anxious,or on edge"
Q_NOT_ABLE_STOP_WORRY="Not being able to stop or control worrying"
Q_GAD_WORRYING_TOO_MUCH ="Worrying too much about different things"
Q_GAD_TROUBLE_RELAXING = "Trouble relaxing "
Q_GAD_BEING_SO_RESTLESS = "Being so restless that is it hard to sit still "
Q_GAD_BECOMING_EASILY_ANNOYED = "Becoming easily annoyed or irritable"
Q_GAD_FEELING_AFRAID = "Feeling afraid, as if something awful might happen"


# PATIENT HEALTH QUESTIONNAIRE -9 (PHQ-9) SECTION
PHQ_HEADER = "Patient Health Questionnaire -9 (PHQ-9)"
PHQ_OPTIONS_INFO = "0 → Not at all, \n 1 → Several Days, \n 2 → More than half the days, \n 3 → Nearly every day"
Q_PHQ_LITTLE_INTEREST= "Little interest or pleasure in doing things"
Q_PHQ_FEELING_DOWN ="Feeling down, depressed, or hopeless"
Q_PHQ_TROUBLE_FALLING = "Trouble falling or staying asleep, or sleeping too much"
Q_PHQ_FEELING_TIRED = "Feeling tired or having little energy"
Q_PHQ_POOR_APPETITE="Poor appetite or overeating"
Q_PHQ_FEELING_BAD_ABOUT_UR_SELF="Feeling bad about yourself - or that you are a failure or have let yourself or your family down"
Q_PHQ_TROUBLE_CONCENTRATION = "Trouble concentrating on things, such as reading the newspaper or watching television"
Q_PHQ_MOVING_OR_SPEAKING_SO_SLOW = "Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual "
Q_PHQ_THOUGHTS_THAT="Thoughts that you would be better off dead, or of hurting yourself in some way"


ASSIST_V3_HEADER = "WHO ASSIST V3.1"
Q1_IN_LIFE_SUBSTANCES_USED_HEADER = "Q1.In your life, which of the following substances have you ever used? (NON-MEDICAL USE ONLY)"
Q1A_TOBACCO_PRODUCTS = "Q1.a.Tobacco products (cigarettes, chewing tobacco, cigars, etc.)"
Q1B_ALCOHOLIC_PRODUCTS = "Q1.b.Alcoholic beverages (beer, wine, spirits, etc.)"
Q1C_CANNABIS="Q1.c.Cannabis (marijuana, pot, grass, hash, etc.)"
Q1D_COCAINE = "Q1.d.Cocaine (coke, crack, etc.)"
Q1E_AMPHETAMINE_TYPE_STIMULANTS = "Q1.e.Amphetamine type stimulants (speed, meth, ecstasy, ice etc.)"
Q1F_INHALANTS = "Q1.f.Inhalants (nitrous, glue, petrol, paint thinner, etc.)"
Q1G_SEDATIVES_OR_SLEEPING_PILLS = "Q1.g.Sedatives or Sleeping Pills (Valium, Serepax, Rohypnol,Temazepam, Normison, Stilnox, etc.)"
Q1H_HALLUCINOGENS = "Q1.h.Hallucinogens (LSD, acid, mushrooms, trips, Ketamine, etc.)"
Q1I_OPIOIDS = "Q1.i.Opioids (heroin, morphine, methadone, opium,Buprenorphine, codeine, etc.)"
Q1J_OTHER_SPECIFY = "Q1.j.Other :"
Q1K_OTHER_SPECIFY_YES = "Q1.k.specify:"



Q2A_TOBACCO_PRODUCTS = "Q2.a.Tobacco products (cigarettes, chewing tobacco, cigars, etc.)"
Q2B_ALCOHOLIC_PRODUCTS = "Q2.b.Alcoholic beverages (beer, wine, spirits, etc.)"
Q2C_CANNABIS="Q2.c.Cannabis (marijuana, pot, grass, hash, etc.)"
Q2D_COCAINE = "Q2.d.Cocaine (coke, crack, etc.)"
Q2E_AMPHETAMINE_TYPE_STIMULANTS = "Q2.e.Amphetamine type stimulants (speed, meth, ecstasy, ice etc.)"
Q2F_INHALANTS = "Q2.f.Inhalants (nitrous, glue, petrol, paint thinner, etc.)"
Q2G_SEDATIVES_OR_SLEEPING_PILLS = "Q2.g.Sedatives or Sleeping Pills (Valium, Serepax, Rohypnol,Temazepam, Normison, Stilnox, etc.)"
Q2H_HALLUCINOGENS = "Q2.h.Hallucinogens (LSD, acid, mushrooms, trips, Ketamine, etc.)"
Q2I_OPIOIDS = "Q2.i.Opioids (heroin, morphine, methadone, opium,Buprenorphine, codeine, etc.)"
Q2J_OTHER_SPECIFY = "Q2.j.Other :"
Q2K_OTHER_SPECIFY_YES = "Q2.k.specify:"



Q3A_TOBACCO_PRODUCTS = "Q3.a.Tobacco products (cigarettes, chewing tobacco, cigars, etc.)"
Q3B_ALCOHOLIC_PRODUCTS = "Q3.b.Alcoholic beverages (beer, wine, spirits, etc.)"
Q3C_CANNABIS="Q3.c.Cannabis (marijuana, pot, grass, hash, etc.)"
Q3D_COCAINE = "Q3.d.Cocaine (coke, crack, etc.)"
Q3E_AMPHETAMINE_TYPE_STIMULANTS = "Q3.e.Amphetamine type stimulants (speed, meth, ecstasy, ice etc.)"
Q3F_INHALANTS = "Q3.f.Inhalants (nitrous, glue, petrol, paint thinner, etc.)"
Q3G_SEDATIVES_OR_SLEEPING_PILLS = "Q3.g.Sedatives or Sleeping Pills (Valium, Serepax, Rohypnol,Temazepam, Normison, Stilnox, etc.)"
Q3H_HALLUCINOGENS = "Q3.h.Hallucinogens (LSD, acid, mushrooms, trips, Ketamine, etc.)"
Q3I_OPIOIDS = "Q3.i.Opioids (heroin, morphine, methadone, opium,Buprenorphine, codeine, etc.)"
Q3J_OTHER_SPECIFY = "Q3.j.Other :"
Q3K_OTHER_SPECIFY_YES = "Q3.k.specify:"



Q4A_TOBACCO_PRODUCTS = "Q4.a.Tobacco products (cigarettes, chewing tobacco, cigars, etc.)"
Q4B_ALCOHOLIC_PRODUCTS = "Q4.b.Alcoholic beverages (beer, wine, spirits, etc.)"
Q4C_CANNABIS="Q4.c.Cannabis (marijuana, pot, grass, hash, etc.)"
Q4D_COCAINE = "Q4.d.Cocaine (coke, crack, etc.)"
Q4E_AMPHETAMINE_TYPE_STIMULANTS = "Q4.e.Amphetamine type stimulants (speed, meth, ecstasy, ice etc.)"
Q4F_INHALANTS = "Q4.f.Inhalants (nitrous, glue, petrol, paint thinner, etc.)"
Q4G_SEDATIVES_OR_SLEEPING_PILLS = "Q4.g.Sedatives or Sleeping Pills (Valium, Serepax, Rohypnol,Temazepam, Normison, Stilnox, etc.)"
Q4H_HALLUCINOGENS = "Q4.h.Hallucinogens (LSD, acid, mushrooms, trips, Ketamine, etc.)"
Q4I_OPIOIDS = "Q4.i.Opioids (heroin, morphine, methadone, opium,Buprenorphine, codeine, etc.)"
Q4J_OTHER_SPECIFY = "Q4.j.Other :"
Q4K_OTHER_SPECIFY_YES = "Q4.k.specify:"



Q5A_TOBACCO_PRODUCTS = "Q5.a.Tobacco products (cigarettes, chewing tobacco, cigars, etc.)"
Q5B_ALCOHOLIC_PRODUCTS = "Q5.b.Alcoholic beverages (beer, wine, spirits, etc.)"
Q5C_CANNABIS="Q5.c.Cannabis (marijuana, pot, grass, hash, etc.)"
Q5D_COCAINE = "Q5.d.Cocaine (coke, crack, etc.)"
Q5E_AMPHETAMINE_TYPE_STIMULANTS = "Q5.e.Amphetamine type stimulants (speed, meth, ecstasy, ice etc.)"
Q5F_INHALANTS = "Q5.f.Inhalants (nitrous, glue, petrol, paint thinner, etc.)"
Q5G_SEDATIVES_OR_SLEEPING_PILLS = "Q5.g.Sedatives or Sleeping Pills (Valium, Serepax, Rohypnol,Temazepam, Normison, Stilnox, etc.)"
Q5H_HALLUCINOGENS = "Q5.h.Hallucinogens (LSD, acid, mushrooms, trips, Ketamine, etc.)"
Q5I_OPIOIDS = "Q5.i.Opioids (heroin, morphine, methadone, opium,Buprenorphine, codeine, etc.)"
Q5J_OTHER_SPECIFY = "Q5.j.Other :"
Q5K_OTHER_SPECIFY_YES = "Q5.k.specify:"


Q6A_TOBACCO_PRODUCTS = "Q6.a.Tobacco products (cigarettes, chewing tobacco, cigars, etc.)"
Q6B_ALCOHOLIC_PRODUCTS = "Q6.b.Alcoholic beverages (beer, wine, spirits, etc.)"
Q6C_CANNABIS="Q6.c.Cannabis (marijuana, pot, grass, hash, etc.)"
Q6D_COCAINE = "Q6.d.Cocaine (coke, crack, etc.)"
Q6E_AMPHETAMINE_TYPE_STIMULANTS = "Q6.e.Amphetamine type stimulants (speed, meth, ecstasy, ice etc.)"
Q6F_INHALANTS = "Q6.f.Inhalants (nitrous, glue, petrol, paint thinner, etc.)"
Q6G_SEDATIVES_OR_SLEEPING_PILLS = "Q6.g.Sedatives or Sleeping Pills (Valium, Serepax, Rohypnol,Temazepam, Normison, Stilnox, etc.)"
Q6H_HALLUCINOGENS = "Q6.h.Hallucinogens (LSD, acid, mushrooms, trips, Ketamine, etc.)"
Q6I_OPIOIDS = "Q6.i.Opioids (heroin, morphine, methadone, opium,Buprenorphine, codeine, etc.)"
Q6J_OTHER_SPECIFY = "Q6.j.Other :"
Q6K_OTHER_SPECIFY_YES = "Q6.k.specify:"


Q7A_TOBACCO_PRODUCTS = "Q7.a.Tobacco products (cigarettes, chewing tobacco, cigars, etc.)"
Q7B_ALCOHOLIC_PRODUCTS = "Q7.b.Alcoholic beverages (beer, wine, spirits, etc.)"
Q7C_CANNABIS="Q7.c.Cannabis (marijuana, pot, grass, hash, etc.)"
Q7D_COCAINE = "Q7.d.Cocaine (coke, crack, etc.)"
Q7E_AMPHETAMINE_TYPE_STIMULANTS = "Q7.e.Amphetamine type stimulants (speed, meth, ecstasy, ice etc.)"
Q7F_INHALANTS = "Q7.f.Inhalants (nitrous, glue, petrol, paint thinner, etc.)"
Q7G_SEDATIVES_OR_SLEEPING_PILLS = "Q7.g.Sedatives or Sleeping Pills (Valium, Serepax, Rohypnol,Temazepam, Normison, Stilnox, etc.)"
Q7H_HALLUCINOGENS = "Q7.h.Hallucinogens (LSD, acid, mushrooms, trips, Ketamine, etc.)"
Q7I_OPIOIDS = "Q7.i.Opioids (heroin, morphine, methadone, opium,Buprenorphine, codeine, etc.)"
Q7J_OTHER_SPECIFY = "Q7.j.Other :"
Q7K_OTHER_SPECIFY_YES = "Q7.k.specify:"

Q2_PAST_THREE_MONTHS_SUBSTANCES_SUB_HEADER = "Q2.In the past three months, how often have you used the substances you mentioned (FIRST DRUG,SECOND DRUG, ETC)?"
Q3_PAST_THREE_MONTHS_HOW_OFTEN_STRONG_DESIRE_SUBHEADER = "Q3.During the past three months, how often have you had a strong desire or urge to use (FIRST DRUG, SECOND DRUG, ETC)?"
Q4_PAST_THREE_MONTHS_HOW_OFTEN_YOUR_USE = "Q4.During the past three months, how often has your use of (FIRST DRUG, SECOND DRUG, ETC) led to health, social, legal or financial problems?"
Q5_PAST_THREE_MONTHS_HOW_OFTEN_YOUR_FAILED_TO_DO = "Q5.During the past three months, how often have you failed to do what was normally expected of you because of your use of (FIRST DRUG, SECOND DRUG, ETC)?"
Q6_HAS_A_FRIEND_OR_RELATIVE_CONCERN = "Q6.Has a friend or relative or anyone else ever expressed concern about your use of (FIRST DRUG, SECOND DRUG, ETC.)??"
Q7_HAS_EVER_TRIED_TO_CUT_DOWN_ON = "Q7.Have you ever tried to cut down on using (FIRST DRUG,SECOND DRUG, ETC.) but failed?"

Q8_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION = "Q8.Have you ever used any drug by injection? (NON-MEDICAL USE ONLY)"

SUBSTANCE_SCORE ="Substance Score"
TOTAL_A_TOBACCO_SCORE ="Tobacco " +SUBSTANCE_SCORE
TOTAL_B_ALCOHOL_SCORE ="Alcohol " +SUBSTANCE_SCORE
TOTAL_C_CANNABIS_SCORE ="Cannabis " +SUBSTANCE_SCORE
TOTAL_D_COCAINE_SCORE ="Cocaine " +SUBSTANCE_SCORE
TOTAL_E_AMPHETAMINES_SCORE ="Amphetamines " +SUBSTANCE_SCORE
TOTAL_F_INHALANTS_SCORE ="Inhalants " +SUBSTANCE_SCORE
TOTAL_G_SEDATIVES_SCORE ="Sedatives " +SUBSTANCE_SCORE
TOTAL_H_HALLUCINOGENS_SCORE ="Hallucinogens " +SUBSTANCE_SCORE
TOTAL_I_OPIOIDS_SCORE ="Opioids " +SUBSTANCE_SCORE
TOTAL_J_OTHER_DRUGS_SCORE ="Other drugs " +SUBSTANCE_SCORE


NO_INTERVENTION = "No Intervention"
RECEIVE_BRIEF_INTERVENTION = "Receive Brief Intervention"
MORE_INTENSIVE_TREATMENT ="More Intensive Treatment"

INTERVENTION_TYPE ="Intervention Type"
A_TOBACCO_INTERVENTION_TYPE ="Tobacco " +INTERVENTION_TYPE
B_ALCOHOL_INTERVENTION_TYPE ="Alcohol " +INTERVENTION_TYPE
C_CANNABIS_INTERVENTION_TYPE ="Cannabis " +INTERVENTION_TYPE
D_COCAINE_INTERVENTION_TYPE ="Cocaine " +INTERVENTION_TYPE
E_AMPHETAMINES_INTERVENTION_TYPE ="Amphetamines " +INTERVENTION_TYPE
F_INHALANTS_INTERVENTION_TYPE ="Inhalants " +INTERVENTION_TYPE
G_SEDATIVES_INTERVENTION_TYPE ="Sedatives " +INTERVENTION_TYPE
H_HALLUCINOGENS_INTERVENTION_TYPE="Hallucinogens " +INTERVENTION_TYPE
I_OPIOIDS_INTERVENTION_TYPE ="Opioids " +SUBSTANCE_SCORE
J_OTHER_INTERVENTION_TYPE ="Other drugs " +INTERVENTION_TYPE

SHEET_NAME ="Patient_Survey_V1_IRIS"
scope =["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/spreadsheets"]
