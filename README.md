# se20uari039_se20uari133_se20uari111_se20uari177

# Team Members

- **se20uari039** = **Nagapranav chakilam**
- **se20uari133** = **Saketh kumar Noothi**
- **se20uari111** = **Nithin reddy Noothi**
- **se20uari177** = **Vijay Vardhan Nomula**

# Hardware Requirements

-Connect your Adafruit TSL2591 sensor to your Raspberry Pi. The sensor typically uses the I2C interface, so you'll need to connect the SDA and SCL pins.

- SDA to the Raspberry Pi's GPIO2 (BCM pin 2)
- SCL to the Raspberry Pi's GPIO3 (BCM pin 3)
- Connect VCC and GND to the respective power and ground pins.

# AdafruitTSL2591

- The Adafruit TSL2591 sensor is a light-to-digital converter that can measure both visible and infrared (IR) light intensity. It is particularly useful for measuring ambient light levels and lux values

# Brief explanation of code

- **Importing Libraries**: You start by importing the necessary libraries:

 - board and busio: These are used for setting up the I2C communication with the TSL2591 sensor.
 - adafruit_tsl2591: This library allows you to interface with the TSL2591 sensor.
 - firebase_admin and credentials: These are used for integrating Firebase with your Python script.
  **Initializing I2C and Sensor**: You initialize the I2C bus and create an Adafruit TSL2591 sensor object. This sets up the hardware communication to read data from the light sensor.

- **Firebase Initialization**: You initialize Firebase using our service account JSON file and provide the Firebase Realtime Database URL.

- **Data Collection Loop** : Inside a while loop, you continuously collect data from the light sensor.

 - lux = sensor.lux retrieves the light intensity in lux.
 - full and ir capture the full spectrum and infrared light intensities.
 - You print these values to the console for real-time monitoring.
- **Firebase Data Storage**: You create a dictionary named data containing the light intensity values.
 - db.reference('/light_data').push(data) pushes this data to the Firebase Realtime Database under the /light_data node.
  Keyboard Interrupt Handling: The code includes a try block to handle a KeyboardInterrupt (Ctrl+C), which allows you to gracefully exit the script when you want to stop data collection.

# Uses of AdafruitTSL2591

**Environmental Sensing**: Monitoring light levels in a room, greenhouse, or outdoor environment to control lighting systems or to gather data on natural light conditions.

**Display Brightness Control**: Adjusting the brightness of displays (e.g., LCD or LED screens) based on ambient light conditions to save power and improve user experience.

**Photography**: Automatically adjusting camera settings like shutter speed and ISO to capture well-exposed photos in changing lighting conditions.

**Energy Efficiency**: Optimizing energy usage in smart homes or buildings by adjusting lighting and HVAC systems based on the available natural light.

# Roles
- **Nagapranav chakilam** - Gathered info on project and sources to look upto and a part of code making
- **Saketh kumar noothi** - As part of python coder
- **Vijay vardhan nomula** - Helped in searching and briefed about rasberry pi 
- **Noothi nithin reddy** -  As part of python coder
