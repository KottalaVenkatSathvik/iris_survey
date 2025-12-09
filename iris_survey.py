import os.path

import gspread
import streamlit as st

from google.oauth2.service_account import Credentials

def find_intervention_type(value, low,mid,high):
    return Constants.NO_INTERVENTION if low <= value < mid else Constants.RECEIVE_BRIEF_INTERVENTION if mid <=value<high else Constants.MORE_INTENSIVE_TREATMENT

import copy
import Constants
from Constants import Q_GAD_BECOMING_EASILY_ANNOYED, Q_GAD_FEELING_AFRAID, TOTAL_E_AMPHETAMINES_SCORE, \
    TOTAL_F_INHALANTS_SCORE
from survey_data_schema import SURVE_DEFAULTS


# survey_data = copy.deepcopy(SURVE_DEFAULTS)

service_acnt_path="survey-account.json"

if os.path.exists("/etc/secrets/survey-account.json"):
    service_acnt_path = "/etc/secrets/survey-account.json"

creds= Credentials.from_service_account_file(service_acnt_path,scopes=Constants.scope)
client =gspread.authorize(creds)
sheet = client.open(Constants.SHEET_NAME).sheet1

############################# APP TITLE #####################################
st.markdown(f"<h1 style='text-align: center;color: #096f7a'>{Constants.APP_TITTLE}</h1>", unsafe_allow_html=True)
############################# DEMOGRAPHIC SECTION - START #####################################
# Collect answers
st.header(Constants.DEMOGRAPHIC_DETAILS_SUBHEADER)
name = st.text_input(Constants.Q_PATIENT_NAME,key=Constants.Q_PATIENT_NAME)
age = st.number_input(Constants.Q_AGE, min_value=0, max_value=150,key=Constants.Q_AGE)
location = st.text_input(Constants.Q_LOCATION,key=Constants.Q_LOCATION)
# occupation = st.text_input(Constants.Q_OCCUPATION)
employment_status = st.selectbox(Constants.Q_EMPLOYMENT_STATUS,Constants.Q_EMPLOYMENT_STATUS_OPTIONS,format_func=lambda x: x,key=Constants.Q_EMPLOYMENT_STATUS)
# education = st.text_input(Constants.Q_EDUCATION)
education_attainment = st.selectbox(Constants.Q_EDUCATIONAL_ATTAINMENT,Constants.Q_EDUCATIONAL_ATTAINMENT_OPTIONS,format_func=lambda x: x,key=Constants.Q_EDUCATIONAL_ATTAINMENT)


############################## PAST_MEDICAL_HISTORY_SUB_HEADER
st.subheader(Constants.PAST_MEDICAL_HISTORY_SUB_HEADER)
allergies = st.radio(Constants.Q_ALLERGIES,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_ALLERGIES)
# survey_data[Constants.Q_ALLERGIES] = allergies

if allergies == Constants.YES:
    allergies_details= st.text_input(Constants.Q_ALLERGIES_DETAILS,key=Constants.Q_ALLERGIES_DETAILS)
    # survey_data[Constants.Q_ALLERGIES_DETAILS] = allergies_details

surgical_procedures = st.radio(Constants.Q_SURGICAL_HIST,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_SURGICAL_HIST)
# survey_data[Constants.Q_SURGICAL_HIST] = surgical_procedures
if surgical_procedures == Constants.YES:
    surgical_procedures_details = st.text_input(Constants.Q_SURGICAL_PROCEDURE_DETAILS,key=Constants.Q_SURGICAL_PROCEDURE_DETAILS)
    # survey_data[Constants.Q_SURGICAL_PROCEDURE_DETAILS] =surgical_procedures_details

a_bp = st.radio(Constants.Q_HYPER_TENSION_BP,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_HYPER_TENSION_BP)
a_diabetes_mellitus = st.radio(Constants.Q_DIABETES_MELLITUS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DIABETES_MELLITUS)
a_hyper_thyroid = st.radio(Constants.Q_HYPER_THYROID,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_HYPER_THYROID)
a_hypo_thyroid = st.radio(Constants.Q_HYPO_THYROID,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_HYPO_THYROID)
a_copd = st.radio(Constants.Q_COPD,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_COPD)
a_peptic_ulcer_disease = st.radio(Constants.Q_PEPTIC_ULCER_DISEASE,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_PEPTIC_ULCER_DISEASE)
a_OTHER = st.text_input(Constants.Q_OTHER_MEDICAL_HIST,key=Constants.Q_OTHER_MEDICAL_HIST)

############################## SOCIAL_HISTORY_SUB_HEADER
st.subheader(Constants.SOCIAL_HISTORY_SUB_HEADER)
substance_used = st.radio(Constants.Q_SUBSTANCES_USE,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_SUBSTANCES_USE)
if substance_used == Constants.YES:
    substances_details = st.text_input(Constants.Q_IS_SUBSTANCES_USED_YES,key=Constants.Q_IS_SUBSTANCES_USED_YES)    
smoking = st.radio(Constants.Q_SMOKING, Constants.YES_OR_NO_OPTIONS,key=Constants.Q_SMOKING)
alcohol = st.radio(Constants.Q_ALCOHOL, Constants.YES_OR_NO_OPTIONS,key=Constants.Q_ALCOHOL)
if alcohol == Constants.YES:
    alcohol_details = st.text_input(Constants.Q_ALCOHOL_DETAILS,key=Constants.Q_ALCOHOL_DETAILS)
diet = st.radio(Constants.Q_DIET, Constants.DIET_OPTIONS,key=Constants.Q_DIET)
physical_activity = st.radio(Constants.Q_PHYSICAL_ACTIVITY, Constants.YES_OR_NO_OPTIONS,key=Constants.Q_PHYSICAL_ACTIVITY)
if physical_activity==Constants.YES:
    physical_activity_details = st.text_input(Constants.Q_IS_PHYSICAL_ACTIVITY_YES,key=Constants.Q_IS_PHYSICAL_ACTIVITY_YES)
    
