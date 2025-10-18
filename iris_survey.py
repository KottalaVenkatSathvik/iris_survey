import streamlit as st
import pandas as pd
import os

def find_intervention_type(value, low,mid,high):
    return Constants.NO_INTERVENTION if low <= value < mid else Constants.RECEIVE_BRIEF_INTERVENTION if mid <=value<high else Constants.MORE_INTENSIVE_TREATMENT

import Constants
from Constants import Q_GAD_BECOMING_EASILY_ANNOYED, Q_GAD_FEELING_AFRAID, TOTAL_E_AMPHETAMINES_SCORE, \
    TOTAL_F_INHALANTS_SCORE, TOTAL_G_SEDATIVES_SCORE
from survey_data_schema import survey_data


############################# APP TITLE #####################################
st.markdown(f"<h1 style='text-align: center;color: #096f7a'>{Constants.APP_TITTLE}</h1>", unsafe_allow_html=True)
############################# DEMOGRAPHIC SECTION - START #####################################
# Collect answers
st.header(Constants.DEMOGRAPHIC_DETAILS_SUBHEADER)
name = st.text_input(Constants.Q_PATIENT_NAME)
age = st.number_input(Constants.Q_AGE, min_value=0, max_value=150)
location = st.text_input(Constants.Q_LOCATION)
occupation = st.text_input(Constants.Q_OCCUPATION)
education = st.text_input(Constants.Q_EDUCATION)

survey_data[Constants.Q_PATIENT_NAME] = name
survey_data[Constants.Q_AGE] = age
survey_data[Constants.Q_OCCUPATION] = occupation
survey_data[Constants.Q_EDUCATION] = education

st.subheader(Constants.PAST_MEDICAL_HISTORY_SUB_HEADER)

allergies = st.radio(Constants.Q_ALLERGIES,Constants.YES_OR_NO_OPTIONS)
survey_data[Constants.Q_ALLERGIES] = allergies

if allergies == Constants.YES:
    allergies_details= st.text_input(Constants.Q_ALLERGIES_DETAILS)
    survey_data[Constants.Q_ALLERGIES_DETAILS] = allergies_details

surgical_procedures = st.radio(Constants.Q_SURGICAL_HIST,Constants.YES_OR_NO_OPTIONS)
survey_data[Constants.Q_SURGICAL_HIST] = surgical_procedures
if surgical_procedures == Constants.YES:
    surgical_procedures_details = st.text_input(Constants.Q_SURGICAL_PROCEDURE_DETAILS)
    survey_data[Constants.Q_SURGICAL_PROCEDURE_DETAILS] =surgical_procedures_details

a_bp = st.radio(Constants.Q_HYPER_TENSION_BP,Constants.YES_OR_NO_OPTIONS)
a_diabetes_mellitus = st.radio(Constants.Q_DIABETES_MELLITUS,Constants.YES_OR_NO_OPTIONS)
a_hyper_thyroid = st.radio(Constants.Q_HYPER_THYROID,Constants.YES_OR_NO_OPTIONS)
a_hypo_thyroid = st.radio(Constants.Q_HYPO_THYROID,Constants.YES_OR_NO_OPTIONS)
a_copd = st.radio(Constants.Q_COPD,Constants.YES_OR_NO_OPTIONS)
a_peptic_ulcer_disease = st.radio(Constants.Q_PEPTIC_ULCER_DISEASE,Constants.YES_OR_NO_OPTIONS)
a_OTHER = st.text_input(Constants.Q_OTHER_MEDICAL_HIST)

survey_data[Constants.Q_HYPER_TENSION_BP] =a_bp
survey_data[Constants.Q_DIABETES_MELLITUS] =a_diabetes_mellitus
survey_data[Constants.Q_HYPER_THYROID] =a_hyper_thyroid
survey_data[Constants.Q_HYPO_THYROID] =a_hypo_thyroid
survey_data[Constants.Q_COPD] =a_copd
survey_data[Constants.Q_PEPTIC_ULCER_DISEASE] =a_peptic_ulcer_disease
survey_data[Constants.Q_OTHER_MEDICAL_HIST] =a_OTHER

st.subheader(Constants.SOCIAL_HISTORY_SUB_HEADER)
substance_used = st.radio(Constants.Q_SUBSTANCES_USE,Constants.YES_OR_NO_OPTIONS)
if substance_used == Constants.YES:
    substances_details = st.text_input(Constants.Q_IS_SUBSTANCES_USED_YES)
    survey_data[Constants.Q_IS_SUBSTANCES_USED_YES] = substances_details
smoking = st.radio(Constants.Q_SMOKING, Constants.YES_OR_NO_OPTIONS)
alcohol = st.radio(Constants.Q_ALCOHOL, Constants.YES_OR_NO_OPTIONS)
if alcohol == Constants.YES:
    alcohol_details = st.text_input(Constants.Q_ALCOHOL_DETAILS)
    survey_data[Constants.Q_ALCOHOL_DETAILS] = alcohol_details
# other_social_history = st.text_input(Constants.Q_OTHER_SOCIAL_HISTORY)
diet = st.radio(Constants.Q_DIET, Constants.DIET_OPTIONS)
physical_activity = st.radio(Constants.Q_PHYSICAL_ACTIVITY, Constants.YES_OR_NO_OPTIONS)

survey_data[Constants.Q_SUBSTANCES_USE]=substance_used
survey_data[Constants.Q_SMOKING]=smoking
survey_data[Constants.Q_ALCOHOL]=alcohol
survey_data[Constants.Q_DIET]=diet
survey_data[Constants.Q_PHYSICAL_ACTIVITY]=physical_activity

if physical_activity==Constants.YES:
    physical_activity_details = st.text_input(Constants.Q_IS_PHYSICAL_ACTIVITY_YES)
    survey_data[Constants.Q_IS_PHYSICAL_ACTIVITY_YES]=physical_activity_details

