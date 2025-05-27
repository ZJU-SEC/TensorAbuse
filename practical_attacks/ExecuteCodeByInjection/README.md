### Code Execution PoC
According to our experiments, malicious Tensorflow model can execute malicious code on victim's computer by a 2-click attack.

To reproduce the Code Execution PoC, you should follow these steps:

- prepare 1 computer with linux OS, called A (here A is the victim)
- run `attack.py` on computer A and it will generate a `tensorflow.py` with malicious code embeded in it under the local directory
- delete `tensorlfow.py`, now we can imagine the situation that A downloads a malicious model to be a victim
- run `model.py` on computer A, now A is a victim. And `model.py` will generate a `tensorflow.py`, DON'T delete it.
- run `model.py` to load malicious model locally for the second time, and malicious code will be triggered.

We don't use any lambda layer to construct Code Execution PoC.