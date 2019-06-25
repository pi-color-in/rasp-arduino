import serial

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)

# constante multiplicativa para obter a quantidade em segundos
const=0.4155

# def cmyk_to_ml(cyan,magenta,yellow,black):

# milliliter_to_milliseconds
def ml_to_ms(qt_ml):
    # tempo em milisegundos para ligar a bomba
    time=qt_ml*const*1000
    return int(time)

def send_color(base,cyan,magenta,yellow,black):
    data = "{},{},{},{},{}\n".format(str(base),str(cyan),str(magenta),str(yellow),str(black))
    print(data)
    ser.write(data)
    output = ''
    while not "finish" in output:
        output = str(ser.readline())
        print 'output:' + output
        ser.close()

def main():
    cyan=10
    magenta=10
    yellow=10
    black=10
    base=15
    send_color(ml_to_ms(base),ml_to_ms(cyan),ml_to_ms(magenta),ml_to_ms(yellow),ml_to_ms(black))

if __name__ == '__main__':
    main()
