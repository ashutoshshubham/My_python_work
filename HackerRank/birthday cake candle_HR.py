def birthdayCakeCandles(candles):
    maximum = max(candles)
    count = candles.count(maximum)
    print(count)

candles = list(map(int,input("Enter  Size of candles ").split()))
birthdayCakeCandles(candles)