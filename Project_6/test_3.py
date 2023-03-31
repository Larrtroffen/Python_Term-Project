import math

def ret_str(num:int):
    # 创建字典
    nums = [x for x in range(0, 11)]
    nums.append(100)
    chars = "零壹贰叁肆伍陆柒捌玖拾佰"
    strs = [char for char in chars]
    # print(len(strs)==len(nums))

    num_dict = {num:char for num,char in zip(nums,strs)}
    # print(num_dict)

    # 获取每一位数
    target_list = []
    while num>0:
        target_list.append(num%10)
        num//=10
    # print(target_list)

    for i in range(len(target_list)):
        target_list[i]*=int(math.pow(10,i))
    # print(target_list)
    target_list.reverse()

    # 判断数的大小并添加相应的字符串
    ans_str = ''
    for num in target_list:
        if num/100 >=1:
            ans_str += num_dict[num//100]+num_dict[100]
        elif num/10 >=1:
            ans_str += num_dict[num//10]+num_dict[10]
        # 这个判断实际上是一个针对题目三位数的解法，不具备高位数可扩展性
        # 如果扩展高位，需要在num==0时写循环判断后面是否全为0，不然1010这种情况就会输出1000
        # 末尾出现0只有两种情况 100或者10
        elif num==target_list[len(target_list)-1] and num==0:
            break
        else:
            ans_str += num_dict[num]
    return ans_str

if __name__ == "__main__":
    print(ret_str(8))
    print(ret_str(45))
    print(ret_str(102))
    print(ret_str(999))
    print(ret_str(40))
    print(ret_str(520))
    print(ret_str(10))
    # num  = int(input("请输入一个0到999之间的整数:"))
    # print(ret_str(num))