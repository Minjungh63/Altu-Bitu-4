"""
N개의 차량이 지나간 후,
대근이는 터널의 입구
영식이는 터널의 출구
대근이와 영식이는 자신들이 적어 둔 차량 번호의 목록을 보고,
터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차들이 몇 대 있다는 것

입력은 총 2N+1개의 줄
첫 줄에는 차의 대수 N(1 ≤ N ≤ 1,000)
둘째 줄부터 N개의 줄에는 대근이가 적은 차량 번호 목록
N+2째 줄부터 N개의 줄에는 영식이가 적은 차량 번호
영어 대문자('A'-'Z')와 숫자('0'-'9')로만
같은 차량 번호가 두 번 이상 주어지는 경우는 없다.

터널 내부에서 반드시 추월을 했을 것으로 여겨지는 차가 몇 대인지 출력
"""
N = int(input())
D = {}
cnt = 0

if N == 1:
    print(cnt)
else:
    Y = []
    for i in range(N):
        D[input()] = i # 차번호를 key, 들어간 순서를 value로 저장
    for _ in range(N):
        Y.append(D[input()]) # 차의 "들어간 순서"를 나온 순서대로 저장
    for i in range(len(Y) - 1):
        for j in range(i + 1, len(Y)):
            if Y[i] > Y[j]: #A보다 터널에서 늦게 나온 차 중에서, A보다 인덱스가 작은 차 가 하나라도 있다면
                cnt += 1
                break

    print(cnt)
