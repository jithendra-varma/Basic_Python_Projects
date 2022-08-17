import qrcode
import cv2

def Basic_QR_Code(data, image_name):
    img = qrcode.make(data)
    img_name = image_name+".png"
    img.save(img_name)

def Advance_QR_Code(v,ec,bs,br,fc,bc,data,image_name):
    qr = qrcode.QRCode(version = v, error_correction = ec, box_size = bs, border = br )
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = fc, back_color = bc)
    img_name = image_name+".png"
    img.save(img_name)

print("Select option : '0' for Basic QR Code (or) '1' for Advanced QR Code (or) '2' for Reading QR Code ")
option = int(input("Enter your chosen option : "))
if option == 0:
    print("enter the data and img name where the qr code shoulb be stored")
    data = input("Enter the data : ")
    image_name = input("img name : ")
    Basic_QR_Code(data, image_name)

elif option == 1:
    print("version parameter is an integer from 1 to 40 that controls the size of the QR Code")
    version = int(input("version : "))
    ec = [qrcode.constants.ERROR_CORRECT_L, qrcode.constants.ERROR_CORRECT_M, qrcode.constants.ERROR_CORRECT_Q, qrcode.constants.ERROR_CORRECT_H]
    print("error correction parameter is an integer from 1 to 4 that controls the errors under the provided rate")
    v = int(input("error correction : "))
    error_correction = ec[v+1]
    print("box_size parameter controls how many pixels each “box” of the QR code is. eg: 10")
    box_size = int(input("box_size : "))
    print("border parameter controls how many boxes thick the border should be. eg: 4")
    border = int(input("border : "))
    print("fill_color parameter takes the code color like black, blue or (R,G,B)")
    fill_color = input("fill_color : ")
    print("back_color parameter takes the background color of the qr code like white, grey or (R,G,B)")
    back_color = input("back_color : ")
    print("Finally enter the data and img name where the qr code shoulb be stored")
    data = input("data : ")
    file_name = input("img name : ")
    Advance_QR_Code(version,error_correction,box_size,border,fill_color,back_color,data,file_name)

elif option == 2:
    img_name = input("Enter the QR Code image file name : ")
    img = cv2.imread(img_name)
    detector = cv2.QRCodeDetector()
    data, vertices, binary_data = detector.detectAndDecode(img)
    print(data)