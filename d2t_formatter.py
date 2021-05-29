def format_content(message):
  # Replace italics (discord: *italics*; tele: _italics_ )
  message = format_italics(message)

  # Replace bolds (discord: **bold**; tele: *bold*)
  message = format_bolds(message)

  # Replace strikethroughs

  # No support for underline (yet)

  return message


"""
Basic cases: 
*words* -> _words_

Edge cases:
***words*** -> **_words_**
**words** -> **words**
"""
def format_italics(message):
  new_message = message
  stack = []
  for idx in range(len(message)):
    c = message[idx]
    # TODO: escaped chars, need store prev char also
    # TODO: Nested formatting - stick with bold or italic?
    # When an asterisk is found
    if c == '*':
      if len(stack) > 0 and stack[-1][0] == '*' and (idx - stack[-1][1]) > 1:
        # (inner-most) match found (cannot be adjacent to c)
        idx_1 = stack.pop()[1] # smaller one in stack
        idx_2 = idx # larger one
        # Replace 
        new_message = new_message[:idx_1] + '_' + new_message[idx_1+1:idx_2] + '_' + new_message[idx_2+1:]
      elif len(stack) > 0 and stack[-1][0] == '*' and (idx - stack[-1][1]) <= 1:
        # Match found but its not the inner-most / no words in between, remove pair from being reformatted
        stack.pop()
        continue
      else:
        # empty stack or top of stack does not match, push c into stack
        # tuple (char, index)
        stack.append((c, idx))
  return new_message

def format_bolds(message):
  return message