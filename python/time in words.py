k=3
n=00
nums = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one',
       'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight','twenty nine']
if n==0:
    print(nums[k-1]+ ' o clock ')
elif n<15:
    print(nums[n-1] + " minutes past "+ nums[k-1])
elif n==15:
    print(" quater past "+nums[k-1])
elif n<30:
    print(nums[n-1] + "half past "+nums[k-1])
elif n==45:
    print(" quarter to "+ nums[k])
elif n<45:
    print(nums[60-n-1]+ " minutes to go "+ nums[k])
else:
    pass