#####################################################
marital_status = st.radio(Constants.Q_MARITAL_STS, Constants.MARITAL_STATUS_OPTIONS,key=Constants.Q_MARITAL_STS)
if marital_status == Constants.MARITAL_STATUS_OPTIONS[0]:
    present_pregency = st.radio(Constants.Q_PRESENT_PREGNANCY,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_PRESENT_PREGNANCY)
    any_physical_violence = st.radio(Constants.Q_IF_MARRIED_ANY_PY_PHYSICAL_VIOLENCE_YES_OR_NO,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_IF_MARRIED_ANY_PY_PHYSICAL_VIOLENCE_YES_OR_NO)
    #########################################################
    num_of_children = st.selectbox(Constants.Q_NUMBER_OF_CHILDREN,Constants.Q_NUMBER_CHILDREN_OPTIONS,key=Constants.Q_NUMBER_OF_CHILDREN)
    if num_of_children>0:
        children_data={}
        for i in range(1,int(num_of_children)+1):
            c_normal = st.selectbox(Constants.Q_C_SEC_NORMAL.format(NO=i),Constants.Q_C_SECTION_NORMAL_OPTIONS,key=Constants.Q_C_SEC_NORMAL.format(NO=i))
            children_data[i]=c_normal

        
        children_data_hist={}

        for i in range(1,int(num_of_children)+1):
            c_normal = st.selectbox(Constants.Q_HISTORY_OF_CHILD_BIRTH.format(NO=i),Constants.Q_HISTORY_CHILD_BIRTH_OPTIONS,key=Constants.Q_HISTORY_OF_CHILD_BIRTH.format(NO=i))
            children_data_hist[i]=c_normal
        

    ########################################################
    abortions = st.radio(Constants.Q_ABORTIONS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_ABORTIONS)
    
    if abortions == Constants.YES:
        how_many_abortions=st.number_input(Constants.Q_HOW_MANY_ABORTED,min_value=0,key=Constants.Q_HOW_MANY_ABORTED)    
#################################
menstrual_cycle = st.radio(Constants.Q_MENSTRUAL_CYCLE,Constants.Q_MENSTRUAL_CYCLE_OPTIONS,key=Constants.Q_MENSTRUAL_CYCLE)
if menstrual_cycle == Constants.Q_MENSTRUAL_CYCLE_OPTIONS[1]:
    frequency_irregular = st.selectbox(Constants.Q_MENSTRUAL_CYCLE_IRREGULAR_FREQ,Constants.Q_MENSTRUAL_CYCLE_FREQUENCY_OPTIONS,format_func= lambda x : x[0],key=Constants.Q_MENSTRUAL_CYCLE_IRREGULAR_FREQ)
    st.session_state[Constants.Q_MENSTRUAL_CYCLE_IRREGULAR_FREQ]=frequency_irregular[0]
#################################

pocd = st.radio(Constants.Q_PCOD,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_PCOD)
pcos = st.radio(Constants.Q_PCOS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_PCOS)

#######################################Q_PAST_3_MONTHS_PREVALENCE

st.subheader(Constants.Q_PAST_3_MONTHS_PREVALENCE)
any_prescription_medications = st.radio(Constants.Q_PRESCRIPTION_MEDI,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_PRESCRIPTION_MEDI)
if any_prescription_medications == Constants.YES:
    prescription_medications_details = st.text_input(Constants.Q_PRESCRIPTION_MEDI_DETAILS,key=Constants.Q_PRESCRIPTION_MEDI_DETAILS)
    prescription_medications_duration = st.selectbox(Constants.Q_PRESCRIPTION_MEDI_DURATION,Constants.OPTIONS_MEDICATIONS_DURATION,format_func=lambda x: x[0])    
    st.session_state[Constants.Q_PRESCRIPTION_MEDI_DURATION] = prescription_medications_duration[1]

any_non_prescription_medications = st.radio(Constants.Q_NON_PRESCRIPTION_MEDI,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_NON_PRESCRIPTION_MEDI)
if any_non_prescription_medications == Constants.YES:
    non_prescription_medications_details = st.text_input(Constants.Q_NON_PRESCRIPTION_MEDI_DETAILS,key=Constants.Q_NON_PRESCRIPTION_MEDI_DETAILS)
    non_prescription_medications_duration = st.selectbox(Constants.Q_NON_PRESCRIPTION_MEDI_DURATION,Constants.OPTIONS_MEDICATIONS_DURATION,format_func=lambda x: x[0])
    
    st.session_state[Constants.Q_OTC_MEDI_DURATION] = non_prescription_medications_duration[1]

any_otc_medications = st.radio(Constants.Q_OTC_MEDI,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_OTC_MEDI)
if any_otc_medications == Constants.YES:
    otc_medications_details = st.text_input(Constants.Q_OTC_MEDI_DETAILS,key=Constants.Q_OTC_MEDI_DETAILS)
    otc_medications_duration = st.selectbox(Constants.Q_OTC_MEDI_DURATION,Constants.OPTIONS_MEDICATIONS_DURATION,format_func=lambda x: x[0])
    st.session_state[Constants.Q_OTC_MEDI_DURATION] = otc_medications_duration[1]



############################# Drug Abuse Screening Test (DAST-10) SECTION - START #####################################
st.header(Constants.DAST_HEADER)
a_dast_drugs_used_med_reasons = st.radio(Constants.Q_DAST_DRUGS_USED_MED_REASONS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_DRUGS_USED_MED_REASONS)
a_dast_more_than_one_drug_at_a_time = st.radio(Constants.Q_DAST_MORE_THAN_ONE_DRUG_AT_A_TIME,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_MORE_THAN_ONE_DRUG_AT_A_TIME)
a_dast_unable_stop_abusing_drugs = st.radio(Constants.Q_DAST_UNABLE_STOP_ABUSING_DRUGS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_UNABLE_STOP_ABUSING_DRUGS)
a_dast_have_ever_had_blackouts = st.radio(Constants.Q_DAST_HAVE_EVER_HAD_BLACKOUTS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_HAVE_EVER_HAD_BLACKOUTS)
a_dast_feel_bad_guilty = st.radio(Constants.Q_DAST_FEEL_BAD_GUILTY,Constants.YES_OR_NO_OPTIONS,key =Constants.Q_DAST_FEEL_BAD_GUILTY)
a_dast_deos_ur_spouse_ever_comp = st.radio(Constants.Q_DAST_DEOS_UR_SPOUSE_EVER_COMP,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_DEOS_UR_SPOUSE_EVER_COMP)
a_dast_you_neglected_ur_family = st.radio(Constants.Q_DAST_YOU_NEGLECTED_UR_FAMILY,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_YOU_NEGLECTED_UR_FAMILY)
a_dast_have_you_engaged_in_illegal = st.radio(Constants.Q_DAST_HAVE_YOU_ENGAGED_IN_ILLEGAL,Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_HAVE_YOU_ENGAGED_IN_ILLEGAL)
a_dast_expr_withdrawal_symptoms = st.radio(Constants.Q_DAST_EXPR_WITHDRAWAL_SYMPTOMS, Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_EXPR_WITHDRAWAL_SYMPTOMS)
a_dast_have_medical_problems = st.radio(Constants.Q_DAST_HAVE_MEDICAL_PROBLEMS, Constants.YES_OR_NO_OPTIONS,key=Constants.Q_DAST_HAVE_MEDICAL_PROBLEMS)


