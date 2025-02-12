#1번 문제

import random
drinks_foods_keys = ["위스키","와인","소주","고량주","사케"]
drinks_foods_values = ["초콜릿","치즈","삼겹살","양꼬치","광어회"]

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) {drinks_foods_keys[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods_values[0]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods_values[1]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods_values[2]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods_values[3]} 입니다')
    elif menu == '5':
        print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods_values[4]} 입니다')
    elif menu == '6':
        random_drink = random.choice(drinks_foods_keys)
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods_values[drinks_foods_keys.index(random_drink)]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break