marital_status = st.radio(Constants.Q_MARITAL_STS, Constants.MARITAL_STATUS_OPTIONS)
num_of_children = st.number_input(Constants.Q_NUMBER_OF_CHILDREN,min_value=0)

survey_data[Constants.Q_MARITAL_STS]=marital_status
survey_data[Constants.Q_NUMBER_OF_CHILDREN]=num_of_children

st.subheader(Constants.Q_PAST_3_MONTHS_PREVALENCE)
any_prescription_medications = st.radio(Constants.Q_PRESCRIPTION_MEDI,Constants.YES_OR_NO_OPTIONS)
if any_prescription_medications == Constants.YES:
    prescription_medications_details = st.text_input(Constants.Q_PRESCRIPTION_MEDI_DETAILS)
    prescription_medications_duration = st.selectbox(Constants.Q_PRESCRIPTION_MEDI_DURATION,Constants.OPTIONS_MEDICATIONS_DURATION,format_func=lambda x: x[0])
    survey_data[Constants.Q_PRESCRIPTION_MEDI_DETAILS] = prescription_medications_details
    survey_data[Constants.Q_PRESCRIPTION_MEDI_DURATION] = prescription_medications_duration

any_non_prescription_medications = st.radio(Constants.Q_NON_PRESCRIPTION_MEDI,Constants.YES_OR_NO_OPTIONS)
if any_non_prescription_medications == Constants.YES:
    non_prescription_medications_details = st.text_input(Constants.Q_NON_PRESCRIPTION_MEDI_DETAILS)
    non_prescription_medications_duration = st.selectbox(Constants.Q_NON_PRESCRIPTION_MEDI_DURATION,Constants.OPTIONS_MEDICATIONS_DURATION,format_func=lambda x: x[0])
    survey_data[Constants.Q_NON_PRESCRIPTION_MEDI_DETAILS] = non_prescription_medications_details
    survey_data[Constants.Q_OTC_MEDI_DURATION] = non_prescription_medications_duration

any_otc_medications = st.radio(Constants.Q_OTC_MEDI,Constants.YES_OR_NO_OPTIONS)
if any_otc_medications == Constants.YES:
    otc_medications_details = st.text_input(Constants.Q_OTC_MEDI_DETAILS)
    otc_medications_duration = st.selectbox(Constants.Q_OTC_MEDI_DURATION,Constants.OPTIONS_MEDICATIONS_DURATION,format_func=lambda x: x[0])
    survey_data[Constants.Q_OTC_MEDI_DETAILS] = otc_medications_details
    survey_data[Constants.Q_OTC_MEDI_DURATION] = otc_medications_duration

survey_data[Constants.Q_PRESCRIPTION_MEDI]=any_prescription_medications
survey_data[Constants.Q_NON_PRESCRIPTION_MEDI]=any_non_prescription_medications
survey_data[Constants.Q_OTC_MEDI]=any_otc_medications

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

survey_data[Constants.Q_FEELING_NERVOUS]=a_gad_feeling_nerv[1]
survey_data[Constants.Q_NOT_ABLE_STOP_WORRY]=a_gad_not_being_able[1]
survey_data[Constants.Q_GAD_WORRYING_TOO_MUCH]=a_gad_worrying_too_much[1]
survey_data[Constants.Q_GAD_TROUBLE_RELAXING]=a_gad_trouble_relaxing[1]
survey_data[Constants.Q_GAD_BEING_SO_RESTLESS]=a_gad_being_so_restless[1]
survey_data[Constants.Q_GAD_BECOMING_EASILY_ANNOYED]=a_gad_becoming_easily_annoyed[1]
survey_data[Constants.Q_GAD_FEELING_AFRAID]=a_gad_feeling_afraid[1]

total_gad_score = a_gad_feeling_nerv[1] + a_gad_not_being_able[1] + a_gad_worrying_too_much[1] + a_gad_trouble_relaxing[1] + a_gad_being_so_restless[1] + a_gad_becoming_easily_annoyed[1] + a_gad_feeling_afraid[1]
survey_data['TOTAL_GAD_SCORE'] = total_gad_score


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
survey_data[Constants.Q_PHQ_LITTLE_INTEREST]=a_PHQ_little_interest[1]
survey_data[Constants.Q_PHQ_FEELING_DOWN]=a_PHQ_feeling_down[1]
survey_data[Constants.Q_PHQ_TROUBLE_FALLING]=a_PHQ_trouble_falling[1]
survey_data[Constants.Q_PHQ_FEELING_TIRED]=a_PHQ_feeling_tired[1]
survey_data[Constants.Q_PHQ_POOR_APPETITE]=a_PHQ_poor_appetite[1]
survey_data[Constants.Q_PHQ_FEELING_BAD_ABOUT_UR_SELF]=a_PHQ_feeling_bad_about_ur_self[1]
survey_data[Constants.Q_PHQ_TROUBLE_CONCENTRATION]=a_PHQ_trouble_concentration[1]
survey_data[Constants.Q_PHQ_MOVING_OR_SPEAKING_SO_SLOW]=a_PHQ_moving_or_speaking_so_slow[1]
survey_data[Constants.Q_PHQ_THOUGHTS_THAT]=a_PHQ_thoughts_that[1]



############################# ASSIST V3.1 - START #####################################
st.header(Constants.ASSIST_V3_HEADER)
st.subheader(Constants.Q1_IN_LIFE_SUBSTANCES_USED_HEADER)

