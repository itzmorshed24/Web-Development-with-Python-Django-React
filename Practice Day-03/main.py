#Variables & Data Types
#১। দুটি সংখ্যা যোগ করে প্রিন্ট করুন।
choporAndFid = 105
muri = 40
ghash = 30
paper = 220
todayTotalCost = choporAndFid + muri + ghash + paper
print("Today Total Cost:", todayTotalCost)

#২। একটি স্ট্রিং এবং একটি নাম্বার যোগ করার আগে টাইপ চেক করুন।
name = 'My age is'
number = 22
print("Type of Name:", type(name))
print("Type of Number:", type(number))
title = name + " " + str(number)
print(title)

#৪। এমন একটি সেট (set) তৈরি করুন যেখানে একই উপাদান একাধিকবার রাখা যাবে না।
fruits = {"Apple", "Banana", "Jackfruits", "Orange", "Apple", "Banana"}
print("Don't Show Double Element:", fruits)

#String Operation
#১। একটি স্ট্রিংয়ের ২য় অক্ষর প্রিন্ট করুন।
className = "Eleven"
print("Second Element is:", className[1])

#২। স্ট্রিংয়ের প্রথম ৫টি অক্ষর দেখান।
fatehrName = "Khairul Islam"
print(len(fatehrName))
print("First 5 Letter is:", fatehrName[:5])

#৩। স্ট্রিংটি উল্টা করে প্রিন্ট করুন।
motherName = "Moriom Begum"
reverse_text = motherName[::-1]
print(reverse_text)

#৪। .lower(), .upper(), .replace(), এবং .split() মেথডগুলো ব্যবহার করে দেখান।
text = "Hello Python World!"
print(text.lower())
print(text.upper())
print(text.replace('Python', 'Java'))
print(text.split())


