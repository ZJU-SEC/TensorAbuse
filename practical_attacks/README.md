# Security Vulnerability Report

Dear Google team, hello there! We have discovered a security vulnerability in the Tensorflow framework model, and this vulnerability may cause danger to the users of Kaggle. The attack scenario is that, any regular user can upload a malicious Tensorflow model (.pb file in SavedModel format) on Kaggle, other regular Kaggle users will be attacked after downloading and running these malicious Tensorflow model. In the worst case, the attacker can obtain the victim's Shell.

We found that by maliciously constructing keras models, four kinds attacks of different risks can be caused to model users, they are:

1. The attacker can obtain the IP address of the model user

2. The attacker can steal the local sensitive files from the model user

3. The attacker can execute arbitrary code on the computer of the model user

4. The attacker can get the SHELL of the model user

For each of these 4 kinds of malicious Tensorflow models, we provide one folder with one PoC video and corresponding source code to reproduce.

It’s known that Goole and Kaggle are very concerned about the security of the pretrained models uploaded by users, which is far ahead of many Model Hub websites. Our team has found that Tensorflow pretrained models (SavedModel format .pb files) may also face situations similar to pickles ( it is well-known that pickle-format model is easy to exploit ). As cybersecurity researchers, we strongly recommend the implementation of a comprehensive review mechanism for Tensorflow models. By detecting the API abuse cases, we can minimize the associated risks and uphold the platform's reputation for security and reliability.

We are eager to hear your perspective on these findings and to discuss potential strategies for mitigating these security risks. If you require further information or assistance, please feel free to reach out to me. Your proactive approach to addressing these concerns would be greatly appreciated by the entire community of Kaggle users.

Attached is the source code and related details for reproducing the above 4 kinds of security attacks. Looking forward to your reply!