import streamlit as st
from datetime import datetime
import pandas as pd

# 세션 상태 초기화
if 'data' not in st.session_state:
    st.session_state['data'] = {}

# 앱 제목 및 설명
st.title("캘린더 및 시간표 & 감정 기록 앱")
st.write("날짜를 선택하세요:")

# 날짜 입력
selected_date = st.date_input("날짜 선택")

if selected_date:
    selected_date_str = selected_date.strftime("%Y-%m-%d")
    st.subheader(f"{selected_date_str} 기록")

    # 시간표 입력
    st.write("시간표를 입력하세요:")
    start_time = st.time_input("시작 시간", datetime.now().time())
    end_time = st.time_input("종료 시간", datetime.now().time())
    activity = st.text_input("활동 내용")

    # 시간표 추가 버튼
    if st.button("시간표 추가"):
        if selected_date_str not in st.session_state['data']:
            st.session_state['data'][selected_date_str] = {'schedule': [], 'emotions': []}
        st.session_state['data'][selected_date_str]['schedule'].append({'start_time': start_time, 'end_time': end_time, 'activity': activity})
        st.success("시간표가 추가되었습니다.")

    # 저장된 시간표 표시
    if selected_date_str in st.session_state['data'] and st.session_state['data'][selected_date_str]['schedule']:
        st.write("시간표:")
        df_schedule = pd.DataFrame(st.session_state['data'][selected_date_str]['schedule'])
        st.table(df_schedule)

    # 감정 선택
    st.write("오늘의 감정을 선택하세요:")
    emotions = ['😊', '😢', '😡', '😴', '😍', '😐']
    selected_emotion = st.selectbox("감정 선택", emotions)

    # 감정 추가 버튼
    if st.button("감정 추가"):
        if selected_date_str not in st.session_state['data']:
            st.session_state['data'][selected_date_str] = {'schedule': [], 'emotions': []}
        st.session_state['data'][selected_date_str]['emotions'].append(selected_emotion)
        st.success("감정이 추가되었습니다.")

    # 저장된 감정 표시
    if selected_date_str in st.session_state['data'] and st.session_state['data'][selected_date_str]['emotions']:
        st.write("오늘의 감정:")
        st.write(" ".join(st.session_state['data'][selected_date_str]['emotions']))
