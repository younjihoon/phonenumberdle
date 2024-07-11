import streamlit as st
from phonenumberdle import Numberdle

st.title('phonenumberdle - 즐거운 전화번호 숫자야구 게임!')
st.write('전화번호 숫자야구 게임은 4자리의 숫자를 맞추는 게임입니다. 전화번호의 앞 4자리와 뒷 4자리에 대해 동시에 진행됩니다. 숫자는 0부터 9까지 입니다. 숫자와 위치가 모두 맞으면 스트라이크, 숫자만 맞으면 볼, 숫자와 위치가 모두 틀리면 아웃입니다. 4자리의 숫자를 입력하고, 결과를 확인하세요!')
st.write('예시 : ')
st.write('010-1234-5678에 대해 5324를 입력하면 1S2B | 1S0B 입니다.')
st.write('010-1234-5678에 대해 6755를 입력하면 OUT | 0S4B 입니다.')

if 'game' not in st.session_state:
    st.session_state['game'] = Numberdle()
game = st.session_state['game']
game_name = st.selectbox("누구의 전화번호로 진행할까요?",game.get_names())
game.set_name(game_name)
trial = st.text_input('4자리 숫자를 입력해주세요.')
# st.button('확인',on_click=game.res(trial))
if st.button('결과 확인'):
    try:
        res = game.result(trial)
        st.write(f'{game_name}의 앞자리 : {res[0]}')
        st.write(f'{game_name}의 뒷자리 : {res[1]}')
        st.write(game.get_log())
    except Exception as e:
        st.write(e)

if st.button('로그 초기화'):
    st.write(f'로그를 초기화 합니다.')
    del st.session_state['game']