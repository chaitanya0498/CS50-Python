text = input("Type the filename: ")
filename = text.lower().strip()

if ".txt" in filename:
    print("text/plain", end="")

elif ".jpg" in filename:
    print("image/jpeg", end="")

elif ".jpeg" in filename:
    print("image/jpeg", end="")

elif ".gif" in filename:
    print("image/gif", end="")

elif ".png" in filename:
    print("image/png", end="")

elif ".pdf" in filename:
    print("application/pdf", end="")

elif ".zip" in filename:
    print("application/zip", end="")

#elif s == "":
 #   print("Type the filename: ", end="")

else:
    print("application/octet-stream")
