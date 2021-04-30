import serial
import Adafruit_SSD1306
import Adafruit_GPIO.SPI as SPI

from time import sleep
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

font = ImageFont.load_default()
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

def result(a):
    #The variables are declared
    x = 0 #Counter
    r = 0 #Result
    opcion = 0 #Flag
    while (a[x+1] != '=' and a[x].isdigit()): #Checks if an operation is needed
        
        if (a[x+1] != '=' and a[x+2].isdigit() and len(a)>2):
            
            if (opcion == 0): #Conditions for the first itteration
                n1 = float(a[x])
                n2 = float(a[x+2])
            else:            #Conditions for the other itterations
                n1 = 0
                n2 = float(a[x+2])
                
            if (a[x+1] == '+' and a[x].isdigit()): #Add operation
                if (opcion == 0): #Conditions for the first itteration
                    r = n1+n2
                else:             #Conditions for the other itterations
                    r += n1 + n2
                x += 2
            elif (a[x+1] == '-' and a[x].isdigit()):#Substract operation
                if (opcion == 0):
                    r = n1-n2
                else:
                    r -= n1 + n2
                x += 2
                
            elif (a[x+1] == '/' and a[x].isdigit() and n2 != 0): #Division operation
                if (opcion == 0):
                    r = n1/n2
                else:
                    r /= n1 + n2
                x += 2
                
            elif (a[x+1] == '*' and a[x].isdigit()): #Multiply operation
                if (opcion == 0):
                    r = n1*n2
                else:
                    r *= n1 + n2
                x += 2
            
            else: #Special cases
                r = 0
                x = 0
                opcion = 0
            opcion = 1
        
        elif (a[1] == ''): #If the operation does not exist
            return 0
            
        else: #Other special cases
            r = 0
            x = 0
            opcion = 0
    if (a[1] == '='): #If the operation is only a number
            return a[0]       
    return r
    
    

def main():
    #Defines the serial information
    ser =  serial.Serial('/dev/ttyUSB0',baudrate=9600, timeout=0.005)
    ser.flush()
    disp.begin()
    x=0
    cal = []
    tmp = ''
    
    while 1:
        if ser.in_waiting > 0:
            #take sarial data from Arduino
            line = ser.readline().decode('utf-8').rstrip()
            
            #Prints the operation on the display
            if line.isdigit() or line=='.': 
                tmp+= str(line)
                draw.text((x,5),      str(line),  font=font, fill=255)
                x += 7 #Takes into account the pixel size of the characters
            #Prints the result on the display
            elif line=='=':
                cal.append(tmp)
                cal.append('=')
                res = result(cal)
                j=0
                draw.text((x,5),   '=' ,  font=font, fill=255)
                draw.rectangle((0,0,128,64),outline=0,fill=0) #Clear the display
                for i in range (len(cal)): #Prints the vector on the display
                    draw.text((j,5),   str(cal[i]) ,  font=font, fill=255)
                    y=len(cal[i]) 
                    j+=7*y

                draw.text((90,45),   str(res) ,  font=font, fill=255)
                x=0
                print(cal)
                print(res)
                cal = [] #Errase the variables
                tmp= ''
                disp.display()
                
            else :
                cal.append(tmp)
                cal.append(str(line))
                tmp=''
                draw.text((x,5),str(line),  font=font, fill=255)
                x += 7

            # Display image
            disp.image(image)
            disp.display()

if __name__ == '__main__':
    main()