import nidaqmx
import numpy as np
import csv
import time

# File to store the data
output_file = "capstone_data.csv"

# Create or overwrite the CSV file with a header
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp (s)", "Voltage ai6 (V)", "Voltage ai0 (V)"])

# DAQ task setup
with nidaqmx.Task() as task:
    # Add analog input voltage channels
    task.ai_channels.add_ai_voltage_chan("Dev1/ai6")
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(rate=50.0, 
                                    sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS, 
                                    samps_per_chan=10)
    task.in_stream.input_buf_size = 100000

    try: 
        task.start()
        print("Acquiring data... Press Ctrl+C to stop.")
        start_time = time.time()  # Record the start time

        while True: 
            # Read data
            data = task.read(number_of_samples_per_channel=100)
            voltage_array = np.array(data)
            channel6 = voltage_array[0]
            channel0 = voltage_array[1]

            # Add timestamps for each sample
            current_time = time.time()
            elapsed_time = current_time - start_time
            timestamps = np.linspace(elapsed_time, elapsed_time + len(channel6) / 50.0, len(channel6))

            # Write data to the CSV file
            with open(output_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(zip(timestamps, channel6, channel0))

    except KeyboardInterrupt:
        print("Acquisition stopped.")
    finally:
        task.stop()