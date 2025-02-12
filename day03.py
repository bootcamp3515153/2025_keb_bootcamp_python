#2번 문제 + 복합기능 다 구현해보기

import random
drinks_foods_keys = ["위스키","와인","소주","고량주","사케"]
drinks_foods_values = ["초콜릿","치즈","삼겹살","양꼬치","광어회"]

def print_menu(n):
    print(f'< {drinks_foods_keys[n-1]}에 어울리는 안주는 {drinks_foods_values[n-1]} 입니다 >')

while True:
    selection = int(input(f'사용할 기능을 선택하세요.\n1) 메뉴 추가 2) 메뉴 삭제 3) 메뉴 보기 4) 종료\n>>'))
    if selection == 1: #메뉴 추가
        app_key = input(f'추가할 술 메뉴를 입력하시오 : ')
        app_value = input(f'추가할 안주 메뉴를 입력하시오 : ')
        drinks_foods_keys.append(app_key)
        drinks_foods_values.append(app_value)

    elif selection == 2: #메뉴 삭제
        re_key = int(input(f'삭제할 메뉴의 번호를 입력하시오 : '))
        drinks_foods_keys.pop(re_key-1)
        drinks_foods_values.pop(re_key-1)

    elif selection == 3: #메뉴 보기
        menu_list = '다음 술 중에 고르시오.\n'
        for i in range(len(drinks_foods_keys)):
            menu_list = menu_list + f'{i+1}) {drinks_foods_keys[i]}  '
        menu_list = menu_list + f'{len(drinks_foods_keys)+1}) 아무거나  {len(drinks_foods_keys)+2}) 전 화면으로 돌아가기\n>>'

        while True:
            menu = int(input(menu_list))
            if menu <= len(drinks_foods_keys):
                print_menu(menu)
            elif menu == len(drinks_foods_keys)+1:
                ran_Num = random.randint(0,len(drinks_foods_keys)-1)
                print_menu(ran_Num)
            else:
                print(f'전 화면으로 돌아갑니다.')
                break

    else: #종료
        print("다음에 또 오세요.")
        break