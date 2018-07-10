spamlist = list()
email_list = list()
i = 0

while True:
    menu = input('1. 스팸 단어 입력, 2. 스팸 메일 검사, 3. 종료: ')


    if menu == '1':
        while True:
            one = input('스팸 단어를 입력하세요: ')
            if one not in spamlist and one != 'exit':
                spamlist.append(one)
            elif one in spamlist:
                print('이미 있습니다.')
            if one == 'exit':
                break
                menu = input('1. 스팸 단어 입력, 2. 스팸 메일 검사, 3. 종료: ')

        
    
    elif menu == '2':
        print(spamlist)
        email = input('이메일 제목: ')
        #email_list.append(email)
        '''while i < len(spamlist):
            if email in spamlist[i]:
                print('스팸 이메일입니다.')
            i = i + 1

        while i < len(spamlist):
            if email not in spamlist[i]:
                print('스팸 이메일이 아닙니다.')
            i = i + 1'''

        while True:
            if email in spamlist:
                print('스팸 이메일입니다')
                break
            
                menu = input('1. 스팸 단어 입력, 2. 스팸 메일 검사, 3. 종료: ')
            elif email not in spamlist:
                print('스팸 이메일 아닙니다')
                break
                menu = input('1. 스팸 단어 입력, 2. 스팸 메일 검사, 3. 종료: ')

        #i = 0

    elif menu == '3':
        print('프로그램 종료')
        break

    else:
        print('없는 메뉴입니다.')

    
    
