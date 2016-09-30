def minimum(a):
	min1 = a[0]
	for i in range(len(a)):
		if a[i]< min1:
			min1 = a[i];
	return min1
		
def arif(a):
	f = 0;
	for i in range(len(a)):
			f=f+a[i]
	f = f/len(a)
	return f
	
ivan = {
"name" : "ivan",
"age":34,
	"children":[{
	"name":"vasja",
	"age":12,
	},{
	"name":"petja",
	"age":10,
	}],
	}
darja={
"name":"darja",
"age":41,
	"children":[{
	"name":"kirill",
	"age":18,
	},{
	"name" : "pavel",
	"age" : 14,
	}],
}
stas={
"name":"stas",
"age":41,
	"children":[{
	"name":"stas",
	"age":28,
	},{
	"name" : "pavel",
	"age" : 24,
	}],
}
emps = [ivan, darja,stas]
def d(emps):
		result =[ ]
		for key in range(len (emps)):
			k = False
			mas = emps[key]["children"]
			for key1 in range (len(mas)):
					if mas[key1]["age"]>18:
						k = True
			if (k==True):
				result.append(emps[key]["name"])
		return result
		
a = [167,2134,44,2,4,56,34,34,513,113]
str1 =  "Vladimir Burashnikov"
print(minimum(a))
print(arif(a))
print(str1[::-1])
print(d(emps))
