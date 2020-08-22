import pyshorteners

urls=input("Paste the URL here\t")
print("\n click here or copy url \t",pyshorteners.Shortener().tinyurl.short(urls))