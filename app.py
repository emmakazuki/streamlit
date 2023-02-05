import streamlit as st
from PIL import Image

st.title("かずきあぷりaaaabbbbbb")
st.caption("これはテストです")
st.subheader("自己紹介")
st.text('テキストてすと')


code = '''
import streamlit as st

st.title('テスト')
'''
st.code(code,language='python')

image = Image.open('スクリーンショット 2023-02-03 235530.png')
st.image(image,width=200)

name = st.text_input('名前')

submit_btn = st.button('送信')
cansel_btn = st.button('キャンセル')

#セレクトボックス
age_category = st.selectbox(
    '年齢層',('子ども','大人'))
# 複数選択
hobby = st.multiselect(
    '趣味',
    ('スポーツ','読書','BTC'))
#スライダー
height = st.slider('身長',min_value=110,max_value=210)

#日付
start_date = st.date_input(
    '開始日')


if submit_btn:
    st.text(f'ようこそ{name}さん')
    st.text(f'年齢層:{age_category}')
    st.text(f'趣味:{",".join(hobby)}')
    st.text(f'身長:{height}')
    st.text(f'日付:{start_date}')
