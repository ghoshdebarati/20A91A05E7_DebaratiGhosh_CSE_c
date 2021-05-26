Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input('enter the purchased amount'))
enter the purchased amount 1340
>>> if a>1000:
	print('the discount offered will be 10%')
	d1=0.1*a
	print('the reduction in price is ',d1)
	p1=a-d1
	print('the discounted price will be',p1)
elif a>2000:
	print('the discount offered will be 20%')
	d2=0.2*a
	print('the reduction in price is ',d2)
	p2=a-d2
	print('the discounted price will be',p2)
elif a>3000:
	print('the discount offered will be 30%')
	d3=0.3*a
	print('the reduction in price is ',d3)
	p3=a-d3
	print('the discounted price will be',p3)
elif a>5000:
	print('the discount offered will be 40%')
	d4=0.4*a
	print('the reduction in price is ',d4)
	p4=a-d4
	print('the discounted price will be',p4)
else:
	print('not eligible for discount')

	
the discount offered will be 10%
the reduction in price is  134.0
the discounted price will be 1206.0
>>> 