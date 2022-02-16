from stringprep import in_table_c21
import streamlit as st
import pandas as pd

st.title('Саволнома роҳнамои касбӣ')
st.title('Дар зарфи 5 дакика аз санҷиш гузашта, соҳибӣ касби мувофиқ шаведҷ')


choice = []
int1 = st.radio(
     "Фарз кардем, ки баъди таълими мувофиқ Шумо ҳама гуна  корро иҷро карда метавонед. Агар ба Шумо интихоби аз ду имконият якеро пешниҳод кунанд, кадомашро меписандед?",
     ('Нигоҳубини ҳайвонот', 'Идора кардани мошин ва дигар таҷҳизоти техникӣ (таъмир ва нигоҳубин)'))
if int1 == 'Нигоҳубини ҳайвонот':
    choice.append('1')
if int1 == 'Идора кардани мошин ва дигар таҷҳизоти техникӣ (таъмир ва нигоҳубин)':
    choice.append('11')

int2 = st.radio(
     "",
     ('Кӯмак ба беморон', 'Тартиб додани ҷадвал, нақша ва барномаҳо барои техникаи компютерӣ'))
if int2 == 'Кӯмак ба беморон':
    choice.append('2')
elif int2 == 'Тартиб додани ҷадвал, нақша ва барномаҳо барои техникаи компютерӣ':
    choice.append('22')


int3 = st.radio(
     "",
     ('Назорат кардани сифати мусаввараи китобҳо, плакатҳо, открыткаҳои бадеӣ, картаҳои граммофон', 'Назорат кардани ҳолат ва сабзиши растаниҳо'))
if int3 == 'Назорат кардани сифати мусаввараи китобҳо, плакатҳо, открыткаҳои бадеӣ, картаҳои граммофон':
    choice.append('3')
else:
    choice.append('33')

int4 = st.radio(
     "",
     ('Коркарди масолеҳ (чӯб, матоъ, пластмасса ва ғайраҳо)', 'Муҳокимаи китобҳои бадеӣ (ё худ намоишномаҳо, консертҳо)'))
if int4 == 'Коркарди масолеҳ (чӯб, матоъ, пластмасса ва ғайраҳо)':
    choice.append('4')
else:
    choice.append('44')

int5 = st.radio(
     "",
     ('Муҳокима кардани асарҳо, мақолаҳои илмии оммафаҳм', 'Ба истеъмолкунандагон расондани маҳсулот, фурӯш ва таблиғоти он'))
if int5 == 'Муҳокима кардани асарҳо, мақолаҳои илмии оммафаҳм':
    choice.append('5')
else:
    choice.append('55')


int6 = st.radio(
     "",
     ('Парвариши ҳайвоноти ҷавон (ин ё он ҷинс)', 'Машқ додани рафиқон ё кӯдакон барои иҷрои амалиёт (меҳнатӣ, таълимӣ, варзишӣ)'))
if int6 == 'Парвариши ҳайвоноти ҷавон (ин ё он ҷинс)':
    choice.append('6')
else:
    choice.append('66')


int7 = st.radio(
     "",
     ('Нусхабардории расму тасвирҳо (ё ҷур кардани асбобҳои мусиқӣ)', 'Идора кардани  ягон воситаи боркашони борбардор ё (нақлиёт) трактор, крани борбардор ва ғайраҳо'))
if int7 == 'Нусхабардории расму тасвирҳо (ё ҷур кардани асбобҳои мусиқӣ)':
    choice.append('7')
else:
    choice.append('77')

int8 = st.radio(
     "",
     ('Ба одамон фаҳмондани маълумотҳои ба онҳо зарур ', 'Оро додани намоишгоҳҳо, витринаҳо ё ширкат варзидан дар тайёр кардани намоишномаҳо, барномаҳо, барномаҳои рақсу суруд)'))
if int8 == 'Ба одамон фаҳмондани маълумотҳои ба онҳо зарур ':
    choice.append('8')
else:
    choice.append('88')



int9 = st.radio(
     "",
     ('Таъмири ашё, маҳсулот (либос, техника), манзилгоҳ', 'Ҷустуҷӯ ва ислоҳи хато дар матнҳо, ҷадвалҳо, тасвирҳо'))
if int9 == 'Таъмири ашё, маҳсулот (либос, техника), манзилгоҳ':
    choice.append('9')
else:
    choice.append('99')


int10 = st.radio(
     "",
     ('Табобати ҳайвонот', 'Иҷрои ҳисобу китоб'))
if int10 == 'Табобати ҳайвонот':
    choice.append('10')
else:
    choice.append('1010')

int11= st.radio(
     "",
     ('Парвариш кардани намудҳои нави растаниҳо', 'Ба нақша гирифтан ва омода намудани навъҳои маҳсулоти саноатӣ (мошинаҳо, либос, хона, молҳои истеъмолӣ ва ғайраҳо)'))
if int11 == 'Парвариш кардани намудҳои нави растаниҳо':
    choice.append('11')
else:
    choice.append('1111')


int12 = st.radio(
     "",
     ('Ҳаллу фасли баҳс, ҷанҷоли байни одамон, бовар кунондан, фаҳмонидан, танбеҳ додан, ҳавасманд кардан', 'Сарфаҳм рафтан ба нақшаҳо, тарҳҳо, ҷадвалҳо'))
if int12 == 'Ҳаллу фасли баҳс, ҷанҷоли байни одамон, бовар кунондан, фаҳмонидан, танбеҳ додан, ҳавасманд кардан':
    choice.append('12')
else:
    choice.append('1212')


int13 = st.radio(
     "",
     ('Мушоҳида намудан  ва омӯхтани фаъолияти маҳфилҳои   ҳаваскорони санъат.', 'Мушоҳида кардан ва омӯхтани ҳаёти микробҳо'))
