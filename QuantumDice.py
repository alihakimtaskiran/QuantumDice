from qiskit import Aer, QuantumCircuit, execute
qd=QuantumCircuit(3,3)
for i in range(3):
    qd.h(0)
    qd.measure(0,i)
qc=Aer.get_backend("statevector_simulator")
def roll_dice():
    r=tuple(execute(qd,qc).result().get_counts())[0][::-1]
    val=0
    for i in range(3):
        val+=int(r[i])*2**i
    if val not in (1,2,3,4,5,6):
        val=roll_dice()
    return val
while True:
	input("Press enter to roll Quantum-Dice")
	print(roll_dice())
