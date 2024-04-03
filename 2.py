def bracket_match(input_str):
    l_l = []
    l_r = []
    result = len(input_str) * [" "]
    for i in range(len(input_str)):
        if input_str[i] == '(':
            l_l.append(i)
        elif input_str[i] == ')':
            if l_l:
                l_l.pop()
            else:
                l_r.append(i)
    for i in range(len(input_str)):
        if i in l_l:
            result[i] = 'x'
        if i in l_r:
            result[i] = '?'
    return result


if __name__ == "__main__":
    input_str = input("请输入字符串：")
    result = bracket_match(input_str)
    print("括号匹配检测结果：")
    print(input_str)
    print(''.join(result))
