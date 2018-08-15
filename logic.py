arr=[10,20,30,40,30,50,10,10,30,46,13,12,10,17,12,12,13,14,19,19,19,19,19,19,19,19] #Cost of Crytocoin WRT time
temp=[] #To hold the rise and fall WRT init_money
i_flag=False #Toggle to toggle strategies, ((True=> Invest & False=> Sale))
#i,cur_idx
gain_factor=1 #Times of Gain requested
gain_factor_for_sale=0.25
init_money=20
cur_idx=2 #assumption for example, in real cur_date can be used

#LET LIST TEMP HOLD PREDICTED VALUES OF UPCOMING WEEK - INIT_MONEY

#INVEST STRATEGY
if i_flag: #Checks for wise investment : Will wait for Jackpot-Week
	for i in range(7): #prediction for 1 week
		temp.append(arr[cur_idx+i+1]-init_money) #gain\loss calc
	if max(temp)>gain_factor*init_money:
		print("Gain on : {}th day".format(temp.index(max(temp))+1))
	else:
		print("Wait till next week")

#SALE STRATEGY
if not(i_flag): #Checks for Sale : Will locate if market will fall in future
	for i in range(7): #prediction for 1 week
		temp.append(arr[cur_idx+i+1]-init_money) #gain\loss calc
	avg=sum(temp)/float(len(temp))
	print(avg)
	if avg<gain_factor_for_sale*init_money*-1:
		print("Sale")
	else:
		print("wait next week")