if int13 == 'Мушоҳида намудан  ва омӯхтани фаъолияти маҳфилҳои   ҳаваскорони санъат.':
    choice.append('13')
else:
    choice.append('1313')



int14 = st.radio(
     "",
     ('Идора кардан ва омӯхтани  дастгоҳҳои тиббӣ.', 'Расонидани ёрии тиббӣ ба одамон ҳангоми ҷарроҳат ёфтан, лат хӯрдан, сӯхтани ягон узви бадан ва ғ.'))
if int14 == 'Идора кардан ва омӯхтани  дастгоҳҳои тиббӣ.':
    choice.append('14')
else:
    choice.append('1414')

int15 = st.radio(
     "",
     ('Ҳисоботи муфассал навиштан доир  ба зуҳурот, воқеоте, ки мавриди мушоҳида қарор доранд, объектҳои санҷишӣ ва ғайра', 'Иншо, тасвири бадеӣ намудани воқеот (аз рӯи мушоҳида, хаёл).'))
if int15 == 'Ҳисоботи муфассал навиштан доир  ба зуҳурот, воқеоте, ки мавриди мушоҳида қарор доранд, объектҳои санҷишӣ ва ғайра':
    choice.append('15')
else:
    choice.append('1515')

int16 = st.radio(
     "",
     ('Дар беморхона санҷишҳои лабораторӣ гузарондан.', 'Қабул, муоинаи беморон , бо онхо ҳамсуҳбат шудан, табобат таъин кардан.'))
if int16 == 'Дар беморхона санҷишҳои лабораторӣ гузарондан.':
    choice.append('16')
else:
    choice.append('1616')


int17 = st.radio(
     "",
     ('Ранга кардани девори биноҳо ва сатҳи маснуот..', 'Иҷро кардани мантажи бино, ҷамъоварии мошинҳо.'))
if int17 == 'Ранга кардани девори биноҳо ва сатҳи маснуот..':
    choice.append('17')
else:
    choice.append('1717')

int18 = st.radio(
     "",
     ('Ташкили сайёҳатҳои фарҳангии ҳамсолон ва  хурдсолон (ба теарт, осорхона), экскурсияҳо, роҳпаймоии туристӣ ва  ғ.', 'Дар саҳна бози кардан, иштирок дар консертҳо.'))
if int18 == 'Ташкили сайёҳатҳои фарҳангии ҳамсолон ва  хурдсолон (ба теарт, осорхона), экскурсияҳо, роҳпаймоии туристӣ ва  ғ.':
    choice.append('18')
else:
    choice.append('1818')

int19 = st.radio(
     "",
     ('Аз руи нақша тайёркунии детал, маҳсулот (мошин, либос), сохтани биноҳо.', 'Машғул шудан ба нақшакашӣ, нусхабардории нақшаҳо,харитаҳо.'))
if int19 == 'Аз руи нақша тайёркунии детал, маҳсулот (мошин, либос), сохтани биноҳо.':
    choice.append('19')
else:
    choice.append('1919')


int20 = st.radio(
     "",
     ('Мубориза бурдан бар зидди касалиҳои растанӣ, ҳашароти зараррасони ҷангал, боғ.', 'Кор дар мошинҳои клавиатурадор (машинаҳои чопӣ ва ғ.).)'))
if int20 == 'Мубориза бурдан бар зидди касалиҳои растанӣ, ҳашароти зараррасони ҷангал, боғ.':
    choice.append('20')
else:
    choice.append('2020')



for i in choice:
    if '11' and '4' and '77' and '99' and '1111' and '14' and '1717' and '19' in choice:
        choice = 'Инсон-техник, касбхои зерин ба шумо мувофиканд: Монтажчӣ, Дуредгар, Челонгар, Токар, Дӯзандагӣ, Гилкор, Электромонтёр, Инженер, Конструктор, Технолог, Кайҳоннавард'
for i in choice:   
    if '2' and '44' and '66' and '8' and '12' and '16' and '18' in choice:
        choice = 'Инсон-инсон, касбҳои зерин ба шумо мувофиқанд: Мураббии кӯдакистон, Ҳамшираи шафқат, Корманди милиса, Фурӯшанда, Корманди иҷтимоӣ, Пешхизмат, Менеҷер, Равоншинос, Ёвари котиб, Омӯзгор, Ҳуқуқшинос, Муфаттиш'
for i in choice:
    if '22' and '5' and '99' and '1010' and '1212' and '15' and '1919' and '2020' in choice:
        choice = 'Инсон-аломатҳои системавӣ, касбҳои зерин ба шумо мувофиқанд: Хазинадор, Оператори компютер, Ҳарфчин, Оператори телефон, Оператори алоқа, Стенограф, Муҳосиб, Сейсмолог, Тарҷумон, Барномасоз, Иқтисодчӣ'
for i in choice:
    if '3' and '55' and '7' and '88' and '13' and '1515' and '17' and '1818' in choice:
        choice = 'Инсон-Образи бадеӣ, касбҳои зерин ба шумо мувофиқанд: Буранда, Сартарош, Ошпаз, Дӯзандагӣ, Суратгир, Кандакор, Дизайнер, Меъмор, Мусиқачӣ, Хореограф, Рассом, Қайкалтарош, Ороишгар'
for i in choice:   
    if '1' and '33' and '6' and '10' and '11' and '1313' and '1616' and '20' in choice:
        choice = 'Инсон-табиат, касбҳои зерин ба шумо мувофиқанд: Чорводор, Боғбон, Деҳқон, Дарахтпарвар, Агроном, Ветеринар, Геолог, Биолог, Химик'


if st.button('Result'):
     st.write(choice)

