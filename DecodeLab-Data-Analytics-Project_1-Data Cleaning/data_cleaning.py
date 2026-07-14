import pandas as pd
df = pd.read_excel("Dataset.xlsx")
print(df.head())

print(df.isnull().sum())                                      #Returns the no of empty clms under each row 

df.dropna(axis= 1 , how= 'all', inplace=True)                 #removes the completely empty clm
df.to_excel("Dataset.xlsx", index= False)                     #saves the changes to excel file
print(df)  

print("Duplicate Rows:", df.duplicated().sum())               #checks for the no of duplicate rows

print("Duplicate Date:", df["OrderID"].duplicated().sum())        #checks for the no of duplicate values under the specific clm 

df.drop_duplicates(inplace=True)
df.to_excel("Dataset.xlsx", index= False)                      #removes duplicate rows
print(df)

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")       #Fills Nan values
df.to_excel("Dataset.xlsx", index= False) 
print(df)

df["Product"] = df["Product"].str.strip().str.title()         #Data Cleaning fomatting
df.to_excel("Dataset.xlsx", index= False)

df["Date"] = pd.to_datetime(df["Date"])                      #coverts the date clm to datetime format
df["Date"] = df["Date"].dt.strftime("%d-%b-%Y")              #Date formatting 
df.to_excel("Dataset.xlsx", index= False)
print(df)

#Saves the cleaned file
print("Data Cleaning Completed Successfully!")


