a_dast1_score = 1 if a_dast_drugs_used_med_reasons == Constants.YES else 0
a_dast2_score = 1 if a_dast_more_than_one_drug_at_a_time == Constants.YES else 0
a_dast3_score = 0 if a_dast_unable_stop_abusing_drugs == Constants.YES else 1
a_dast4_score = 1 if a_dast_have_ever_had_blackouts == Constants.YES else 0
a_dast5_score = 1 if a_dast_feel_bad_guilty == Constants.YES else 0
a_dast6_score = 1 if a_dast_deos_ur_spouse_ever_comp == Constants.YES else 0
a_dast7_score = 1 if a_dast_you_neglected_ur_family == Constants.YES else 0
a_dast8_score = 1 if a_dast_have_you_engaged_in_illegal == Constants.YES else 0
a_dast9_score = 1 if a_dast_expr_withdrawal_symptoms == Constants.YES else 0
a_dast10_score = 1 if a_dast_have_medical_problems == Constants.YES else 0

interpretion_score = a_dast1_score + a_dast2_score+a_dast3_score+a_dast4_score+a_dast5_score+a_dast6_score+a_dast7_score+a_dast8_score+a_dast9_score+a_dast10_score
st.session_state[Constants.Q_DAST_INTERPRETION_OF_SCORE] = interpretion_score

degree_cal=''

if interpretion_score == 0:
    degree_cal =Constants.DEGREE_OF_PROB_NO_PROBL    
elif 1<= interpretion_score <=2:
    degree_cal = Constants.DEGREE_OF_PROB_LOW_LEVEL    
elif 3<= interpretion_score <=5:
    degree_cal = Constants.DEGREE_OF_PROB_MODERATE_LEVEL
elif 6<= interpretion_score <=8:
    degree_cal = Constants.DEGREE_OF_PROB_SUBSTANTIAL_LEVEL
else:
    degree_cal = Constants.DEGREE_OF_PROB_SEVERE_LEVEL
  
st.session_state[Constants.Q_DEGREE_OF_PROBLEM_RELATED_TO_DRUG_ABUSE]  = degree_cal['degree']

st.session_state[Constants.Q_SUGGESTED_ACTION]  = degree_cal['action']

############################# ASSIST V3.1 - START #####################################
st.header(Constants.ASSIST_V3_HEADER)
st.subheader(Constants.Q1_IN_LIFE_SUBSTANCES_USED_HEADER)

Q1AA_TOBACCO_PRODUCTS = st.radio(Constants.Q1A_TOBACCO_PRODUCTS,Constants.YES_OR_NO_OPTIONS,key = Constants.Q1A_TOBACCO_PRODUCTS)
Q1BA_ALCOHOLIC_PRODUCTS = st.radio(Constants.Q1B_ALCOHOLIC_PRODUCTS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1B_ALCOHOLIC_PRODUCTS)
Q1CA_CANNABIS = st.radio(Constants.Q1C_CANNABIS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1C_CANNABIS)
Q1DA_COCAINE =st.radio(Constants.Q1D_COCAINE,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1D_COCAINE)
Q1EA_AMPHETAMINE_TYPE_STIMULANTS =st.radio(Constants.Q1E_AMPHETAMINE_TYPE_STIMULANTS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1E_AMPHETAMINE_TYPE_STIMULANTS)
Q1FA_INHALANTS =st.radio(Constants.Q1F_INHALANTS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1F_INHALANTS)
Q1GA_SEDATIVES_OR_SLEEPING_PILLS= st.radio(Constants.Q1G_SEDATIVES_OR_SLEEPING_PILLS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1G_SEDATIVES_OR_SLEEPING_PILLS)
Q1HA_HALLUCINOGEN = st.radio(Constants.Q1H_HALLUCINOGENS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1H_HALLUCINOGENS)
Q1IA_OPIOIDS =st.radio(Constants.Q1I_OPIOIDS,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1I_OPIOIDS)
Q1JA_OTHER_SPECIFY =st.radio(Constants.Q1J_OTHER_SPECIFY,Constants.YES_OR_NO_OPTIONS,key=Constants.Q1J_OTHER_SPECIFY)
if Q1JA_OTHER_SPECIFY == Constants.YES :
    Q1KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q1K_OTHER_SPECIFY_YES,key=Constants.Q1K_OTHER_SPECIFY_YES)    


IS_USER_SELECTED_YES_Q1_SECTION=all( a.lower() == "no" for a in [Q1AA_TOBACCO_PRODUCTS,Q1BA_ALCOHOLIC_PRODUCTS,Q1CA_CANNABIS,Q1DA_COCAINE,Q1EA_AMPHETAMINE_TYPE_STIMULANTS,Q1FA_INHALANTS,Q1GA_SEDATIVES_OR_SLEEPING_PILLS,Q1IA_OPIOIDS,Q1HA_HALLUCINOGEN,Q1JA_OTHER_SPECIFY])

