import datetime

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np





def test1():
    # 기업 데이터를 딕셔너리로 생성 (22개 기업 예시)
    # companies_data = {
    #     "기업명": ["기업 1", "기업 2", "기업 3", "기업 4", "기업 5", "기업 6", "기업 7", "기업 8", "기업 9", "기업 10",
    #             "기업 11", "기업 12", "기업 13", "기업 14", "기업 15", "기업 16", "기업 17", "기업 18", "기업 19", "기업 20",
    #             "기업 21", "기업 22"],
    #     "도달": [1200000, 890000, 2340000, 1900000, 1550000, 920000, 3500000, 2100000, 1700000, 1200000,
    #            2900000, 1600000, 1000000, 3100000, 1400000, 3200000, 2500000, 2700000, 3000000, 1300000,
    #            1400000, 1500000],
    #     "조회수": [150000, 80000, 240000, 190000, 155000, 92000, 350000, 210000, 170000, 120000,
    #             290000, 160000, 100000, 310000, 140000, 320000, 250000, 270000, 300000, 120000,
    #             140000, 150000],
    #     "지출금액": [500000, 400000, 600000, 550000, 500000, 420000, 700000, 620000, 570000, 530000,
    #              690000, 500000, 450000, 720000, 540000, 780000, 650000, 700000, 750000, 480000,
    #              520000, 540000]
    # }
    #
    # # 데이터프레임 생성
    # df = pd.DataFrame(companies_data)
    file = r'C:\Users\LeadersTrading\Documents\카카오톡 받은 파일\company_distribution_integer.csv'
    df = pd.read_csv(file, encoding='UTF-8')

    # Streamlit 앱 타이틀
    st.title("기업별 퍼포먼스 데이터")

    # 22개의 기업 정보를 카드 형식으로 출력
    for index, row in df.iterrows():
        st.markdown("---")  # 구분선
        st.subheader(f"{row['Company']}")
        col1, col2, col3 = st.columns(3)  # 3개의 열을 나란히 표시

        # 첫 번째 열: 도달 수
        with col1:
            st.metric(label="도달", value=f"{row['Views']:,}")

        # 두 번째 열: 조회수
        with col2:
            st.metric(label="조회 수", value=f"{row['Hits']:,}")

        # 세 번째 열: 지출 금액
        with col3:
            st.metric(label="리액션 수", value=f"{row['Likes']:,}")

def test_2():
    # Streamlit 페이지 제목 설정
    st.title("Seaborn과 Matplotlib을 활용한 데이터 시각화")

    # 샘플 데이터셋 로드 (seaborn 내장 데이터셋 사용)
    data = sns.load_dataset("penguins")

    # Seaborn을 이용하여 scatter plot 생성
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x="flipper_length_mm", y="body_mass_g", hue="species", ax=ax)

    # Streamlit에 그래프 표시
    st.pyplot(fig)

def test_3():
    # 페이지 수에 맞춰 슬라이드 내용을 사전으로 정의
    slides = {
        1: "Slide 1: Introduction\n\nWelcome to the presentation!",
        2: "Slide 2: Overview\n\nHere's an overview of what we're going to cover.",
        3: "Slide 3: Details\n\nDetailed information goes here.",
        4: "Slide 4: Conclusion\n\nThank you for watching!"
    }

    # 세션 상태로 슬라이드 번호 관리 (초기값: 1)
    if "slide_number" not in st.session_state:
        st.session_state.slide_number = 1

    # 슬라이드 내용 출력
    st.markdown(f"### {slides[st.session_state.slide_number]}")

    # 이전 슬라이드 버튼
    if st.session_state.slide_number > 1:
        if st.button("Previous"):
            st.session_state.slide_number -= 1

    # 다음 슬라이드 버튼
    if st.session_state.slide_number < len(slides):
        if st.button("Next"):
            st.session_state.slide_number += 1

    # 슬라이드 번호 표시
    st.write(f"Slide {st.session_state.slide_number} of {len(slides)}")

