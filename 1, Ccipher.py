def ceaser(text, shift_amount, direction):
  if shift_amount > 26:
    shift_amount = shift_amount % 26
  if direction == "encode":
    cipher_text = " "
    plain_text = text
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
  elif direction == "decode":
    plain_text = ""
    cipher_text = text
    for letter in cipher_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")
  
my_flag = True
while(my_flag):   
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  ceaser(text,shift_amount = shift, direction = direction)

  my_choice = input("Do you want to play again? yes or no?")
  if my_choice == "no":
    my_flag = False