if not IS_USER_SELECTED_YES_Q1_SECTION:
    st.subheader(Constants.Q2_PAST_THREE_MONTHS_SUBSTANCES_SUB_HEADER)
    Q2AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q2A_TOBACCO_PRODUCTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q2B_ALCOHOLIC_PRODUCTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2CA_CANNABIS = st.selectbox(Constants.Q2C_CANNABIS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2DA_COCAINE =st.selectbox(Constants.Q2D_COCAINE,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2EA_AMPHETAMINE_TYPE_STIMULANTS =st.selectbox(Constants.Q2E_AMPHETAMINE_TYPE_STIMULANTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2FA_INHALANTS =st.selectbox(Constants.Q2F_INHALANTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2GA_SEDATIVES_OR_SLEEPING_PILLS= st.selectbox(Constants.Q2G_SEDATIVES_OR_SLEEPING_PILLS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2HA_HALLUCINOGEN = st.selectbox(Constants.Q2H_HALLUCINOGENS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2IA_OPIOIDS =st.selectbox(Constants.Q2I_OPIOIDS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    Q2JA_OTHER_SPECIFY =st.selectbox(Constants.Q2J_OTHER_SPECIFY,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,format_func=lambda x:x[0])
    if Q2JA_OTHER_SPECIFY[1] != 0:
        Q2KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q2K_OTHER_SPECIFY_YES,key=Constants.Q2K_OTHER_SPECIFY_YES)       


    st.session_state[Constants.Q2A_TOBACCO_PRODUCTS] = Q2AA_TOBACCO_PRODUCTS[1]
    st.session_state[Constants.Q2B_ALCOHOLIC_PRODUCTS] = Q2BA_ALCOHOLIC_PRODUCTS[1]
    st.session_state[Constants.Q2C_CANNABIS] = Q2CA_CANNABIS[1]
    st.session_state[Constants.Q2D_COCAINE] = Q2DA_COCAINE[1]
    st.session_state[Constants.Q2E_AMPHETAMINE_TYPE_STIMULANTS] = Q2EA_AMPHETAMINE_TYPE_STIMULANTS[1]
    st.session_state[Constants.Q2F_INHALANTS] = Q2FA_INHALANTS[1]
    st.session_state[Constants.Q2G_SEDATIVES_OR_SLEEPING_PILLS] = Q2GA_SEDATIVES_OR_SLEEPING_PILLS[1]
    st.session_state[Constants.Q2H_HALLUCINOGENS] = Q2HA_HALLUCINOGEN[1]
    st.session_state[Constants.Q2I_OPIOIDS] = Q2IA_OPIOIDS[1]
    st.session_state[Constants.Q2J_OTHER_SPECIFY] = Q2JA_OTHER_SPECIFY[1]

    IS_USER_SELECTED_YES_Q2_SECTION = all(a[0] == 0 for a in
                                          [Q2AA_TOBACCO_PRODUCTS, Q2BA_ALCOHOLIC_PRODUCTS, Q2CA_CANNABIS, Q2DA_COCAINE,
                                           Q2EA_AMPHETAMINE_TYPE_STIMULANTS, Q2FA_INHALANTS,
                                           Q2GA_SEDATIVES_OR_SLEEPING_PILLS, Q2HA_HALLUCINOGEN,Q2IA_OPIOIDS, Q2JA_OTHER_SPECIFY])

    if not IS_USER_SELECTED_YES_Q2_SECTION:
        st.subheader(Constants.Q3_PAST_THREE_MONTHS_HOW_OFTEN_STRONG_DESIRE_SUBHEADER)
        Q3AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q3A_TOBACCO_PRODUCTS,
                                             Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                             
                                             format_func=lambda x: x[0])
        Q3BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q3B_ALCOHOLIC_PRODUCTS,
                                               Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                              
                                               format_func=lambda x: x[0],
                                               )
        Q3CA_CANNABIS = st.selectbox(Constants.Q3C_CANNABIS,
                                     Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                    
                                     format_func=lambda x: x[0])
        Q3DA_COCAINE = st.selectbox(Constants.Q3D_COCAINE,
                                    Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                    
                                    format_func=lambda x: x[0])
        Q3EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q3E_AMPHETAMINE_TYPE_STIMULANTS,
                                                        Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                                        
                                                        format_func=lambda x: x[0])
        Q3FA_INHALANTS = st.selectbox(Constants.Q3F_INHALANTS,
                                      Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                     
                                      format_func=lambda x: x[0])
        Q3GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q3G_SEDATIVES_OR_SLEEPING_PILLS,
                                                        Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                                        
                                                        format_func=lambda x: x[0])
        Q3HA_HALLUCINOGEN = st.selectbox(Constants.Q3H_HALLUCINOGENS,
                                         Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                         
                                         format_func=lambda x: x[0])
        Q3IA_OPIOIDS = st.selectbox(Constants.Q3I_OPIOIDS,
                                    Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                    
                                    format_func=lambda x: x[0])
        Q3JA_OTHER_SPECIFY = st.selectbox(Constants.Q3J_OTHER_SPECIFY,
                                          Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                         
                                          format_func=lambda x: x[0])
        if Q3JA_OTHER_SPECIFY[1] != 0 :
            Q3KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q3K_OTHER_SPECIFY_YES,key=Constants.Q3K_OTHER_SPECIFY_YES)            

        st.session_state[Constants.Q3A_TOBACCO_PRODUCTS] = Q3AA_TOBACCO_PRODUCTS[1]
        st.session_state[Constants.Q3B_ALCOHOLIC_PRODUCTS] = Q3BA_ALCOHOLIC_PRODUCTS[1]
        st.session_state[Constants.Q3C_CANNABIS] = Q3CA_CANNABIS[1]
        st.session_state[Constants.Q3D_COCAINE] = Q3DA_COCAINE[1]
        st.session_state[Constants.Q3E_AMPHETAMINE_TYPE_STIMULANTS] = Q3EA_AMPHETAMINE_TYPE_STIMULANTS[1]
        st.session_state[Constants.Q3F_INHALANTS] = Q3FA_INHALANTS[1]
        st.session_state[Constants.Q3G_SEDATIVES_OR_SLEEPING_PILLS] = Q3GA_SEDATIVES_OR_SLEEPING_PILLS[1]
        st.session_state[Constants.Q3H_HALLUCINOGENS] = Q3HA_HALLUCINOGEN[1]
        st.session_state[Constants.Q3I_OPIOIDS] = Q3IA_OPIOIDS[1]
        st.session_state[Constants.Q3J_OTHER_SPECIFY] = Q3JA_OTHER_SPECIFY[1]

        st.subheader(Constants.Q4_PAST_THREE_MONTHS_HOW_OFTEN_YOUR_USE)
        Q4AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q4A_TOBACCO_PRODUCTS,
                                             Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                            
                                             format_func=lambda x: x[0])
        Q4BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q4B_ALCOHOLIC_PRODUCTS,
                                               Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                               
                                               format_func=lambda x: x[0])
        Q4CA_CANNABIS = st.selectbox(Constants.Q4C_CANNABIS,
                                     Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                    
                                     format_func=lambda x: x[0])
        Q4DA_COCAINE = st.selectbox(Constants.Q4D_COCAINE,
                                    Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                    
                                    format_func=lambda x: x[0])
        Q4EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q4E_AMPHETAMINE_TYPE_STIMULANTS,
                                                        Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                                       
                                                        format_func=lambda x: x[0])
        Q4FA_INHALANTS = st.selectbox(Constants.Q4F_INHALANTS,
                                      Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                      
                                      format_func=lambda x: x[0])
        Q4GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q4G_SEDATIVES_OR_SLEEPING_PILLS,
                                                        Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                                        
                                                        format_func=lambda x: x[0])
        Q4HA_HALLUCINOGEN = st.selectbox(Constants.Q4H_HALLUCINOGENS,
                                         Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                        
                                         format_func=lambda x: x[0])
        Q4IA_OPIOIDS = st.selectbox(Constants.Q4I_OPIOIDS,
                                    Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                   
                                    format_func=lambda x: x[0])
        Q4JA_OTHER_SPECIFY = st.selectbox(Constants.Q4J_OTHER_SPECIFY,
                                          Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,                                          
                                          format_func=lambda x: x[0])

        if Q4JA_OTHER_SPECIFY[1] !=0 :
            Q4KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q4K_OTHER_SPECIFY_YES,key=Constants.Q4K_OTHER_SPECIFY_YES)
           

        st.session_state[Constants.Q4A_TOBACCO_PRODUCTS] = Q4AA_TOBACCO_PRODUCTS[1]
        st.session_state[Constants.Q4B_ALCOHOLIC_PRODUCTS] = Q4BA_ALCOHOLIC_PRODUCTS[1]
        st.session_state[Constants.Q4C_CANNABIS] = Q4CA_CANNABIS[1]
        st.session_state[Constants.Q4D_COCAINE] = Q4DA_COCAINE[1]
        st.session_state[Constants.Q4E_AMPHETAMINE_TYPE_STIMULANTS] = Q4EA_AMPHETAMINE_TYPE_STIMULANTS[1]
        st.session_state[Constants.Q4F_INHALANTS] = Q4FA_INHALANTS[1]
        st.session_state[Constants.Q4G_SEDATIVES_OR_SLEEPING_PILLS] = Q4GA_SEDATIVES_OR_SLEEPING_PILLS[1]
        st.session_state[Constants.Q4H_HALLUCINOGENS] = Q4HA_HALLUCINOGEN[1]
        st.session_state[Constants.Q4I_OPIOIDS] = Q4IA_OPIOIDS[1]
        st.session_state[Constants.Q4J_OTHER_SPECIFY] = Q4JA_OTHER_SPECIFY[1]

        st.subheader(Constants.Q5_PAST_THREE_MONTHS_HOW_OFTEN_YOUR_FAILED_TO_DO)
        # Q5AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q5A_TOBACCO_PRODUCTS,
        #                                  Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
        #                                  key="Q5A_TOBACCO_PRODUCTS", format_func=lambda x: x[0])
        Q5BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q5B_ALCOHOLIC_PRODUCTS,
                                           Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                            format_func=lambda x: x[0])
        Q5CA_CANNABIS = st.selectbox(Constants.Q5C_CANNABIS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                  format_func=lambda x: x[0])
        Q5DA_COCAINE = st.selectbox(Constants.Q5D_COCAINE, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                 format_func=lambda x: x[0])
        Q5EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q5E_AMPHETAMINE_TYPE_STIMULANTS,
                                                    Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                                     format_func=lambda x: x[0])
        Q5FA_INHALANTS = st.selectbox(Constants.Q5F_INHALANTS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                   format_func=lambda x: x[0])
        Q5GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q5G_SEDATIVES_OR_SLEEPING_PILLS,
                                                    Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                                     format_func=lambda x: x[0])
        Q5HA_HALLUCINOGEN = st.selectbox(Constants.Q5H_HALLUCINOGENS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                      format_func=lambda x: x[0])
        Q5IA_OPIOIDS = st.selectbox(Constants.Q5I_OPIOIDS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                format_func=lambda x: x[0])
        Q5JA_OTHER_SPECIFY = st.selectbox(Constants.Q5J_OTHER_SPECIFY, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                       format_func=lambda x: x[0])

        if Q5JA_OTHER_SPECIFY[1] !=0:
            Q5KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q5K_OTHER_SPECIFY_YES,key=Constants.Q5K_OTHER_SPECIFY_YES)
            

        # survey_data[Constants.Q5A_TOBACCO_PRODUCTS] = Q5AA_TOBACCO_PRODUCTS[1]
        st.session_state[Constants.Q5B_ALCOHOLIC_PRODUCTS] = Q5BA_ALCOHOLIC_PRODUCTS[1]
        st.session_state[Constants.Q5C_CANNABIS] = Q5CA_CANNABIS[1]
        st.session_state[Constants.Q5D_COCAINE] = Q5DA_COCAINE[1]
        st.session_state[Constants.Q5E_AMPHETAMINE_TYPE_STIMULANTS] = Q5EA_AMPHETAMINE_TYPE_STIMULANTS[1]
        st.session_state[Constants.Q5F_INHALANTS] = Q5FA_INHALANTS[1]
        st.session_state[Constants.Q5G_SEDATIVES_OR_SLEEPING_PILLS] = Q5GA_SEDATIVES_OR_SLEEPING_PILLS[1]
        st.session_state[Constants.Q5H_HALLUCINOGENS] = Q5HA_HALLUCINOGEN[1]
        st.session_state[Constants.Q5I_OPIOIDS] = Q5IA_OPIOIDS[1]
        st.session_state[Constants.Q5J_OTHER_SPECIFY] = Q5JA_OTHER_SPECIFY[1]

    st.subheader(Constants.Q6_HAS_A_FRIEND_OR_RELATIVE_CONCERN)
    Q6AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q6A_TOBACCO_PRODUCTS,
                                     Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                     format_func=lambda x: x[0])
    Q6BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q6B_ALCOHOLIC_PRODUCTS,
                                       Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                        format_func=lambda x: x[0])
    Q6CA_CANNABIS = st.selectbox(Constants.Q6C_CANNABIS, Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                              format_func=lambda x: x[0])
    Q6DA_COCAINE = st.selectbox(Constants.Q6D_COCAINE, Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                           format_func=lambda x: x[0])
    Q6EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q6E_AMPHETAMINE_TYPE_STIMULANTS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                                format_func=lambda x: x[0])
    Q6FA_INHALANTS = st.selectbox(Constants.Q6F_INHALANTS, Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                              format_func=lambda x: x[0])
    Q6GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q6G_SEDATIVES_OR_SLEEPING_PILLS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                               
                                                format_func=lambda x: x[0])
    Q6HA_HALLUCINOGEN = st.selectbox(Constants.Q6H_HALLUCINOGENS,
                                 Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                
                                 format_func=lambda x: x[0])
    Q6IA_OPIOIDS = st.selectbox(Constants.Q6I_OPIOIDS,
                            Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                            
                            format_func=lambda x: x[0])
    Q6JA_OTHER_SPECIFY = st.selectbox(Constants.Q6J_OTHER_SPECIFY,
                                  Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                  
                                  format_func=lambda x: x[0])
    if Q6JA_OTHER_SPECIFY [1] !=0 :
        Q6KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q6K_OTHER_SPECIFY_YES,key=Constants.Q6K_OTHER_SPECIFY_YES)
        

    st.session_state[Constants.Q6A_TOBACCO_PRODUCTS] = Q6AA_TOBACCO_PRODUCTS[1]
    st.session_state[Constants.Q6B_ALCOHOLIC_PRODUCTS] = Q6BA_ALCOHOLIC_PRODUCTS[1]
    st.session_state[Constants.Q6C_CANNABIS] = Q6CA_CANNABIS[1]
    st.session_state[Constants.Q6D_COCAINE] = Q6DA_COCAINE[1]
    st.session_state[Constants.Q6E_AMPHETAMINE_TYPE_STIMULANTS] = Q6EA_AMPHETAMINE_TYPE_STIMULANTS[1]
    st.session_state[Constants.Q6F_INHALANTS] = Q6FA_INHALANTS[1]
    st.session_state[Constants.Q6G_SEDATIVES_OR_SLEEPING_PILLS] = Q6GA_SEDATIVES_OR_SLEEPING_PILLS[1]
    st.session_state[Constants.Q6H_HALLUCINOGENS] = Q6HA_HALLUCINOGEN[1]
    st.session_state[Constants.Q6I_OPIOIDS] = Q6IA_OPIOIDS[1]
    st.session_state[Constants.Q6J_OTHER_SPECIFY] = Q6JA_OTHER_SPECIFY[1]

    st.subheader(Constants.Q7_HAS_EVER_TRIED_TO_CUT_DOWN_ON)
    Q7AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q7A_TOBACCO_PRODUCTS,
                                     Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                     
                                     format_func=lambda x: x[0])
    Q7BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q7B_ALCOHOLIC_PRODUCTS,
                                       Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,                                       
                                       format_func=lambda x: x[0])
    Q7CA_CANNABIS = st.selectbox(Constants.Q7C_CANNABIS,
                             Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,                             
                             format_func=lambda x: x[0])
    Q7DA_COCAINE = st.selectbox(Constants.Q7D_COCAINE,
                            Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,                            
                            format_func=lambda x: x[0])
    Q7EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q7E_AMPHETAMINE_TYPE_STIMULANTS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                                
                                                format_func=lambda x: x[0])
    Q7FA_INHALANTS = st.selectbox(Constants.Q7F_INHALANTS,
                              Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,                              
                              format_func=lambda x: x[0])
    Q7GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q7G_SEDATIVES_OR_SLEEPING_PILLS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,                                                
                                                format_func=lambda x: x[0])
    Q7HA_HALLUCINOGEN = st.selectbox(Constants.Q7H_HALLUCINOGENS,
                                 Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                 
                                 format_func=lambda x: x[0])
    Q7IA_OPIOIDS = st.selectbox(Constants.Q7I_OPIOIDS,
                            Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,                            
                            format_func=lambda x: x[0])
    Q7JA_OTHER_SPECIFY = st.selectbox(Constants.Q7J_OTHER_SPECIFY,
                                  Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,                                  
                                  format_func=lambda x: x[0])

    if Q7JA_OTHER_SPECIFY[1] !=0 :
            Q7KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q7K_OTHER_SPECIFY_YES,key=Constants.Q7K_OTHER_SPECIFY_YES)
           

    st.session_state[Constants.Q7A_TOBACCO_PRODUCTS] = Q7AA_TOBACCO_PRODUCTS[1]
    st.session_state[Constants.Q7B_ALCOHOLIC_PRODUCTS] = Q7BA_ALCOHOLIC_PRODUCTS[1]
    st.session_state[Constants.Q7C_CANNABIS] = Q7CA_CANNABIS[1]
    st.session_state[Constants.Q7D_COCAINE] = Q7DA_COCAINE[1]
    st.session_state[Constants.Q7E_AMPHETAMINE_TYPE_STIMULANTS] = Q7EA_AMPHETAMINE_TYPE_STIMULANTS[1]
    st.session_state[Constants.Q7F_INHALANTS] = Q7FA_INHALANTS[1]
    st.session_state[Constants.Q7G_SEDATIVES_OR_SLEEPING_PILLS] = Q7GA_SEDATIVES_OR_SLEEPING_PILLS[1]
    st.session_state[Constants.Q7H_HALLUCINOGENS] = Q7HA_HALLUCINOGEN[1]
    st.session_state[Constants.Q7I_OPIOIDS] = Q7IA_OPIOIDS[1]
    st.session_state[Constants.Q7J_OTHER_SPECIFY] = Q7JA_OTHER_SPECIFY[1]


