def show_candidates(candidate_list):
    print("==연습생 리스트==")
    for name in candidate_list:
        print(name.strip(),end=' ')

def make_idol(candidate_list):
    for name in candidate_list:
        print("신예 아이돌 "+ name.rstrip() + " 인기 급상승")

def make_world_star(candidate_list):
    for name in candidate_list:
        print("아이돌 "+ name.rstrip() +" 월드스타 등극")

f=open("연습생.txt",'r',encoding='UTF-8')
candidate_list=f.readlines()
f.close()

show_candidates(candidate_list)
make_idol(candidate_list)
make_world_star(candidate_list)