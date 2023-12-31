import streamlit as st
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'読み込み中です。 {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'完了！'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに表示')
if button:
    right_column.write('正解')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3')
