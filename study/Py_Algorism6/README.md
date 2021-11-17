# Py-algorism6

# 자료가 크기 순서대로 정렬된 리스트에서 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘

# (리스트에 찾는 값이 없으면 -1을 돌려준다.)

- 리스트의 자료가 순서대로 정렬되어 있으므로 훨씬 더 빠르게 탐색할 수 있음

- 탐색할 자료를 둘로 나누어 찾는 값이 있을 법한 곳만 탐색하기 때문에 자료를 하나하나 찾아야하는 순차 탐색보다 원하는 자료를 훨씬 빨리 찾을 수 있음

# 알고리즘 순서

1. 중간 위치를 찾음

2. 찾는 값과 중간 위치 값을 비교

3. 같다면 원하는 값을 찾은 것이므로 위치 번호를 결괏값으로 돌려줌

4. 찾는 값이 중간 위치 값보다 크다면 중간 위치의 오른쪽을 대상으로 다시 탐색

5. 찾는 값이 중간 위치 값보다 작다면 중간 위치의 왼쪽을 대상으로 다시 탐색