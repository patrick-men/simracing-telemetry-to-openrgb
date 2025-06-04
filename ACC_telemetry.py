# from pyaccsharedmemory import accSharedMemory
#
# asm = accSharedMemory()
# sm = asm.read_shared_memory()
#
# if (sm is not None):
#     print("Physics:")
#     print(f"Pad life: {sm.Physics.pad_life}")
#
#     print("Graphics:")
#     print(f"Strategy tyre set: {sm.Graphics.penalty.name}")
#
#     print("Static: ")
#     print(f"Max RPM: {sm.Static.max_rpm}")
#
# asm.close()

from multiprocessing import shared_memory
import numpy as np

# Use the shared memory name printed by writer
shm = shared_memory.SharedMemory(name='$rFactor2SMMP_Telemetry$')  # replace with actual name

# Create numpy array backed by shared memory
shm_array = np.ndarray((4,), dtype='int32', buffer=shm.buf)
print("Read from shared memory:", shm_array[:])

# Clean up
shm.close()