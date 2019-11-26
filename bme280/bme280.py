import time, datetime
import digitalio
import board
import busio
import adafruit_bme280
import json
import requests
import sys
import logging

api_url = "http://seed-it.eu:4000/sensor";
sending_timeout = 2; # timeout used to wait a certain amoun of time before returning the get/post of seed-IT API
time_between_record = 60 - sending_timeout; # minutes calculated in seconds (timeout taken into account)

# Log configuration
logger = logging.getLogger('bme280')
logger.setLevel(logging.INFO)
# create a file handler
handler = logging.FileHandler('bme280.log')
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
alice = logging.StreamHandler()
alice.setFormatter(formatter)
logger.addHandler(alice)

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
print('Welcome to Rose, the tracking device of Seed-IT')
print('===============================================')
logger.info('Please note Altitude is calculated based on pressure information.')
logger.info('Altitude will not be shown nor stored as it\'s not necessary for this app.')
logger.info('Start record of BME280 sensor')
print('-------------------')

# The sensor will need a moment to gather initial readings
time.sleep(1)

# ISO8601
## {"datetime": "2019-11-14T10:11:59.378308+01:00", "temperature": 22.69, "humidity": 37.33, "pressure": 986.74}
def get_date_time():
    return now.replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()

# JSON part
def sensor_to_json():
    # dict which will be used by JSON
    bob = {'datetime': get_date_time(), # date T time in ISO8601
            'temperature': float(f'{bme280.temperature:.1f}'), # in Celsius
            'humidity': float(f'{bme280.humidity:.1f}'), # in percentage
            'pressure': float(f'{bme280.pressure:.2f}')} # in hectopascal
    data_json = json.dumps(bob)
    logger.info('Records: %s', data_json)
    with open('bme280data.json', 'a') as f:
        f.write(data_json + "\n")
    return data_json

# Fail method whenever needed
def fail(msg):
    print(">>> Oops:",msg,file=sys.stderr)
    logger.warn('Oops: %s', msg)

def post_data():
    logger.info('Send data to seed-IT server via API')
    try:
        r = requests.post(api_url, data=data, timeout=sending_timeout)
        logger.info('Status code: %s - %s', str(r.status_code), r.json()['message'])
        if r.status_code in range(200,300):
            logger.info('Success')
        else:
            fail(str(r.status_code))
    except requests.exceptions.HTTPError as err:
        fail('HTTP error')
    except requests.exceptions.ConnectionError as errc:
        fail('Connection error')
    except requests.exceptions.Timeout as errt:
        # set up for a tmp file before next try
        fail('Timeout error')
    except request.exceptions.RequestException as e:
        # catastrophic error, you need to go to jail
        fail('Request error')

while True:
    try:
        now = datetime.datetime.now() # Get current date and time
        utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
        utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
        data = sensor_to_json()
        post_data()
        time.sleep(time_between_record)
    except (KeyboardInterrupt, SystemExit):
        logger.info('KeyboardInterrupt/SystemExit caught')
        sys.exit()

