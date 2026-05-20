import streamlit as st
st.title('Ju Motors Aluguel de Carros')
st.sidebar.title('Escolha um modelo: ')
st.sidebar.image('logo.png')

carros = ['BMW','Mustang','Porsche', 'Fusca', 'Hb20']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)



st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Qauntos km você rodou com o {opcao}?')

if opcao == 'BMW':
 diaria = 600
elif opcao == 'Mustang':
 diaria = 900
elif opcao == 'Porsche':
 diaria = 400
elif opcao == 'Hb20':
 diaria = 300
elif opcao == 'Fusca':
 diaria = 250




if st.button('Calcular'):
    dias = int(dias)
    km = float(km)


    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km



    st.warning(f'Você alugou o {opcao} por dias e rodou {km} km. O valor total a pagar é R${aluguel_total : .2f}')