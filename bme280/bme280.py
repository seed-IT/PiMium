import time, datetime
import digitalio
import board
import busio
import adafruit_bme280
import json
import sys

# Create library object using Bus I2C port
#i2c = busio.I2C(board.SCL, board.SDA)
#bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# OR create library object using Bus SPI port
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
bme_cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# Change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25
bme280.mode = adafruit_bme280.MODE_NORMAL
bme280.standby_period = adafruit_bme280.STANDBY_TC_500
bme280.iir_filter = adafruit_bme280.IIR_FILTER_X16
bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X2

# Clear terminal before starting everything
print(chr(27) + "[2J")
print('Please note Altitude is calculated based on pressure information.')
print('Altitude will not be shown nor stored as it\'s not necessary for this app.')
print('Starting record of BME280 sensor...')
print('===================================')

# The sensor will need a moment to gather initial readings
time.sleep(1)

# ISO8601
def get_date_time():
    now.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

# Terminal viewer
def display():
    print(f'\n{now.strftime("%Y-%m-%d T %H:%M:%S")}')
    print(f'Temperature: {bme280.temperature:.1f} °C')
    print(f'Humidity: {bme280.humidity:.2f} %')
    print(f'Pressure: {bme280.pressure:.2f} hPa')

# JSON part
def sensor_to_json():
    # dict which will be used by JSON
    bob = {'datetime': now.replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat(), # date T time in ISO8601
            'temperature': float(f'{bme280.temperature:.2f}'), # in Celsius
            'humidity': float(f'{bme280.humidity:.2f}'), # in percentage
            'pressure': float(f'{bme280.pressure:.2f}')} # in hectopascal
    data_json = json.dumps(bob)
    with open('bme280data.json', 'a') as f:
            f.write(data_json + "\n")
    return;

while True:
    try:
        now = datetime.datetime.now() # Get current date and time
        utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
        utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
        display();
        sensor_to_json();
        time.sleep(300) # 5 minutes
    except (KeyboardInterrupt, SystemExit):
        print("KeyboardInterrupt has been caught. Stopping BME280 app...")
        sys.exit()

