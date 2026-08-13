import psutil
print("Hi,I am something.")

def check():
    a = int(input("Enter your cpu usage : "))
    b = psutil.cpu_percent(interval = 1)
    print(f"Your current cpu percentage is : {b}")
    if b > a:
        print("Email sent")
    else:
        print("Ralax man")

check()
