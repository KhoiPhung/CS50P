file_name = input("File name: ")

#check whether the input has . or not

if "." in file_name:
#split the file name using .
    name, extension = file_name.split(".")

    if extension:
        match extension:
            case "jpeg" | "jpg":
                print("image/jpeg")
            case "pdf":
                print("application/pdf")
            case "gif":
                print("image/gif")
            case "png":
                print("image/png")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _:
                print("application/octet-stream")
    else:
        print("application/octet-stream")

else:
    print("application/octet-stream")