Q1AA_TOBACCO_PRODUCTS = st.radio(Constants.Q1A_TOBACCO_PRODUCTS,Constants.YES_OR_NO_OPTIONS,key="Q1A_TOBACCO_PRODUCTS")
Q1BA_ALCOHOLIC_PRODUCTS = st.radio(Constants.Q1B_ALCOHOLIC_PRODUCTS,Constants.YES_OR_NO_OPTIONS,key="Q1B_ALCOHOLIC_PRODUCTS")
Q1CA_CANNABIS = st.radio(Constants.Q1C_CANNABIS,Constants.YES_OR_NO_OPTIONS,key="Q1C_CANNABIS")
Q1DA_COCAINE =st.radio(Constants.Q1D_COCAINE,Constants.YES_OR_NO_OPTIONS,key="Q1D_COCAINE")
Q1EA_AMPHETAMINE_TYPE_STIMULANTS =st.radio(Constants.Q1E_AMPHETAMINE_TYPE_STIMULANTS,Constants.YES_OR_NO_OPTIONS,key="Q1E_AMPHETAMINE_TYPE_STIMULANTS")
Q1FA_INHALANTS =st.radio(Constants.Q1F_INHALANTS,Constants.YES_OR_NO_OPTIONS,key="Q1F_INHALANTS")
Q1GA_SEDATIVES_OR_SLEEPING_PILLS= st.radio(Constants.Q1G_SEDATIVES_OR_SLEEPING_PILLS,Constants.YES_OR_NO_OPTIONS,key="Q1G_SEDATIVES_OR_SLEEPING_PILLS")
Q1HA_HALLUCINOGEN = st.radio(Constants.Q1H_HALLUCINOGENS,Constants.YES_OR_NO_OPTIONS,key="Q1H_HALLUCINOGENS")
Q1IA_OPIOIDS =st.radio(Constants.Q1I_OPIOIDS,Constants.YES_OR_NO_OPTIONS,key="Q1I_OPIOIDS")
Q1JA_OTHER_SPECIFY =st.radio(Constants.Q1J_OTHER_SPECIFY,Constants.YES_OR_NO_OPTIONS,key="Q1J_OTHER_SPECIFY")
if Q1JA_OTHER_SPECIFY == Constants.YES :
    Q1KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q1K_OTHER_SPECIFY_YES,key="Q1K_OTHER_SPECIFY_YES")
    survey_data[Constants.Q1K_OTHER_SPECIFY_YES] = Q1KA_TEXT_OTHER_SPECIFY

survey_data[Constants.Q1A_TOBACCO_PRODUCTS]=Q1AA_TOBACCO_PRODUCTS
survey_data[Constants.Q1B_ALCOHOLIC_PRODUCTS]=Q1BA_ALCOHOLIC_PRODUCTS
survey_data[Constants.Q1C_CANNABIS]=Q1CA_CANNABIS
survey_data[Constants.Q1D_COCAINE]=Q1DA_COCAINE
survey_data[Constants.Q1E_AMPHETAMINE_TYPE_STIMULANTS]=Q1EA_AMPHETAMINE_TYPE_STIMULANTS
survey_data[Constants.Q1F_INHALANTS]=Q1FA_INHALANTS
survey_data[Constants.Q1G_SEDATIVES_OR_SLEEPING_PILLS]=Q1GA_SEDATIVES_OR_SLEEPING_PILLS
survey_data[Constants.Q1H_HALLUCINOGENS]=Q1HA_HALLUCINOGEN
survey_data[Constants.Q1I_OPIOIDS]=Q1IA_OPIOIDS
survey_data[Constants.Q1J_OTHER_SPECIFY]=Q1JA_OTHER_SPECIFY

IS_USER_SELECTED_YES_Q1_SECTION=all( a.lower() == "no" for a in [Q1AA_TOBACCO_PRODUCTS,Q1BA_ALCOHOLIC_PRODUCTS,Q1CA_CANNABIS,Q1DA_COCAINE,Q1EA_AMPHETAMINE_TYPE_STIMULANTS,Q1FA_INHALANTS,Q1GA_SEDATIVES_OR_SLEEPING_PILLS,Q1IA_OPIOIDS,Q1HA_HALLUCINOGEN,Q1JA_OTHER_SPECIFY])

