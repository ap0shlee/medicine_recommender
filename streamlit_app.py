import streamlit as st

# 약물 데이터베이스 예시
medicine_db = {
    "생리통": [
        {"이름": "이부펜정", "형태": "정제 및 캡슐형", "성분": ["이부프로펜"]},
        {"이름": "타이레놀정", "형태": "정제 및 캡슐형", "성분": ["아세트아미노펜"]},
        {"이름": "애니펜시럽", "형태": "액상형", "성분": ["덱시부프로펜"]}
    ],
    "복통": [
        {"이름": "훼스탈플러스정", "형태": "정제 및 캡슐형", "성분": ["소화효소", "리파제"]},
        {"이름": "까스활명수액", "형태": "액상형", "성분": ["생약"]},
        {"이름": "다제스캡슐", "형태": "정제 및 캡슐형", "성분": ["소화효소"]}
    ],
    "두통": [
        {"이름": "이지엔6에이스정", "형태": "정제 및 캡슐형", "성분": ["아세트아미노펜"]},
        {"이름": "타이레놀시럽", "형태": "액상형", "성분": ["아세트아미노펜"]},
        {"이름": "속콜펜정", "형태": "정제 및 캡슐형", "성분": ["이부프로펜", "카페인"]}
    ],
    "근육통": [
        {"이름": "펜잘큐정", "형태": "정제 및 캡슐형", "성분": ["이부프로펜", "카페인"]},
        {"이름": "타이레놀시럽", "형태": "액상형", "성분": ["아세트아미노펜"]},
        {"이름": "부루펜정", "형태": "정제 및 캡슐형", "성분": ["이부프로펜"]}
    ],
    "관절통": [
        {"이름": "타세놀정", "형태": "정제 및 캡슐형", "성분": ["아세트아미노펜"]},
        {"이름": "세토펜시럽", "형태": "액상형", "성분": ["아세트아미노펜"]},
        {"이름": "부루펜시럽", "형태": "액상형", "성분": ["이부프로펜"]}
    ],
    "치통": [
        {"이름": "타이레놀정", "형태": "정제 및 캡슐형", "성분": ["아세트아미노펜"]},
        {"이름": "맥시부펜시럽", "형태": "액상형", "성분": ["덱시부프로펜"]},
        {"이름": "게보린정", "형태": "정제 및 캡슐형", "성분": ["이부프로펜", "카페인"]}
    ]
}
avoid_ingredients = {
    "천식": ["이부프로펜"],
    "알레르기": ["카페인", "이부프로펜"],
    "졸음": ["항히스타민"],
    "위장 장애": ["이부프로펜"]
}

def main():
    st.title("💊Painkiller Adviser")

    symptom = st.selectbox("1. 증상을 선택하세요:", list(medicine_db.keys()))
    selected_criteria = st.multiselect("2. 고려사항을 선택하세요:", list(avoid_ingredients.keys()))
    form = st.radio("3. 약 형태를 선택하세요:", ["정제 및 캡슐형", "액상형"])

    avoid_set = set()
    for c in selected_criteria:
        avoid_set.update(avoid_ingredients.get(c, []))

    st.markdown(f"### 🚫피해야 할 성분: {', '.join(avoid_set) if avoid_set else '없음'}")

    candidates = medicine_db.get(symptom, [])
    recommended = []
    for med in candidates:
        if med["형태"] == form and not any(ingredient in avoid_set for ingredient in med["성분"]):
            recommended.append(med["이름"])

    if recommended:
        st.markdown("### ✅추천 약물:")
        for name in recommended:
            st.write(f"- {name}")
    else:
        st.warning("조건에 맞는 약물이 없습니다. 약사와 상담을 권장합니다.")

# 하단 링크 추가
    st.markdown("---")
    st.markdown("📮간략한 설문 -> [https://forms.gle/N8vsQsLsfscxJedo8]")

if __name__ == "__main__":
    main()
