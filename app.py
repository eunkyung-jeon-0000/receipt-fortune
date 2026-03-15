import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. AI Studio API 설정
genai.configure(api_key="AIzaSyBQ3TeJLt6yXo9nIYf9NhY9xUzFWtYVs3k")
model = genai.GenerativeModel('gemini-1.5-flash') # 영수증 사진 분석용

# 2. 화면 구성
st.set_page_config(page_title="영수증 점성술", page_icon="🔮")
st.title("🔮 영수증 점성술사")
st.write("오늘 당신이 쓴 영수증 속 '기운'을 분석해 드립니다.")

# 3. 파일 업로드
uploaded_file = st.file_uploader("영수증 사진을 찍거나 업로드하세요", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='분석 중인 영수증...', use_column_width=True)
    
    with st.spinner('영수증 귀신이 강림하는 중...'):
        # AI에게 보낼 엉뚱한 프롬프트
        prompt = """
        이 영수증 사진을 보고 다음 내용을 작성해줘. 
        매우 신비롭고 엉뚱하며 '킹받는' 말투로 해줘.
        1. 영수증의 기운: (예: 텅장으로 가는 급행열차의 기운)
        2. 전생의 흔적: (품목 하나를 골라 전생과 연결)
        3. 오늘의 예언: (말도 안 되는 미래 예측)
        4. 행운의 아이템: (주변의 엉뚱한 물건 추천)
        """
        
        # AI 분석 실행
        response = model.generate_content([prompt, image])
        
        st.success("점괘가 나왔습니다!")
        st.markdown(response.text)

# 하단 재미 요소
st.divider()
st.caption("주의: 이 점괘를 믿을 시 잔액이 부족해질 수 있습니다.")