if not IS_USER_SELECTED_YES_Q1_SECTION:
    st.subheader(Constants.Q2_PAST_THREE_MONTHS_SUBSTANCES_SUB_HEADER)
    Q2AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q2A_TOBACCO_PRODUCTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2A_TOBACCO_PRODUCTS",format_func=lambda x:x[0])
    Q2BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q2B_ALCOHOLIC_PRODUCTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2B_ALCOHOLIC_PRODUCTS",format_func=lambda x:x[0])
    Q2CA_CANNABIS = st.selectbox(Constants.Q2C_CANNABIS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2C_CANNABIS",format_func=lambda x:x[0])
    Q2DA_COCAINE =st.selectbox(Constants.Q2D_COCAINE,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2D_COCAINE",format_func=lambda x:x[0])
    Q2EA_AMPHETAMINE_TYPE_STIMULANTS =st.selectbox(Constants.Q2E_AMPHETAMINE_TYPE_STIMULANTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2E_AMPHETAMINE_TYPE_STIMULANTS",format_func=lambda x:x[0])
    Q2FA_INHALANTS =st.selectbox(Constants.Q2F_INHALANTS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2F_INHALANTS",format_func=lambda x:x[0])
    Q2GA_SEDATIVES_OR_SLEEPING_PILLS= st.selectbox(Constants.Q2G_SEDATIVES_OR_SLEEPING_PILLS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2G_SEDATIVES_OR_SLEEPING_PILLS",format_func=lambda x:x[0])
    Q2HA_HALLUCINOGEN = st.selectbox(Constants.Q2H_HALLUCINOGENS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2H_HALLUCINOGENS",format_func=lambda x:x[0])
    Q2IA_OPIOIDS =st.selectbox(Constants.Q2I_OPIOIDS,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2I_OPIOIDS",format_func=lambda x:x[0])
    Q2JA_OTHER_SPECIFY =st.selectbox(Constants.Q2J_OTHER_SPECIFY,Constants.OPTIONS_Q2_OFTEN_SUBSTANCES,key="Q2J_OTHER_SPECIFY",format_func=lambda x:x[0])
    if Q2JA_OTHER_SPECIFY[1] != 0:
        Q2KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q2K_OTHER_SPECIFY_YES,key="Q2K_OTHER_SPECIFY_YES")
        survey_data[Constants.Q2K_OTHER_SPECIFY_YES] = Q2KA_TEXT_OTHER_SPECIFY



    survey_data[Constants.Q2A_TOBACCO_PRODUCTS] = Q2AA_TOBACCO_PRODUCTS[1]
    survey_data[Constants.Q2B_ALCOHOLIC_PRODUCTS] = Q2BA_ALCOHOLIC_PRODUCTS[1]
    survey_data[Constants.Q2C_CANNABIS] = Q2CA_CANNABIS[1]
    survey_data[Constants.Q2D_COCAINE] = Q2DA_COCAINE[1]
    survey_data[Constants.Q2E_AMPHETAMINE_TYPE_STIMULANTS] = Q2EA_AMPHETAMINE_TYPE_STIMULANTS[1]
    survey_data[Constants.Q2F_INHALANTS] = Q2FA_INHALANTS[1]
    survey_data[Constants.Q2G_SEDATIVES_OR_SLEEPING_PILLS] = Q2GA_SEDATIVES_OR_SLEEPING_PILLS[1]
    survey_data[Constants.Q2H_HALLUCINOGENS] = Q2HA_HALLUCINOGEN[1]
    survey_data[Constants.Q2I_OPIOIDS] = Q2IA_OPIOIDS[1]
    survey_data[Constants.Q2J_OTHER_SPECIFY] = Q2JA_OTHER_SPECIFY[1]

    IS_USER_SELECTED_YES_Q2_SECTION = all(a[0] == 0 for a in
                                          [Q2AA_TOBACCO_PRODUCTS, Q2BA_ALCOHOLIC_PRODUCTS, Q2CA_CANNABIS, Q2DA_COCAINE,
                                           Q2EA_AMPHETAMINE_TYPE_STIMULANTS, Q2FA_INHALANTS,
                                           Q2GA_SEDATIVES_OR_SLEEPING_PILLS, Q2HA_HALLUCINOGEN, Q2JA_OTHER_SPECIFY])

    if not IS_USER_SELECTED_YES_Q2_SECTION:
        st.subheader(Constants.Q3_PAST_THREE_MONTHS_HOW_OFTEN_STRONG_DESIRE_SUBHEADER)
        Q3AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q3A_TOBACCO_PRODUCTS,
                                             Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                             key="Q3A_TOBACCO_PRODUCTS",
                                             format_func=lambda x: x[0])
        Q3BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q3B_ALCOHOLIC_PRODUCTS,
                                               Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                               key="Q3B_ALCOHOLIC_PRODUCTS",
                                               format_func=lambda x: x[0],
                                               )
        Q3CA_CANNABIS = st.selectbox(Constants.Q3C_CANNABIS,
                                     Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                     key="Q3C_CANNABIS",
                                     format_func=lambda x: x[0])
        Q3DA_COCAINE = st.selectbox(Constants.Q3D_COCAINE,
                                    Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                    key="Q3D_COCAINE",
                                    format_func=lambda x: x[0])
        Q3EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q3E_AMPHETAMINE_TYPE_STIMULANTS,
                                                        Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                                        key="Q3E_AMPHETAMINE_TYPE_STIMULANTS",
                                                        format_func=lambda x: x[0])
        Q3FA_INHALANTS = st.selectbox(Constants.Q3F_INHALANTS,
                                      Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                      key="Q3F_INHALANTS",
                                      format_func=lambda x: x[0])
        Q3GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q3G_SEDATIVES_OR_SLEEPING_PILLS,
                                                        Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                                        key="Q3G_SEDATIVES_OR_SLEEPING_PILLS",
                                                        format_func=lambda x: x[0])
        Q3HA_HALLUCINOGEN = st.selectbox(Constants.Q3H_HALLUCINOGENS,
                                         Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                         key="Q3H_HALLUCINOGENS",
                                         format_func=lambda x: x[0])
        Q3IA_OPIOIDS = st.selectbox(Constants.Q3I_OPIOIDS,
                                    Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                    key="Q3I_OPIOIDS",
                                    format_func=lambda x: x[0])
        Q3JA_OTHER_SPECIFY = st.selectbox(Constants.Q3J_OTHER_SPECIFY,
                                          Constants.OPTIONS_Q3_OFTEN_SUBSTANCES,
                                          key="Q3J_OTHER_SPECIFY",
                                          format_func=lambda x: x[0])
        if Q3JA_OTHER_SPECIFY[1] != 0 :
            Q3KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q3K_OTHER_SPECIFY_YES,key="Q3K_OTHER_SPECIFY_YES")
            survey_data[Constants.Q3K_OTHER_SPECIFY_YES] = Q3KA_TEXT_OTHER_SPECIFY

        survey_data[Constants.Q3A_TOBACCO_PRODUCTS] = Q3AA_TOBACCO_PRODUCTS[1]
        survey_data[Constants.Q3B_ALCOHOLIC_PRODUCTS] = Q3BA_ALCOHOLIC_PRODUCTS[1]
        survey_data[Constants.Q3C_CANNABIS] = Q3CA_CANNABIS[1]
        survey_data[Constants.Q3D_COCAINE] = Q3DA_COCAINE[1]
        survey_data[Constants.Q3E_AMPHETAMINE_TYPE_STIMULANTS] = Q3EA_AMPHETAMINE_TYPE_STIMULANTS[1]
        survey_data[Constants.Q3F_INHALANTS] = Q3FA_INHALANTS[1]
        survey_data[Constants.Q3G_SEDATIVES_OR_SLEEPING_PILLS] = Q3GA_SEDATIVES_OR_SLEEPING_PILLS[1]
        survey_data[Constants.Q3H_HALLUCINOGENS] = Q3HA_HALLUCINOGEN[1]
        survey_data[Constants.Q3I_OPIOIDS] = Q3IA_OPIOIDS[1]
        survey_data[Constants.Q3J_OTHER_SPECIFY] = Q3JA_OTHER_SPECIFY[1]

        st.subheader(Constants.Q4_PAST_THREE_MONTHS_HOW_OFTEN_YOUR_USE)
        Q4AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q4A_TOBACCO_PRODUCTS,
                                             Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                             key="Q4A_TOBACCO_PRODUCTS",
                                             format_func=lambda x: x[0])
        Q4BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q4B_ALCOHOLIC_PRODUCTS,
                                               Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                               key="Q4B_ALCOHOLIC_PRODUCTS",
                                               format_func=lambda x: x[0])
        Q4CA_CANNABIS = st.selectbox(Constants.Q4C_CANNABIS,
                                     Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                     key="Q4C_CANNABIS",
                                     format_func=lambda x: x[0])
        Q4DA_COCAINE = st.selectbox(Constants.Q4D_COCAINE,
                                    Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                    key="Q4D_COCAINE",
                                    format_func=lambda x: x[0])
        Q4EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q4E_AMPHETAMINE_TYPE_STIMULANTS,
                                                        Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                                        key="Q4E_AMPHETAMINE_TYPE_STIMULANTS",
                                                        format_func=lambda x: x[0])
        Q4FA_INHALANTS = st.selectbox(Constants.Q4F_INHALANTS,
                                      Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                      key="Q4F_INHALANTS",
                                      format_func=lambda x: x[0])
        Q4GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q4G_SEDATIVES_OR_SLEEPING_PILLS,
                                                        Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                                        key="Q4G_SEDATIVES_OR_SLEEPING_PILLS",
                                                        format_func=lambda x: x[0])
        Q4HA_HALLUCINOGEN = st.selectbox(Constants.Q4H_HALLUCINOGENS,
                                         Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                         key="Q4H_HALLUCINOGENS",
                                         format_func=lambda x: x[0])
        Q4IA_OPIOIDS = st.selectbox(Constants.Q4I_OPIOIDS,
                                    Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                    key="Q4I_OPIOIDS",
                                    format_func=lambda x: x[0])
        Q4JA_OTHER_SPECIFY = st.selectbox(Constants.Q4J_OTHER_SPECIFY,
                                          Constants.OPTIONS_Q4_OFTEN_SUBSTANCES,
                                          key="Q4J_OTHER_SPECIFY",
                                          format_func=lambda x: x[0])

        if Q4JA_OTHER_SPECIFY[1] !=0 :
            Q4KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q4K_OTHER_SPECIFY_YES,key="Q4K_OTHER_SPECIFY_YES")
            survey_data[Constants.Q4K_OTHER_SPECIFY_YES] = Q4KA_TEXT_OTHER_SPECIFY

        survey_data[Constants.Q4A_TOBACCO_PRODUCTS] = Q4AA_TOBACCO_PRODUCTS[1]
        survey_data[Constants.Q4B_ALCOHOLIC_PRODUCTS] = Q4BA_ALCOHOLIC_PRODUCTS[1]
        survey_data[Constants.Q4C_CANNABIS] = Q4CA_CANNABIS[1]
        survey_data[Constants.Q4D_COCAINE] = Q4DA_COCAINE[1]
        survey_data[Constants.Q4E_AMPHETAMINE_TYPE_STIMULANTS] = Q4EA_AMPHETAMINE_TYPE_STIMULANTS[1]
        survey_data[Constants.Q4F_INHALANTS] = Q4FA_INHALANTS[1]
        survey_data[Constants.Q4G_SEDATIVES_OR_SLEEPING_PILLS] = Q4GA_SEDATIVES_OR_SLEEPING_PILLS[1]
        survey_data[Constants.Q4H_HALLUCINOGENS] = Q4HA_HALLUCINOGEN[1]
        survey_data[Constants.Q4I_OPIOIDS] = Q4IA_OPIOIDS[1]
        survey_data[Constants.Q4J_OTHER_SPECIFY] = Q4JA_OTHER_SPECIFY[1]

        st.subheader(Constants.Q5_PAST_THREE_MONTHS_HOW_OFTEN_YOUR_FAILED_TO_DO)
        # Q5AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q5A_TOBACCO_PRODUCTS,
        #                                  Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
        #                                  key="Q5A_TOBACCO_PRODUCTS", format_func=lambda x: x[0])
        Q5BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q5B_ALCOHOLIC_PRODUCTS,
                                           Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                           key="Q5B_ALCOHOLIC_PRODUCTS", format_func=lambda x: x[0])
        Q5CA_CANNABIS = st.selectbox(Constants.Q5C_CANNABIS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                 key="Q5C_CANNABIS", format_func=lambda x: x[0])
        Q5DA_COCAINE = st.selectbox(Constants.Q5D_COCAINE, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                key="Q5D_COCAINE", format_func=lambda x: x[0])
        Q5EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q5E_AMPHETAMINE_TYPE_STIMULANTS,
                                                    Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                                    key="Q5E_AMPHETAMINE_TYPE_STIMULANTS", format_func=lambda x: x[0])
        Q5FA_INHALANTS = st.selectbox(Constants.Q5F_INHALANTS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                  key="Q5F_INHALANTS", format_func=lambda x: x[0])
        Q5GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q5G_SEDATIVES_OR_SLEEPING_PILLS,
                                                    Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                                    key="Q5G_SEDATIVES_OR_SLEEPING_PILLS", format_func=lambda x: x[0])
        Q5HA_HALLUCINOGEN = st.selectbox(Constants.Q5H_HALLUCINOGENS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                     key="Q5H_HALLUCINOGENS", format_func=lambda x: x[0])
        Q5IA_OPIOIDS = st.selectbox(Constants.Q5I_OPIOIDS, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                key="Q5I_OPIOIDS", format_func=lambda x: x[0])
        Q5JA_OTHER_SPECIFY = st.selectbox(Constants.Q5J_OTHER_SPECIFY, Constants.OPTIONS_Q5_OFTEN_SUBSTANCES,
                                      key="Q5J_OTHER_SPECIFY", format_func=lambda x: x[0])

        if Q5JA_OTHER_SPECIFY[1] !=0:
            Q5KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q5K_OTHER_SPECIFY_YES,key="Q5K_OTHER_SPECIFY_YES")
            survey_data[Constants.Q5K_OTHER_SPECIFY_YES] = Q5KA_TEXT_OTHER_SPECIFY

        # survey_data[Constants.Q5A_TOBACCO_PRODUCTS] = Q5AA_TOBACCO_PRODUCTS[1]
        survey_data[Constants.Q5B_ALCOHOLIC_PRODUCTS] = Q5BA_ALCOHOLIC_PRODUCTS[1]
        survey_data[Constants.Q5C_CANNABIS] = Q5CA_CANNABIS[1]
        survey_data[Constants.Q5D_COCAINE] = Q5DA_COCAINE[1]
        survey_data[Constants.Q5E_AMPHETAMINE_TYPE_STIMULANTS] = Q5EA_AMPHETAMINE_TYPE_STIMULANTS[1]
        survey_data[Constants.Q5F_INHALANTS] = Q5FA_INHALANTS[1]
        survey_data[Constants.Q5G_SEDATIVES_OR_SLEEPING_PILLS] = Q5GA_SEDATIVES_OR_SLEEPING_PILLS[1]
        survey_data[Constants.Q5H_HALLUCINOGENS] = Q5HA_HALLUCINOGEN[1]
        survey_data[Constants.Q5I_OPIOIDS] = Q5IA_OPIOIDS[1]
        survey_data[Constants.Q5J_OTHER_SPECIFY] = Q5JA_OTHER_SPECIFY[1]

    st.subheader(Constants.Q6_HAS_A_FRIEND_OR_RELATIVE_CONCERN)
    Q6AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q6A_TOBACCO_PRODUCTS,
                                     Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                     key="Q6A_TOBACCO_PRODUCTS", format_func=lambda x: x[0])
    Q6BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q6B_ALCOHOLIC_PRODUCTS,
                                       Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                       key="Q6B_ALCOHOLIC_PRODUCTS", format_func=lambda x: x[0])
    Q6CA_CANNABIS = st.selectbox(Constants.Q6C_CANNABIS, Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                             key="Q6C_CANNABIS", format_func=lambda x: x[0])
    Q6DA_COCAINE = st.selectbox(Constants.Q6D_COCAINE, Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                            key="Q6D_COCAINE", format_func=lambda x: x[0])
    Q6EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q6E_AMPHETAMINE_TYPE_STIMULANTS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                                key="Q6E_AMPHETAMINE_TYPE_STIMULANTS", format_func=lambda x: x[0])
    Q6FA_INHALANTS = st.selectbox(Constants.Q6F_INHALANTS, Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                              key="Q6F_INHALANTS", format_func=lambda x: x[0])
    Q6GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q6G_SEDATIVES_OR_SLEEPING_PILLS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                                key="Q6G_SEDATIVES_OR_SLEEPING_PILLS",
                                                format_func=lambda x: x[0])
    Q6HA_HALLUCINOGEN = st.selectbox(Constants.Q6H_HALLUCINOGENS,
                                 Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                 key="Q6H_HALLUCINOGENS",
                                 format_func=lambda x: x[0])
    Q6IA_OPIOIDS = st.selectbox(Constants.Q6I_OPIOIDS,
                            Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                            key="Q6I_OPIOIDS",
                            format_func=lambda x: x[0])
    Q6JA_OTHER_SPECIFY = st.selectbox(Constants.Q6J_OTHER_SPECIFY,
                                  Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                  key="Q6J_OTHER_SPECIFY",
                                  format_func=lambda x: x[0])
    if Q6JA_OTHER_SPECIFY [1] !=0 :
        Q6KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q6K_OTHER_SPECIFY_YES,key="Q6K_OTHER_SPECIFY_YES")
        survey_data[Constants.Q6K_OTHER_SPECIFY_YES] = Q6KA_TEXT_OTHER_SPECIFY

    survey_data[Constants.Q6A_TOBACCO_PRODUCTS] = Q6AA_TOBACCO_PRODUCTS[1]
    survey_data[Constants.Q6B_ALCOHOLIC_PRODUCTS] = Q6BA_ALCOHOLIC_PRODUCTS[1]
    survey_data[Constants.Q6C_CANNABIS] = Q6CA_CANNABIS[1]
    survey_data[Constants.Q6D_COCAINE] = Q6DA_COCAINE[1]
    survey_data[Constants.Q6E_AMPHETAMINE_TYPE_STIMULANTS] = Q6EA_AMPHETAMINE_TYPE_STIMULANTS[1]
    survey_data[Constants.Q6F_INHALANTS] = Q6FA_INHALANTS[1]
    survey_data[Constants.Q6G_SEDATIVES_OR_SLEEPING_PILLS] = Q6GA_SEDATIVES_OR_SLEEPING_PILLS[1]
    survey_data[Constants.Q6H_HALLUCINOGENS] = Q6HA_HALLUCINOGEN[1]
    survey_data[Constants.Q6I_OPIOIDS] = Q6IA_OPIOIDS[1]
    survey_data[Constants.Q6J_OTHER_SPECIFY] = Q6JA_OTHER_SPECIFY[1]

    st.subheader(Constants.Q7_HAS_EVER_TRIED_TO_CUT_DOWN_ON)
    Q7AA_TOBACCO_PRODUCTS = st.selectbox(Constants.Q7A_TOBACCO_PRODUCTS,
                                     Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                     key="Q7A_TOBACCO_PRODUCTS",
                                     format_func=lambda x: x[0])
    Q7BA_ALCOHOLIC_PRODUCTS = st.selectbox(Constants.Q7B_ALCOHOLIC_PRODUCTS,
                                       Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                       key="Q7B_ALCOHOLIC_PRODUCTS",
                                       format_func=lambda x: x[0])
    Q7CA_CANNABIS = st.selectbox(Constants.Q7C_CANNABIS,
                             Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                             key="Q7C_CANNABIS",
                             format_func=lambda x: x[0])
    Q7DA_COCAINE = st.selectbox(Constants.Q7D_COCAINE,
                            Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                            key="Q7D_COCAINE",
                            format_func=lambda x: x[0])
    Q7EA_AMPHETAMINE_TYPE_STIMULANTS = st.selectbox(Constants.Q7E_AMPHETAMINE_TYPE_STIMULANTS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                                key="Q7E_AMPHETAMINE_TYPE_STIMULANTS",
                                                format_func=lambda x: x[0])
    Q7FA_INHALANTS = st.selectbox(Constants.Q7F_INHALANTS,
                              Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                              key="Q7F_INHALANTS",
                              format_func=lambda x: x[0])
    Q7GA_SEDATIVES_OR_SLEEPING_PILLS = st.selectbox(Constants.Q7G_SEDATIVES_OR_SLEEPING_PILLS,
                                                Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                                key="Q7G_SEDATIVES_OR_SLEEPING_PILLS",
                                                format_func=lambda x: x[0])
    Q7HA_HALLUCINOGEN = st.selectbox(Constants.Q7H_HALLUCINOGENS,
                                 Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                 key="Q7H_HALLUCINOGENS",
                                 format_func=lambda x: x[0])
    Q7IA_OPIOIDS = st.selectbox(Constants.Q7I_OPIOIDS,
                            Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                            key="Q7I_OPIOIDS",
                            format_func=lambda x: x[0])
    Q7JA_OTHER_SPECIFY = st.selectbox(Constants.Q7J_OTHER_SPECIFY,
                                  Constants.OPTIONS_Q6_and_Q7_OFTEN_SUBSTANCES,
                                  key="Q7J_OTHER_SPECIFY",
                                  format_func=lambda x: x[0])

    if Q7JA_OTHER_SPECIFY[1] !=0 :
            Q7KA_TEXT_OTHER_SPECIFY = st.text_input(Constants.Q7K_OTHER_SPECIFY_YES,key="Q7K_OTHER_SPECIFY_YES")
            survey_data[Constants.Q7K_OTHER_SPECIFY_YES] = Q7KA_TEXT_OTHER_SPECIFY

    survey_data[Constants.Q7A_TOBACCO_PRODUCTS] = Q7AA_TOBACCO_PRODUCTS[1]
    survey_data[Constants.Q7B_ALCOHOLIC_PRODUCTS] = Q7BA_ALCOHOLIC_PRODUCTS[1]
    survey_data[Constants.Q7C_CANNABIS] = Q7CA_CANNABIS[1]
    survey_data[Constants.Q7D_COCAINE] = Q7DA_COCAINE[1]
    survey_data[Constants.Q7E_AMPHETAMINE_TYPE_STIMULANTS] = Q7EA_AMPHETAMINE_TYPE_STIMULANTS[1]
    survey_data[Constants.Q7F_INHALANTS] = Q7FA_INHALANTS[1]
    survey_data[Constants.Q7G_SEDATIVES_OR_SLEEPING_PILLS] = Q7GA_SEDATIVES_OR_SLEEPING_PILLS[1]
    survey_data[Constants.Q7H_HALLUCINOGENS] = Q7HA_HALLUCINOGEN[1]
    survey_data[Constants.Q7I_OPIOIDS] = Q7IA_OPIOIDS[1]
    survey_data[Constants.Q7J_OTHER_SPECIFY] = Q7JA_OTHER_SPECIFY[1]


