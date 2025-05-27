### LeakFile PoC
According to our experiments, malicious Tensorflow model can steal important file contents from victim, and transfer the file contents to attacker.

To reproduce the LeakFile PoC, you should follow these steps:

- prepare 2 different computers with linux OS, called A and B (here A is attacker and B is victim)
- replace `<attacker's IP address>` with IP address of computer A in `attack.py`.
- run `attack.py` on computer A and it will generate a malicious Tensorflow model locally at `./model/LeakFile/saved_model`
- copy the malicious Tensorflow model folder from computer A to computer B
- run `server.py` on computer A, where IP address is the same with `<attacker's IP address>` you replace in `attack.py`
- while `server.py` is running on A, run `model.py` to run the malicious model on computer B, and you will see A receive some important file contents from B.

We don't use any lambda layer to construct LeakFile PoC.