
extension = input("File name: ")
extension = extension.lower().rstrip().lstrip()

def jformat():
    if extension.endswith(".jpg") or extension.endswith(".jpeg"):
            print("image/jpeg")
    elif extension.endswith(".png"):
            print("image/png")
    elif extension.endswith(".gif"):
            print("image/gif")
    elif extension.endswith(".pdf"):
            print("application/pdf")
    elif extension.endswith(".txt"):
            print("text/plain")
    elif extension.endswith("zip"):
            print("application/zip")
    elif extension.endswith(".py"):
            print("application/py")
    else:
            print("application/octet-stream")
jformat()




# match extension:
#     case extension.find(".jpg") | extension.find(".jpeg"):
#         print("image/jpeg")
#     case extension.find(".gif"):
#         print("image/gif")
#     case extension.find(".png"):
#         print("image/png")
#     case _:
#         print("application/octet-stream")
