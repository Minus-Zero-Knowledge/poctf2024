# Reverse 300-3 - Beef-Witted Mushrumps
## Description
For this challenge, I wanted to do something in the vein of simplified memory operations in a simulated virtual machine, and I ended up with this. The binary here takes in custom bytecode, executes it, and prints the output. It won't look like much if you run it, but that doesn't matter for this type of challenge.

The thing about memory operations in VMs is that the memory manager is in the middle of everything. Operations on the guest side are limited in favor of host-controlled VMM. So on the guest side, like this code, operations are performed in discrete data, then sequentially processed. Essentially, operations are distributed. That is what is being done here. This code represents the operation for a single byte. Extrapolate based on that, and write your own VMM,

Right Click, Save As... [Reverse300-3](https://pointeroverflowctf.com/static/Reverse300-3)

MD5 checksum c622aedabec6f2bfed7aab7ef25bd4da

## Solution
The VM decodes the flag by xor-ing adjacent bytes.

## Flag
`poctf{uwsp_7h3_g4m3_15_4f007}`
