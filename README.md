
![Header](Caesar-Cipher.png)

# Caesar Cipher
Imagine you're passing notes to your friend in class, but you don't want anyone else to understand what you're saying. One way to do this is by using a secret code called the Caesar Cipher, named after Julius Caesar, who is believed to have used it to send secret messages to his generals.

The Caesar Cipher is a very simple encryption technique where each letter in the message is replaced by a letter some fixed number of positions down the alphabet. For example, if you shift each letter in the message by three positions to the right, 'A' becomes 'D', 'B' becomes 'E', and so on.

- example 
```
plain text : You are the best
cipher txt : csy evi xli fiwx 
if shifted 4 characters to right 
```
- The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A → 0, B → 1, ..., Z → 25. Encryption of a letter x by a shift n can be described mathematically as
```
encryption(x) = (x + n) % 26
```
- Decryption is performed similarly,
```
decyption(x) = (x - n) % 26


## Show your support

You can give a ⭐️ if this project helped you !
