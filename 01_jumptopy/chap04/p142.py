def my_sum(num1,num2):
    print("덧셈 연산")
    internal_result =num1 + num2
    if internal_result>0:
        print("연산결과가 양수로 분석됩니다.")
    elif internal_result==0:
        print("연산결과가 0으로 분석됩니다.")
    else:
        print("연산결과가 음수로 분석됩니다.")
    return internal_result

result = my_sum(1,2)

print("최종 연산 결과 : %d" %result)
print("계산기 ver1.0 종료")