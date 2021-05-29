def format_content(message):
  # Replace italics (discord: *italics* / _italics_; tele: _italics_ )
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
*****words***** -> ****_words_****

**words** -> **words**
****words**** -> ****words****
"""
def format_italics(message):
  new_message = message
  stack = []
  for idx in range(len(message)):
    c = message[idx]
    # TODO: escaped chars, need store prev char also
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

# By this point, italics would have been formatted and remaining asterisk pairs should be
# converted to single asterisks
def format_bolds(message):
  new_message = message
   
  # While loop to account for multiple asterisks ****hi**** -> *hi*
  while '**' in new_message:
    new_message = new_message.replace('**', '*')

  # Handling italicised + bolded words:
  # MarkdownV1 that we use in telegram does not support nested formats
  # So, at this point, italicised + bolded words would be like *_some words_* to
  # which tele would end up rendering as '_some words_', BOLDED.
  # In this case, we will reduce italicised + bolded words to just italicised words.
  new_message = new_message.replace('*_', '_') # open side
  new_message = new_message.replace('_*', '_') # close side

  return new_message