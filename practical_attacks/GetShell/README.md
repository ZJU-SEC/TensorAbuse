### Get Shell PoC
According to our experiments, malicious Tensorflow model can help attacker GET SHELL from victim. This is very dangerous.

To reproduce the Get Shell PoC, you should follow these steps:

- prepare 2 different computers with linux OS, called A and B (here A is attacker and B is victim)
- replace `<attacker's IP address>` with IP address of computer A in `attack.py`.
- run `attack.py` on computer A and it will generate a malicious Tensorflow model locally at `./model/GetShell/saved_model`
    - PS: You SHOULD make your `~/.ssh/authorized_keys` a backup, because running `attack.py` may edit this file
- copy the malicious Tensorflow model folder from computer A to computer B
- run `server_for_hack.py` on computer A, where IP address is the same with `<attacker's IP address>` you replace in `attack.py`
- while `server_for_hack.py` is running on A, run `model.py` to run the malicious model on computer B, and you will see A gets B's Shell.

We don't use any lambda layer to construct Get SHELL PoC. To ensure that the PoC can be reproduce, computer B (the victim computer) should better to have only one username under `/home` directory.