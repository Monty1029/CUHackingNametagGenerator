from PIL import Image, ImageDraw, ImageFont
import sys

img = Image.open("nametag.jpg").convert('RGBA')

imgWidth, imgHeight = img.size

print("Enter 'exit' at any time to end program.")

while(1):

    name = raw_input("Enter name: ")
    if (name == "exit"):
        sys.exit()
    company = raw_input("Enter company: ")
    if (company == "exit"):
        sys.exit()

    nameFont = ImageFont.truetype("segoeuisb.ttf", 96)
    companyFont = ImageFont.truetype("segoeuisb.ttf", 48)
    draw = ImageDraw.Draw(img)

    nameWidth, nameTextHeight = nameFont.getsize(name)
    companyWidth, companyTextHeight = companyFont.getsize(company)

    draw.text(((imgWidth-nameWidth)/2, 400), name, (0,0,0), font=nameFont)
    draw.text(((imgWidth-companyWidth)/2, 560), company, (0,0,0), font=companyFont)

    img.save(name + ".png")
    print("Nametag created.")