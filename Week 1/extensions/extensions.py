file = input("File name: ")

file = file.strip().lower().split(".")

match file[-1]:
    case "gif" | "png":
        print(f"image/{file[-1]}")
    case "jpg" | "jpeg":
        print(f"image/jpeg")
    case "pdf" | "zip":
        print(f"application/{file[-1]}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