#슬라이드 및 다중 페이지 대시보드 템플릿
def test_4():
    # 사이드바로 페이지 선택
    st.sidebar.title("Presentation Navigation")
    page = st.sidebar.radio("Go to", ["Introduction", "Overview", "Details", "Conclusion"])

    # 페이지 내용 구성
    if page == "Introduction":
        st.title("Introduction")
        st.write("Welcome to the presentation!")
    elif page == "Overview":
        st.title("Overview")
        st.write("Here's an overview of what we're going to cover.")
    elif page == "Details":
        st.title("Details")
        st.write("Here is the detailed information.")
    elif page == "Conclusion":
        st.title("Conclusion")
        st.write("Thank you for watching!")

#모던한 카드 레이아웃
def test_5():
    # 3개의 칼럼으로 카드 스타일 구성
    st.title("Modern Dashboard")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Metric 1")
        st.metric(label="Sales", value="70k", delta="-5%")
        st.write("Monthly sales performance.")

    with col2:
        st.header("Metric 2")
        st.metric(label="Revenue", value="$100k", delta="8%")
        st.write("Monthly revenue growth.")

    with col3:
        st.header("Metric 3")
        st.metric(label="Customer Satisfaction", value="95%", delta="2%")
        st.write("Customer feedback summary.")


#탭을 이용한 인터페이스
def test_6():
    st.title("Report Dashboard")

    tab1, tab2, tab3 = st.tabs(["Summary", "Detailed Analysis", "Conclusions"])

    with tab1:
        st.header("Executive Summary")
        st.write("Summary content goes here.")

    with tab2:
        st.header("Detailed Analysis")
        st.write("Detailed analysis content goes here.")
        st.line_chart([1, 2, 3, 4, 5])  # 예제 차트 추가

    with tab3:
        st.header("Conclusions")
        st.write("Conclusion content goes here.")


#CSS로 텍스트 스타일링 및 배경색 추가
def test_7():
    st.markdown("""
        <style>
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
        .card h3 {
            color: #007bff;
        }
        </style>
        """, unsafe_allow_html=True)

    # 카드 레이아웃을 적용하여 섹션을 구성
    st.markdown('<div class="card"><h3>Section 1</h3><p>Content for section 1 goes here.</p></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Section 2</h3><p>Content for section 2 goes here.</p></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>Section 3</h3><p>Content for section 3 goes here.</p></div>',
                unsafe_allow_html=True)

#커스텀 폰트 및 컬러 스키마 추가
def test_8():
    st.markdown("""
        <style>
        body {
            font-family: 'Arial', sans-serif;
            color: #333;
            background-color: #e9ecef;
        }
        .highlight {
            font-size: 24px;
            color: #FF5733;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="highlight">This is a highlighted text section.</div>', unsafe_allow_html=True)

#드롭다운 메뉴와 상호작용 기반 인터페이스
def test_9():
    st.title("Interactive Dashboard")

    # 드롭다운을 이용한 선택 메뉴
    option = st.selectbox("Select a Data Category", ("Sales", "Marketing", "Customer Feedback"))

    if option == "Sales":
        st.write("Sales data visualization goes here.")
    elif option == "Marketing":
        st.write("Marketing data visualization goes here.")
    elif option == "Customer Feedback":
        st.write("Customer feedback analysis goes here.")

    # 체크박스 기반 추가 옵션
    if st.checkbox("Show Advanced Metrics"):
        st.write("Advanced metrics are displayed here.")

#데이터 테이블과 차트를 활용한 분석 섹션
def test_10():
    # 더미 데이터 생성
    data = pd.DataFrame(np.random.randn(10, 5), columns=("A", "B", "C", "D", "E"))

    # 컬럼 배치
    col1, col2 = st.columns(2)

    with col1:
        st.write("Data Table")
        st.dataframe(data)

    with col2:
        st.write("Chart")
        st.bar_chart(data)


def test_df():


    file = "['강서구', '양천구', '영등포구', '마포구', '용산구']_python_잡코리아.csv"
    df = pd.read_csv(file, encoding='cp949')

    today = str(datetime.datetime.today()).split(' ')[0]
    df = df[df['마감일'] >= today].reset_index(drop=True)
    df = df.sort_values(['마감일'], ascending=True).reset_index(drop=True)

    df.to_csv(f'new_{file}', encoding='cp949')


def test():
    plt.figurl(figsize=(10, 4))
    sns.histplot(date['거래금액'], kde=True)
    plt.tilte()
    plt.xlabel()
    plt.ylabel()
    plt.show()




test_9()
