a="basith"#b=0,a=1,s=2,i=3,t=4,h=5(Neg=h=-1,t=-2,i=-3,s=-4,a=-5,b=-6)
print(a[0:2]) # inlcude o exclude 2
print(a[-3:-1]) #include -3 and exclude -1
print(a[3:5]) #converted the above negative in to positive which gives same output
print(a[:2]) # This is same as this print(a[0:2]) which by default takes the value of 0
print(a[1:6]) # This starts from a and completes till the end
print(a[1:]) #This is same as print(a[1:6])

#To find te length of the string use 'len'

a="shaik"
print(len(a))
#the length of string starts with "1"


#Slicing with skip value
a="shaik" #start wthe indices with '0'
print(a[0:2:3]) #0:2 will be sh and slice every 3rd part , Among 'sh' theres no 3rd part so 's'

a="shaikabdulbasith"
print(a[2:8:3])

a="0123456789"
print(a[1:6:2])