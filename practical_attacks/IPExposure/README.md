### IP Exposure PoC
According to our experiments, malicious Tensorflow model can expose victim's IP address to attacker.

To reproduce the IP Exposure PoC, you should follow these steps:

- prepare 2 different computers with linux OS, called A and B (here A is attacker and B is victim)
- replace `<attacker's IP address>` with IP address of computer A in `attack.py`.
- run `server_for_train.py` on computer A
- run `attack.py` on computer A and it will generate a malicious Tensorflow model locally at `./model/DebugIdentity/saved_model`
- copy the malicious Tensorflow model folder from computer A to computer B
- run `server_for_hack.py` on computer A, where IP address is the same with `<attacker's IP address>` you replace in `attack.py`
- while `server_for_hack.py` is running on A, run `model.py` to run the malicious model on computer B, and you will see A receive some TCP packages from B, so that A gets B's IP address.

We don't use any lambda layer to construct IP Exposure PoC.