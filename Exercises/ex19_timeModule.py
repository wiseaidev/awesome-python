import time 

def func1(n):
	list_ = []
	for i in range(n):
		list_ += [i**2]
	return	list_
def func2(n):
	list_ = []
	for i in range(n):
		list_.append(i**2)
	return list_
def func3(n):
	return [i**2 for i in range(n)]
def func4(n):
	return (i**2 for i in range(n))
def time_(func, n = 1000000):
	start = time.clock()
	func(n)
	stop =time.clock()
	return stop - start

if __name__ == "__main__":
	print(f"{'+ operator ':-<30}> {time_(func1) :.6f} sec")
	print(f"{' append ':-<30}> {time_(func2) :.6f} sec")
	print(f"{'list comp ':-<30}> {time_(func3) :.6f} sec")
	print(f"{'gen exp ':-<30}> {time_(func4) :.6f} sec")