Q8A_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION=st.selectbox(Constants.Q8_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION,Constants.OPTIONS_DRUG_BY_INJECTION,format_func= lambda x:x[0])
st.session_state[Constants.Q8_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION]=Q8A_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION[1]

A_LIST = [
          st.session_state.get(Constants.Q2A_TOBACCO_PRODUCTS,''),
           st.session_state.get(Constants.Q3A_TOBACCO_PRODUCTS,''),
          st.session_state.get(Constants.Q4A_TOBACCO_PRODUCTS,''),
           st.session_state.get(Constants.Q5A_TOBACCO_PRODUCTS,''),
          st.session_state.get(Constants.Q6A_TOBACCO_PRODUCTS,''),
          st.session_state.get(Constants.Q7A_TOBACCO_PRODUCTS,'')]
st.session_state[Constants.TOTAL_A_TOBACCO_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in A_LIST)

B_LIST = [st.session_state.get(Constants.Q2B_ALCOHOLIC_PRODUCTS,''),
          st.session_state.get(Constants.Q3B_ALCOHOLIC_PRODUCTS,''),
          st.session_state.get(Constants.Q4B_ALCOHOLIC_PRODUCTS,''),
         st.session_state.get(Constants.Q5B_ALCOHOLIC_PRODUCTS,''),
          st.session_state.get(Constants.Q6B_ALCOHOLIC_PRODUCTS,''),
          st.session_state.get(Constants.Q7B_ALCOHOLIC_PRODUCTS,'')
          ]
st.session_state[Constants.TOTAL_B_ALCOHOL_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in B_LIST)

C_LIST = [st.session_state.get(Constants.Q2C_CANNABIS,''),
          st.session_state.get(Constants.Q3C_CANNABIS,''),
          st.session_state.get(Constants.Q4C_CANNABIS,''),
         st.session_state.get(Constants.Q5C_CANNABIS,''),
          st.session_state.get(Constants.Q6C_CANNABIS,''),
          st.session_state.get(Constants.Q7C_CANNABIS,'')
          ]

st.session_state[Constants.TOTAL_C_CANNABIS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in C_LIST)


D_LIST = [st.session_state.get(Constants.Q2D_COCAINE,''),
          st.session_state.get(Constants.Q3D_COCAINE,''),
          st.session_state.get(Constants.Q4D_COCAINE,''),
          st.session_state.get(Constants.Q5D_COCAINE,''),
          st.session_state.get(Constants.Q6D_COCAINE,''),
          st.session_state.get(Constants.Q7D_COCAINE,'')
          ]

st.session_state[Constants.TOTAL_D_COCAINE_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in D_LIST)


E_LIST = [st.session_state.get(Constants.Q2E_AMPHETAMINE_TYPE_STIMULANTS,''),
          st.session_state.get(Constants.Q3E_AMPHETAMINE_TYPE_STIMULANTS,''),
          st.session_state.get(Constants.Q4E_AMPHETAMINE_TYPE_STIMULANTS,''),
          st.session_state.get(Constants.Q5E_AMPHETAMINE_TYPE_STIMULANTS,''),
          st.session_state.get(Constants.Q6E_AMPHETAMINE_TYPE_STIMULANTS,''),
          st.session_state.get(Constants.Q7E_AMPHETAMINE_TYPE_STIMULANTS,''),
          ]
