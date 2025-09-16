#language: python 3
#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    dic = {key:arr.count(key) for key in set(arr)}
    del(dic[max(dic)])
    print(max(dic))
