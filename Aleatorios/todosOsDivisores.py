num = int(input())
nums = [i for i in range(1, num//2+1) if num%i==0]
nums.append(num)
print(" ".join(str(i) for i in nums))