Q8A_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION=st.selectbox(Constants.Q8_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION,Constants.OPTIONS_DRUG_BY_INJECTION,format_func= lambda x:x[0])
survey_data[Constants.Q8_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION]=Q8A_HAVE_YOU_EVER_USED_ANY_DRUG_BY_INJECTION[1]

A_LIST = [
          survey_data[Constants.Q2A_TOBACCO_PRODUCTS],
          survey_data[Constants.Q3A_TOBACCO_PRODUCTS],
          survey_data[Constants.Q4A_TOBACCO_PRODUCTS],
          survey_data[Constants.Q5A_TOBACCO_PRODUCTS],
          survey_data[Constants.Q6A_TOBACCO_PRODUCTS],
          survey_data[Constants.Q7A_TOBACCO_PRODUCTS]]
survey_data[Constants.TOTAL_A_TOBACCO_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in A_LIST)

B_LIST = [survey_data[Constants.Q2B_ALCOHOLIC_PRODUCTS],
          survey_data[Constants.Q3B_ALCOHOLIC_PRODUCTS],
          survey_data[Constants.Q4B_ALCOHOLIC_PRODUCTS],
          survey_data[Constants.Q5B_ALCOHOLIC_PRODUCTS],
          survey_data[Constants.Q6B_ALCOHOLIC_PRODUCTS],
          survey_data[Constants.Q7B_ALCOHOLIC_PRODUCTS],
          ]
