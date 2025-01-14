import streamlit as st


# text를 입력하는 검색창 하나

# ani_list에 있는 글자가 일부라도 들어가면
# img_list에 있는 사진이 출력되도록 

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 검색 입력창
ani = st.text_input('검색하실 애니메이션을 입력하세요')

# 입력값이 ani_list의 일부와 매칭되는지 확인
if ani:
    found = False
    for i, title in enumerate(ani_list):
        if ani in title:  # 부분 문자열 검색
            st.image(img_list[i], caption=title, width=300)
            found = True
    if not found:
        st.write("해당 애니메이션을 찾을 수 없습니다.")


'''
search = st.text_input('검색하실 애니메이션을 입력하세요')

for ani in ani_list:
    if search in ani :
        img_idx=ani_list.index(ani)

if search !='':
    st.image(img_list[img_idx])
'''