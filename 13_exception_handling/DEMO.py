# keyboard interrupt
try:
    while True:
        num=input("Enter or Ctrl+c to STop ")
except KeyboardInterrupt:
    print("Program terminatted by UseR!!!")