import board
import busio
import adafruit_tsl2591
import firebase_admin
from firebase_admin import credentials, db

# Initialize I2C bus and Adafruit TSL2591 sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c)

# Initialize Firebase with your service account JSON file
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-firebase-project-id.firebaseio.com/'
})

try:
    while True:
        # Read light levels
        lux = sensor.lux
        full, ir = sensor.full_luminous_flux, sensor.ir_luminous_flux
        
        print(f"Lux: {lux:.2f}")
        print(f"Full Spectrum: {full}")
        print(f"Infrared: {ir}")
        
        # Store light data in Firebase
        data = {
            'lux': lux,
            'full_spectrum': full,
            'infrared': ir
        }
        db.reference('/light_data').push(data)
        
except KeyboardInterrupt:
    pass
