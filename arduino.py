import serial
import sys
import time

# constante multiplicativa para obter a quantidade em segundos a partir de ml
const_ml_to_ms=0.4155

# calcula a percentagem total de tinta
def cmyk_total_percent(cyan_code,magenta_code,yellow_code,black_code):
    percent_total=cyan_code+magenta_code+yellow_code+black_code
    return float(percent_total)

# quantidade em ml e igual a porcentagem parcial (de cada tinta) * 100
# dividido pela porcentagem total (soma de todas as tintas)
def cmyk_to_ml(percent_of_color,percent_total):
    color_in_ml=(100*float(percent_of_color))/float(percent_total)
    return int(color_in_ml)

# milliliter_to_milliseconds
def ml_to_ms(qt_ml):
    time=qt_ml*const_ml_to_ms*1000
    # tempo em milisegundos para ligar a bomba
    return int(time)

def send_color(base,cyan,magenta,yellow,black):
    #import ipdb; ipdb.set_trace()
    ser = serial.Serial(port='/dev/ttyACM1', baudrate=9600)
    time.sleep(1)
    data = "{},{},{},{},{}\n".format(str(base),str(cyan),str(magenta),str(yellow),str(black))
    # data = "2000,2000,2000,2000,2000\n"
    print(data)
    ser.write(data)
    time.sleep(2)
    output = ''
    while not "finish" in output:
        output = str(ser.readline())
        print 'output:' + output
    ser.close()

def main(base_code,cyan_code,magenta_code,yellow_code,black_code):
    # percentagem total das cores
    percent_total=cmyk_total_percent(cyan_code,magenta_code,yellow_code,black_code)
    # define todas as cores
    base=ml_to_ms(cmyk_to_ml(base_code,percent_total))
    cyan=ml_to_ms(cmyk_to_ml(cyan_code,percent_total))
    magenta=ml_to_ms(cmyk_to_ml(magenta_code,percent_total))
    yellow=ml_to_ms(cmyk_to_ml(yellow_code,percent_total))
    black=ml_to_ms(cmyk_to_ml(black_code,percent_total))
    # envia as cores em milisegundos para o arduino
    send_color(base,cyan,magenta,yellow,black)

if __name__ == '__main__':
    main(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
