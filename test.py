import tensorflow as tf

# List all physical GPUs
physical_gpus = tf.config.list_physical_devices('GPU')
print(f"Number of GPUs available: {len(physical_gpus)}")

# Detailed GPU information
for i, gpu in enumerate(physical_gpus):
    print(f"GPU {i}: {gpu}")
