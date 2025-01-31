def print_korean_name_art(character):
    name_art = {
        '김': [
            "  **  **    **",
            "      **    **",
            "      **    **",
            "      **    **",
            "      **    **",
            "      **    **",
            "              ",
            "  ** ** ** ** ",
            "  **        **",
            "  **        **",
            "  **        **",
            "  ** ** ** **",
            "              ",
            "              ",
            "              ",
            "              "
        ],
        '하': [
            "    *        *    ",
            " **** ***    *    ",
            " **** *****  *    ",
            "   *****     *    ",
            "  ** ***     *    ",
            " ***     **  ***  ",
            " ***     **  *    ",
            " ***     **  *    ",
            "   *****     *    ",
            "    *        *    ",
            "             *    ",
            "             *    ",
            "                  ",
            "                  ",
            "                  ",
            "                  "
        ],
        '은': [
            "   *******    ",
            "  ***   ***   ",
            "  **     *    ",
            "  ***  ***    ",
            "   ******     ",
            "************  ",
            "  **          ",
            "  **          ",
            "  **          ",
            "  **********  ",
            "              ",
            "              ",
            "              ",
            "              ",
            "              ",
            "              "
        ]
    }

    # 16x16 배열을 입력된 문자로 변경
    for char, art in name_art.items():
        for i in range(16):
            name_art[char][i] = name_art[char][i].replace('*', character)

    # 각 글자의 아스키 아트를 출력
    for i in range(16):
        print(name_art['김'][i] + ' ' + name_art['하'][i] + ' ' + name_art['은'][i])


# 사용자로부터 문자를 입력받기
user_character = input("문자를 입력하세요: ")
print_korean_name_art(user_character)
