# Py-algorism5

# 동작원리

1. 리스트 a에 아직 자료가 남아 있다면 > while a:

2. 남은 자료 중에 맨 앞의 값을 뽑아냄 > value = a.pop(0)

3. 그 값이 result의 어느 위치에 들어가면 적당할지 알아냄 > ins_idx = find_ins_idx(result, value)

4. 3번 과정에서 찾아낸 위치에 뽑아낸 값을 삽입 > result.insert(ins_idx, value)

5.  1번 과정으로 돌아가 자료가 없을 때까지 반복