st.session_state[TOTAL_E_AMPHETAMINES_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in E_LIST)

F_LIST = [st.session_state.get(Constants.Q2F_INHALANTS,''),
          st.session_state.get(Constants.Q3F_INHALANTS,''),
          st.session_state.get(Constants.Q4F_INHALANTS,''),
          st.session_state.get(Constants.Q5F_INHALANTS,''),
          st.session_state.get(Constants.Q6F_INHALANTS,''),
          st.session_state.get(Constants.Q7F_INHALANTS,''),
          ]

st.session_state[TOTAL_F_INHALANTS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in F_LIST)

G_LIST = [st.session_state.get(Constants.Q2G_SEDATIVES_OR_SLEEPING_PILLS,''),
         st.session_state.get(Constants.Q3G_SEDATIVES_OR_SLEEPING_PILLS,''),
         st.session_state.get(Constants.Q4G_SEDATIVES_OR_SLEEPING_PILLS,''),
          st.session_state.get(Constants.Q5G_SEDATIVES_OR_SLEEPING_PILLS,''),
         st.session_state.get(Constants.Q6G_SEDATIVES_OR_SLEEPING_PILLS,''),
          st.session_state.get(Constants.Q7G_SEDATIVES_OR_SLEEPING_PILLS,'')
          ]

st.session_state[Constants.TOTAL_G_SEDATIVES_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in G_LIST)


H_LIST = [st.session_state.get(Constants.Q2H_HALLUCINOGENS,''),
          st.session_state.get(Constants.Q3H_HALLUCINOGENS,''),
          st.session_state.get(Constants.Q4H_HALLUCINOGENS,''),
          st.session_state.get(Constants.Q5H_HALLUCINOGENS,''),
          st.session_state.get(Constants.Q6H_HALLUCINOGENS,''),
          st.session_state.get(Constants.Q7H_HALLUCINOGENS,''),
          ]

st.session_state[Constants.TOTAL_H_HALLUCINOGENS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in H_LIST)

I_LIST = [st.session_state.get(Constants.Q2I_OPIOIDS,''),
          st.session_state.get(Constants.Q3I_OPIOIDS,''),
          st.session_state.get(Constants.Q4I_OPIOIDS,''),
          st.session_state.get(Constants.Q5I_OPIOIDS,''),
          st.session_state.get(Constants.Q6I_OPIOIDS,''),
          st.session_state.get(Constants.Q7I_OPIOIDS,''),
          ]

st.session_state[Constants.TOTAL_I_OPIOIDS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in I_LIST)

J_LIST = [st.session_state.get(Constants.Q2J_OTHER_SPECIFY,''),
          st.session_state.get(Constants.Q3J_OTHER_SPECIFY,''),
          st.session_state.get(Constants.Q4J_OTHER_SPECIFY,''),
          st.session_state.get(Constants.Q5J_OTHER_SPECIFY,''),
          st.session_state.get(Constants.Q6J_OTHER_SPECIFY,''),
          st.session_state.get(Constants.Q7J_OTHER_SPECIFY,''),
          ]

st.session_state[Constants.TOTAL_J_OTHER_DRUGS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in J_LIST)

st.session_state[Constants.A_TOBACCO_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_A_TOBACCO_SCORE],0,4,27)
st.session_state[Constants.B_ALCOHOL_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_B_ALCOHOL_SCORE],0,11,27)
st.session_state[Constants.C_CANNABIS_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_C_CANNABIS_SCORE],0,4,27)
st.session_state[Constants.D_COCAINE_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_D_COCAINE_SCORE],0,4,27)
st.session_state[Constants.E_AMPHETAMINES_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_E_AMPHETAMINES_SCORE],0,4,27)
st.session_state[Constants.F_INHALANTS_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_F_INHALANTS_SCORE],0,4,27)
st.session_state[Constants.G_SEDATIVES_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_G_SEDATIVES_SCORE],0,4,27)
st.session_state[Constants.H_HALLUCINOGENS_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_H_HALLUCINOGENS_SCORE],0,4,27)
st.session_state[Constants.I_OPIOIDS_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_I_OPIOIDS_SCORE],0,4,27)
st.session_state[Constants.J_OTHER_INTERVENTION_TYPE] = find_intervention_type(st.session_state[Constants.TOTAL_J_OTHER_DRUGS_SCORE],0,4,27)


############################# GAD-7 Anxiety SECTION - START #####################################
st.header(Constants.GAD_7_ANXIETY_HEADER)
# st.info(Constants.GAD_7_ANXIETY_OPTIONS_INFO)
a_gad_feeling_nerv = st.selectbox(Constants.Q_FEELING_NERVOUS,Constants.GAD_7_ANXIETY_OPTIONS,format_func= lambda x : x[0])
a_gad_not_being_able = st.selectbox(Constants.Q_NOT_ABLE_STOP_WORRY,Constants.GAD_7_ANXIETY_OPTIONS,format_func= lambda x : x[0])
a_gad_worrying_too_much = st.selectbox(Constants.Q_GAD_WORRYING_TOO_MUCH,Constants.GAD_7_ANXIETY_OPTIONS,format_func= lambda x : x[0])
a_gad_trouble_relaxing = st.selectbox(Constants.Q_GAD_TROUBLE_RELAXING,Constants.GAD_7_ANXIETY_OPTIONS,format_func= lambda x : x[0])
a_gad_being_so_restless = st.selectbox(Constants.Q_GAD_BEING_SO_RESTLESS,Constants.GAD_7_ANXIETY_OPTIONS,format_func= lambda x : x[0])
a_gad_becoming_easily_annoyed = st.selectbox(Q_GAD_BECOMING_EASILY_ANNOYED,Constants.GAD_7_ANXIETY_OPTIONS,format_func= lambda x : x[0])
a_gad_feeling_afraid = st.selectbox(Q_GAD_FEELING_AFRAID,Constants.GAD_7_ANXIETY_OPTIONS,format_func= lambda x : x[0])

