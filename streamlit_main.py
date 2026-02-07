import streamlit as st

st.title("안녕하세요 Streamlit")

st.header("헤더를 입력할 수 있어요")

st.subheader("이것은 subheader입니다")

st.caption("캡션을 넣어봅니다")

sample_code = '''
def function():
    print('hello, world')
    '''
st.code(sample_code)