survey_data[Constants.TOTAL_B_ALCOHOL_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in B_LIST)

C_LIST = [survey_data[Constants.Q2C_CANNABIS],
          survey_data[Constants.Q3C_CANNABIS],
          survey_data[Constants.Q4C_CANNABIS],
          survey_data[Constants.Q5C_CANNABIS],
          survey_data[Constants.Q6C_CANNABIS],
          survey_data[Constants.Q7C_CANNABIS],
          ]

survey_data[Constants.TOTAL_C_CANNABIS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in C_LIST)


D_LIST = [survey_data[Constants.Q2D_COCAINE],
          survey_data[Constants.Q3D_COCAINE],
          survey_data[Constants.Q4D_COCAINE],
          survey_data[Constants.Q5D_COCAINE],
          survey_data[Constants.Q6D_COCAINE],
          survey_data[Constants.Q7D_COCAINE],
          ]

survey_data[Constants.TOTAL_D_COCAINE_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in D_LIST)


E_LIST = [survey_data[Constants.Q2E_AMPHETAMINE_TYPE_STIMULANTS],
          survey_data[Constants.Q3E_AMPHETAMINE_TYPE_STIMULANTS],
          survey_data[Constants.Q4E_AMPHETAMINE_TYPE_STIMULANTS],
          survey_data[Constants.Q5E_AMPHETAMINE_TYPE_STIMULANTS],
          survey_data[Constants.Q6E_AMPHETAMINE_TYPE_STIMULANTS],
          survey_data[Constants.Q7E_AMPHETAMINE_TYPE_STIMULANTS],
          ]
