#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：彭杨杰
日期：2022/5/11
"""
print("欢迎使用RPSLS游戏")
import random
player_choice=input("请输入您的选择:")#显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(player_choice):#def自定义函数
    """
    将游戏对象对应到不同的整数
    """
    if player_choice=="石头":#if函数设置条件
       player_choice=0
       return player_choice#返回函数
    elif player_choice=="史波克":#elif函数设置另外条件
         player_choice=1
         return player_choice
    elif player_choice=="纸" :
         player_choice=2
         return player_choice
    elif player_choice == "蜥蜴":
         player_choice=3
         return player_choice
    elif player_choice=="剪刀":
         player_choice=4
         return player_choice
    else:#else函数设置剩下条件
        return "Error: No Correct Name”"
def number_to_name(comp_number):#def自定义新函数
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if comp_number==0:#if设置条件
       comp_number="石头"
       return comp_number#返回函数
    elif comp_number==1:#elif函数设置另外条件
         comp_number="史波克"
         return comp_number
    elif comp_number==2:
         comp_number="纸"
         return comp_number
    elif comp_number==3:
         comp_number="蜥蜴"
         return comp_number
    elif comp_number==4:
         comp_number="剪刀"
         return comp_number



def rpsls(player_choice):#def自定义新函数
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
print("-------- ")# 输出"-------- "进行分割

player_choice_number=name_to_number(player_choice) # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
comp_number=int(random.randrange(5))# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
print("您的选择为",player_choice)
print("计算机选择的对象是",number_to_name(comp_number)) # 在屏幕上显示计算机选择的随机对象
if(player_choice=="剪刀"and number_to_name(comp_number)=="纸"):# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
 print("您赢了")
elif(player_choice=="纸"and number_to_name(comp_number)=="石头"):
    print("您赢了")
elif (player_choice == "石头" and number_to_name(comp_number) =="剪刀"):
    print("您赢了")
elif(player_choice=="蜥蜴"and number_to_name(comp_number)=="史波克"):
    print("您赢了")
elif(player_choice=="纸"and number_to_name(comp_number)=="史波克"):
    print("您赢了")
elif (player_choice == "石头" and number_to_name(comp_number) =="蜥蜴"):
    print("您赢了")
elif(player_choice=="史波克"and number_to_name(comp_number)=="剪刀"):
    print("您赢了")
elif(player_choice=="剪刀"and number_to_name(comp_number)=="蜥蜴"):
    print("您赢了")
elif(player_choice=="蜥蜴"and number_to_name(comp_number)=="纸"):
    print("您赢了")
elif(player_choice=="史波克"and number_to_name(comp_number)=="石头"):
    print("您赢了")
elif player_choice==number_to_name(comp_number):
    print("您和计算机出的一样呢")
else:
    print("计算机赢了")
    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”











