from bs4 import BeautifulSoup
import os 
import pandas as pd

def AliexpressScrapping():
    d={"Namee":[],"Price":[],"StorLink":[],"StoreNames":[]}
    try:
        for file in os.listdir("data"):
            with open(f"Aliexpress/{file}") as f:
                html_doc=f.read()
                soup = BeautifulSoup(html_doc, 'html.parser')
                name=soup.find("h3")
                Fetch_name=name.get_text()
                d["Name"].append(Fetch_name)
                price=soup.find("div",attrs={"class":"multi--price-sale--U-S0jtj"})
                Fetch_price=price.get_text()
                d["Price"].append(Fetch_price)
                l=soup.find("a",attrs={"class":"cards--storeLink--XkKUQFS"})
                link=l["href"]
                d["StoreLink"].append(link)
                storename=soup.find("a",attrs={"class":"cards--storeLink--XkKUQFS"})
                Fetch_storename=storename.get_text()
                d["StoreNames"].append(Fetch_storename)


    except Exception as e:
        print("file is empty")

    df=pd.DataFrame(d)
    df.set_index("Name", inplace=True)
    df["Price"]=df["Price"].str.replace("PKR","")
    df["Price"]=df["Price"].str.replace(",","").astype(float)
    df.to_csv("Aliexpress_Data.csv")