st.session_state[Constants.Q_FEELING_NERVOUS]=a_gad_feeling_nerv[1]
st.session_state[Constants.Q_NOT_ABLE_STOP_WORRY]=a_gad_not_being_able[1]
st.session_state[Constants.Q_GAD_WORRYING_TOO_MUCH]=a_gad_worrying_too_much[1]
st.session_state[Constants.Q_GAD_TROUBLE_RELAXING]=a_gad_trouble_relaxing[1]
st.session_state[Constants.Q_GAD_BEING_SO_RESTLESS]=a_gad_being_so_restless[1]
st.session_state[Constants.Q_GAD_BECOMING_EASILY_ANNOYED]=a_gad_becoming_easily_annoyed[1]
st.session_state[Constants.Q_GAD_FEELING_AFRAID]=a_gad_feeling_afraid[1]

total_gad_score = a_gad_feeling_nerv[1] + a_gad_not_being_able[1] + a_gad_worrying_too_much[1] + a_gad_trouble_relaxing[1] + a_gad_being_so_restless[1] + a_gad_becoming_easily_annoyed[1] + a_gad_feeling_afraid[1]
st.session_state[Constants.Q_TOTAL_GAD_SCORE] = total_gad_score

############################# Patient Health Questionnaire -9 (PHQ-9) - START #####################################
st.header(Constants.PHQ_HEADER)
st.info(Constants.PHQ_OPTIONS_INFO)
a_PHQ_little_interest= st.selectbox(Constants.Q_PHQ_LITTLE_INTEREST, Constants.PHQ_OPTIONS,format_func= lambda  x : x[0])
a_PHQ_feeling_down =st.selectbox(Constants.Q_PHQ_FEELING_DOWN, Constants.PHQ_OPTIONS ,format_func= lambda  x : x[0] )
a_PHQ_trouble_falling = st.selectbox(Constants.Q_PHQ_TROUBLE_FALLING, Constants.PHQ_OPTIONS , format_func= lambda  x : x[0])
a_PHQ_feeling_tired = st.selectbox(Constants.Q_PHQ_FEELING_TIRED, Constants.PHQ_OPTIONS , format_func= lambda  x : x[0])
a_PHQ_poor_appetite=st.selectbox(Constants.Q_PHQ_POOR_APPETITE, Constants.PHQ_OPTIONS , format_func= lambda  x : x[0])
a_PHQ_feeling_bad_about_ur_self=st.selectbox(Constants.Q_PHQ_FEELING_BAD_ABOUT_UR_SELF,  Constants.PHQ_OPTIONS , format_func= lambda  x : x[0])
a_PHQ_trouble_concentration = st.selectbox(Constants.Q_PHQ_TROUBLE_CONCENTRATION,  Constants.PHQ_OPTIONS , format_func= lambda  x : x[0])
a_PHQ_moving_or_speaking_so_slow = st.selectbox(Constants.Q_PHQ_MOVING_OR_SPEAKING_SO_SLOW,  Constants.PHQ_OPTIONS , format_func= lambda  x : x[0])
a_PHQ_thoughts_that=st.selectbox(Constants.Q_PHQ_THOUGHTS_THAT,  Constants.PHQ_OPTIONS , format_func= lambda  x : x[0])

#adding PHQ RELATED ANSWERS TO 'survey_data'
st.session_state[Constants.Q_PHQ_LITTLE_INTEREST]=a_PHQ_little_interest[1]
st.session_state[Constants.Q_PHQ_FEELING_DOWN]=a_PHQ_feeling_down[1]
st.session_state[Constants.Q_PHQ_TROUBLE_FALLING]=a_PHQ_trouble_falling[1]
st.session_state[Constants.Q_PHQ_FEELING_TIRED]=a_PHQ_feeling_tired[1]
st.session_state[Constants.Q_PHQ_POOR_APPETITE]=a_PHQ_poor_appetite[1]
st.session_state[Constants.Q_PHQ_FEELING_BAD_ABOUT_UR_SELF]=a_PHQ_feeling_bad_about_ur_self[1]
st.session_state[Constants.Q_PHQ_TROUBLE_CONCENTRATION]=a_PHQ_trouble_concentration[1]
st.session_state[Constants.Q_PHQ_MOVING_OR_SPEAKING_SO_SLOW]=a_PHQ_moving_or_speaking_so_slow[1]
st.session_state[Constants.Q_PHQ_THOUGHTS_THAT]=a_PHQ_thoughts_that[1]

total_PHQ_score = a_PHQ_little_interest[1] + a_PHQ_feeling_down[1] + a_PHQ_trouble_falling[1] + a_PHQ_feeling_tired[1] + a_PHQ_poor_appetite[1] + a_PHQ_feeling_bad_about_ur_self[1] + a_PHQ_trouble_concentration[1] + a_PHQ_moving_or_speaking_so_slow[1]+a_PHQ_thoughts_that[1]
st.session_state[Constants.Q_TOTAL_PHQ_SCORE] = total_PHQ_score

# Submit button
if st.button("Submit"):
    default_headers = list(SURVE_DEFAULTS.keys())
    
    headers = sheet.row_values(1)
    if not headers:
        sheet.append_row((default_headers))
        headers = default_headers
    
    row =[]
    for state_key, column_name in SURVE_DEFAULTS.items():
        row.append(st.session_state.get(state_key,""))
    sheet.append_row(row)
    
    for state_key in SURVE_DEFAULTS.keys():
       st.session_state.pop(state_key,None)

    st.toast("✅ Response submitted! Thank you.")
    st.rerun()

# # Optional: view all responses (for admin)
# if st.checkbox("Show all responses"):
#     if os.path.exists("responses.csv"):
#         st.dataframe(pd.read_csv("responses.csv"))
#     else:
#         st.warning("No responses yet.")

# st.download_button(
#     label="Download CSV",
#     data="",
#     file_name="data.csv",
#     mime="text/csv",
#     icon=":material/download:",
# )



