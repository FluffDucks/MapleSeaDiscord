def format_content(message):
  # Replace italics (discord: *italics*; tele: _italics_ )
  message = format_italics(message)

  # Replace bolds (discord: **bold**)

  # Replace strikethroughs

  # No support for underline (yet)

  return message

def format_italics(message):
  new_message = message
  stack = []
  for idx in range(len(message)):
    c = message[idx]
    # TODO: escaped chars, need store prev char also
    if c == '*':
      if len(stack) > 0 and stack[-1][0] == '*':
        # match found
        idx_1 = stack.pop()[1] # smaller one in stack
        idx_2 = idx # larger one
        # Replace 
        new_message = new_message[:idx_1] + '_' + new_message[idx_1+1:idx_2] + '_' + new_message[idx_2+1:]
      else:
        # empty stack or not match, push into stack
        # tuple (char, index)
        stack.append((c, idx))
  return new_message