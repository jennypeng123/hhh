#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������
���ڣ�2022/5/11
"""
print("��ӭʹ��RPSLS��Ϸ")
import random
player_choice=input("����������ѡ��:")#��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(player_choice):#def�Զ��庯��
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if player_choice=="ʯͷ":#if������������
       player_choice=0
       return player_choice#���غ���
    elif player_choice=="ʷ����":#elif����������������
         player_choice=1
         return player_choice
    elif player_choice=="ֽ" :
         player_choice=2
         return player_choice
    elif player_choice == "����":
         player_choice=3
         return player_choice
    elif player_choice=="����":
         player_choice=4
         return player_choice
    else:#else��������ʣ������
        return "Error: No Correct Name��"
def number_to_name(comp_number):#def�Զ����º���
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if comp_number==0:#if��������
       comp_number="ʯͷ"
       return comp_number#���غ���
    elif comp_number==1:#elif����������������
         comp_number="ʷ����"
         return comp_number
    elif comp_number==2:
         comp_number="ֽ"
         return comp_number
    elif comp_number==3:
         comp_number="����"
         return comp_number
    elif comp_number==4:
         comp_number="����"
         return comp_number



def rpsls(player_choice):#def�Զ����º���
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
print("-------- ")# ���"-------- "���зָ�

player_choice_number=name_to_number(player_choice) # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
comp_number=int(random.randrange(5))# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
print("����ѡ��Ϊ",player_choice)
print("�����ѡ��Ķ�����",number_to_name(comp_number)) # ����Ļ����ʾ�����ѡ����������
if(player_choice=="����"and number_to_name(comp_number)=="ֽ"):# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
 print("��Ӯ��")
elif(player_choice=="ֽ"and number_to_name(comp_number)=="ʯͷ"):
    print("��Ӯ��")
elif (player_choice == "ʯͷ" and number_to_name(comp_number) =="����"):
    print("��Ӯ��")
elif(player_choice=="����"and number_to_name(comp_number)=="ʷ����"):
    print("��Ӯ��")
elif(player_choice=="ֽ"and number_to_name(comp_number)=="ʷ����"):
    print("��Ӯ��")
elif (player_choice == "ʯͷ" and number_to_name(comp_number) =="����"):
    print("��Ӯ��")
elif(player_choice=="ʷ����"and number_to_name(comp_number)=="����"):
    print("��Ӯ��")
elif(player_choice=="����"and number_to_name(comp_number)=="����"):
    print("��Ӯ��")
elif(player_choice=="����"and number_to_name(comp_number)=="ֽ"):
    print("��Ӯ��")
elif(player_choice=="ʷ����"and number_to_name(comp_number)=="ʯͷ"):
    print("��Ӯ��")
elif player_choice==number_to_name(comp_number):
    print("���ͼ��������һ����")
else:
    print("�����Ӯ��")
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�











