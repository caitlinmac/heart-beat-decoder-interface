import streamlit as st
import requests
#from streamlit_lottie import st_lottie

'''
# heartbeatDECODER
## your AI-powered heart health partner
'''
# ## AI Clinician to analyze your ECG results machine learning model to classify ECG results


'''
Welcome to **heartbeatDECODER**!

The heartbeatDECODER tool allows you  to quickly and easily identify irregular heart beat patterns from a single or double lead ECG measurement!

heartbeatDECODER uses advanced machine learning algorithms to analyze complex ECG signal traces and extract meaningful information. It is compatible with 1 or 2-lead ECG - so you can use the sensor of a smartwatch or a simplified clinical device.

With heartbeatDECODER, you have access to clinician-level diagnostic precision on your own terms.

Identify early signs of heart abnormalities and cardiovascular disease so you can act fast and improve your health outcomes!
'''


st.markdown('''
## First, please record or upload your ecg results and indicate their format:
''')

# input_columns = st.columns(2)
st.button("Upload ECG results")
st.button("Analyze my results")

# Animation
#st_lottie('https://lottiefiles.com/animations/ecg-nFJKmPyH46?from=search')


# Call API to run model on input data
url = 'http://127.0.0.1:8000/predict'


# test values for api
_0preRR = 163
_0postRR = 165
_0pPeak = 0.069610222
_0tPeak = -0.083280601
_0rPeak = 0.614133158
_0sPeak = -0.392761319
_0qPeak = 0.047159284
_0qrsinterval = 15
_0pqinterval = 2
_0qtinterval = 27
_0stinterval = 10
_0qrsmorph0 = 0.047159284
_0qrsmorph1 = 0.146934163
_0qrsmorph2 = 0.506484864
_0qrsmorph3 = 0.550094976
_0qrsmorph4 = -0.05303844
_1preRR = 163
_1postRR = 165
_1pPeak = -0.013397687
_1tPeak = 0.204003068
_1rPeak = 0.123921531
_1sPeak = -0.421341864
_1qPeak = -0.023370488
_1qrsinterval = 14
_1pqinterval= 3
_1qtinterval = 23
_1stinterval = 6
_1qrsmorph0 = -0.02337048
_1qrsmorph1 = -0.01165031
_1qrsmorph2 = 0.082607626
_1qrsmorph3 = 0.101372903
_1qrsmorph4 = -0.18338685

params = {'_0preRR': _0preRR,
'_0postRR': _0postRR,
'_0pPeak': _0pPeak,
'_0tPeak': _0tPeak,
'_0rPeak': _0rPeak,
'_0sPeak':_0sPeak,
'_0qPeak': _0qPeak,
'_0qrsinterval': _0qrsinterval,
'_0pqinterval': _0pqinterval,
'_0qtinterval': _0qtinterval,
'_0stinterval': _0stinterval,
'_0qrsmorph0': _0qrsmorph0,
'_0qrsmorph1': _0qrsmorph1,
'_0qrsmorph2': _0qrsmorph2,
'_0qrsmorph3': _0qrsmorph3,
'_0qrsmorph4': _0qrsmorph4,
'_1preRR': _1preRR,
'_1postRR': _1postRR,
'_1pPeak': _1pPeak,
'_1tPeak': _1tPeak,
'_1rPeak': _1rPeak,
'_1sPeak': _1sPeak,
'_1qPeak': _1qPeak,
'_1qrsinterval': _1qrsinterval,
'_1pqinterval': _1pqinterval,
'_1qtinterval': _1qtinterval,
'_1stinterval': _1stinterval,
'_1qrsmorph0': _1qrsmorph0,
'_1qrsmorph1': _1qrsmorph1,
'_1qrsmorph2': _1qrsmorph2,
'_1qrsmorph3': _1qrsmorph3,
'_1qrsmorph4': _1qrsmorph4
}



# response = requests.get(url, params=params)

# Output results
st.markdown('''
## The results are in...
''')
# st.write(f"{response.json()}")

# from david:
"""params ={}
_0preRR = '0_pre-RR',
_0postRR = '0_post-RR',
_0pPeak = '0_pPeak',
_0tPeak = '0_tPeak',
_0rPeak = '0_rPeak',
_0sPeak = '0_sPeak',
_0qPeak = '0_qPeak',
_0qrsinterval = '0_qrs_interval',
_0pqinterval = '0_pq_interval',
_0qtinterval = '0_qt_interval',
_0stinterval = '0_st_interval',
_0qrsmorph0 = '0_qrs_morph0',
_0qrsmorph1 = '0_qrs_morph1',
_0qrsmorph2 = '0_qrs_morph2',
_0qrsmorph3 = '0_qrs_morph3',
_0qrsmorph4 = '0_qrs_morph4',
_1preRR = '1_pre-RR',
_1postRR = '1_post-RR',
_1pPeak = '1_pPeak',
_1tPeak = '1_tPeak',
_1rPeak = '1_rPeak',
_1sPeak = '1_sPeak',
_1qPeak ='1_qPeak',
_1qrsinterval = '1_qrs_interval',
_1pqinterval = '1_pq_interval',
_1qtinterval = '1_qt_interval',
_1stinterval = '1_st_interval',
_1qrsmorph0 = '1_qrs_morph0',
_1qrsmorph1 = '1_qrs_morph1',
_1qrsmorph2 = '1_qrs_morph2',
_1qrsmorph3 = '1_qrs_morph3',
_1qrsmorph4 = '1_qrs_morph4'
}"""


# params with default values
"""params_og = {'0_pre-RR': 163 ,
          '0_post-RR': 165 ,
          '0_pPeak': 0.069610222,
          '0_tPeak': -0.083280601,
          '0_rPeak': 0.614133158,
          '0_sPeak': -0.392761319,
          '0_qPeak': 0.047159284,
          '0_qrs_interval': 15,
          '0_pq_interval': 2,
          '0_qt_interval': 27,
          '0_st_interval': 10,
          '0_qrs_morph0': 0.047159284,
          '0_qrs_morph1': 0.146934163,
          '0_qrs_morph2': 0.506484864,
          '0_qrs_morph3': 0.550094976,
          '0_qrs_morph4': -0.053038448,
          '1_pre-RR': 163,
          '1_post-RR': 165,
          '1_pPeak': -0.013397687,
          '1_tPeak': 0.204003068,
          '1_rPeak': 0.123921531,
          '1_sPeak': -0.421341864,
          '1_qPeak': -0.023370488,
          '1_qrs_interval': 14,
          '1_pq_interval': 3,
          '1_qt_interval': 23,
          '1_st_interval': 6,
          '1_qrs_morph0': -0.023370488,
          '1_qrs_morph1': -0.01165031,
          '1_qrs_morph2': 0.082607626,
          '1_qrs_morph3': 0.101372903,
          '1_qrs_morph4': -0.183386854}"""
