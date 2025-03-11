if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    unique_scores=list(set(arr))
    unique_scores.sort()
    runner_up=unique_scores[-2]
    print(runner_up)