survey_data[TOTAL_E_AMPHETAMINES_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in E_LIST)

F_LIST = [survey_data[Constants.Q2F_INHALANTS],
          survey_data[Constants.Q3F_INHALANTS],
          survey_data[Constants.Q4F_INHALANTS],
          survey_data[Constants.Q5F_INHALANTS],
          survey_data[Constants.Q6F_INHALANTS],
          survey_data[Constants.Q7F_INHALANTS],
          ]

survey_data[TOTAL_F_INHALANTS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in F_LIST)

G_LIST = [survey_data[Constants.Q2G_SEDATIVES_OR_SLEEPING_PILLS],
          survey_data[Constants.Q3G_SEDATIVES_OR_SLEEPING_PILLS],
          survey_data[Constants.Q4G_SEDATIVES_OR_SLEEPING_PILLS],
          survey_data[Constants.Q5G_SEDATIVES_OR_SLEEPING_PILLS],
          survey_data[Constants.Q6G_SEDATIVES_OR_SLEEPING_PILLS],
          survey_data[Constants.Q7G_SEDATIVES_OR_SLEEPING_PILLS],
          ]

survey_data[Constants.TOTAL_G_SEDATIVES_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in G_LIST)


H_LIST = [survey_data[Constants.Q2H_HALLUCINOGENS],
          survey_data[Constants.Q3H_HALLUCINOGENS],
          survey_data[Constants.Q4H_HALLUCINOGENS],
          survey_data[Constants.Q5H_HALLUCINOGENS],
          survey_data[Constants.Q6H_HALLUCINOGENS],
          survey_data[Constants.Q7H_HALLUCINOGENS],
          ]

