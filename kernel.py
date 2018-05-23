import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import numpy

# Number of elements in array. Size set to 1,000,000
size = numpy.int32(2560)

# Equivalent to:
# creating an array of floats, of size and populating it with random numbers
# 'a' is your host side array
a = numpy.random.randn(1,size).astype(numpy.float32)

a_gpu = cuda.mem_alloc(a.nbytes)    # Equivalent to cudaMalloc. 'a_gpu' is your device side array

cuda.memcpy_htod(a_gpu,a) # equivalent to cudaMemCpy host to device

# Your CUDA kernel
mod = SourceModule("""
        __global__ void twice(float *a, int numElements){
        
        int idx = threadIdx.x + blockDim.x * blockIdx.x;
        if(idx < numElements){
          a[idx] = a[idx] * 2; 
        }
        }
      """)

# Equivalent to twice<<< >>>(a_gpu, size)
grid = (10, 1)
block = (256,1,1)
func = mod.get_function("twice")
func(a_gpu, size, grid = (10,1), block=(256,1,1))

a_doubled = numpy.empty_like(a)
cuda.memcpy_dtoh(a_doubled, a_gpu)

print ("Original Array")
print (a)
print ("Doubled Array")
print (a_doubled)