survey_data[Constants.TOTAL_H_HALLUCINOGENS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in H_LIST)

I_LIST = [survey_data[Constants.Q2I_OPIOIDS],
          survey_data[Constants.Q3I_OPIOIDS],
          survey_data[Constants.Q4I_OPIOIDS],
          survey_data[Constants.Q5I_OPIOIDS],
          survey_data[Constants.Q6I_OPIOIDS],
          survey_data[Constants.Q7I_OPIOIDS],
          ]

survey_data[Constants.TOTAL_I_OPIOIDS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in I_LIST)

J_LIST = [survey_data[Constants.Q2J_OTHER_SPECIFY],
          survey_data[Constants.Q3J_OTHER_SPECIFY],
          survey_data[Constants.Q4J_OTHER_SPECIFY],
          survey_data[Constants.Q5J_OTHER_SPECIFY],
          survey_data[Constants.Q6J_OTHER_SPECIFY],
          survey_data[Constants.Q7J_OTHER_SPECIFY],
          ]

survey_data[Constants.TOTAL_J_OTHER_DRUGS_SCORE] = sum(0 if (x =='' or x is None)  else int(x) for x in J_LIST)

survey_data[Constants.A_TOBACCO_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_A_TOBACCO_SCORE],0,4,27)
survey_data[Constants.B_ALCOHOL_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_B_ALCOHOL_SCORE],0,11,27)
survey_data[Constants.C_CANNABIS_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_C_CANNABIS_SCORE],0,4,27)
survey_data[Constants.D_COCAINE_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_D_COCAINE_SCORE],0,4,27)
survey_data[Constants.E_AMPHETAMINES_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_E_AMPHETAMINES_SCORE],0,4,27)
survey_data[Constants.F_INHALANTS_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_F_INHALANTS_SCORE],0,4,27)
survey_data[Constants.G_SEDATIVES_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_G_SEDATIVES_SCORE],0,4,27)
survey_data[Constants.H_HALLUCINOGENS_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_H_HALLUCINOGENS_SCORE],0,4,27)
survey_data[Constants.I_OPIOIDS_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_I_OPIOIDS_SCORE],0,4,27)
survey_data[Constants.J_OTHER_INTERVENTION_TYPE] = find_intervention_type(survey_data[Constants.TOTAL_J_OTHER_DRUGS_SCORE],0,4,27)

# Submit button
if st.button("Submit"):
    # Save responses to CSV file
    file = "responses.csv"
    df = pd.DataFrame([survey_data])

    if os.path.exists(file):
        df.to_csv(file, mode="a", header=False, index=False)
    else:
        df.to_csv(file, index=False)

    st.toast("✅ Response submitted! Thank you.")

# Optional: view all responses (for admin)
if st.checkbox("Show all responses"):
    if os.path.exists("responses.csv"):
        st.dataframe(pd.read_csv("responses.csv"))
    else:
        st.warning("No responses yet.")

# st.download_button(
#     label="Download CSV",
#     data="",
#     file_name="data.csv",
#     mime="text/csv",
#     icon=":material/download:",
# )



