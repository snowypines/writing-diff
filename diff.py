import difflib

d = difflib.Differ()

original = open("original.txt", "r")
original = original.read().splitlines()
edited = open("edited.txt", "r")
edited = edited.read().splitlines()

delta = open("delta.txt", "w")

i = 0

while i < len(original): 
  delta.write('Paragraph #' + str(i) + '\n')
  original_phrase = original[i].split('. ')
  edited_phrase = edited[i].split('. ')

  j = 0
  concise_diff = ''

  while j < len(original_phrase): 
    try:
      og_sent = original_phrase[j]
      ed_sent = edited_phrase[j]

      # print(og_sent)
      # print(ed_sent)

      if og_sent != ed_sent:
        diff = d.compare(og_sent.split(), ed_sent.split())
        for k in diff: 
          if not k.startswith(' ') and not k.startswith('?'):
            concise_diff += k + '\n'
        delta.write(''.join(concise_diff))
        delta.write('\n' + original_phrase[j] + '\n' + edited_phrase[j] + '\n\n')
        # print(original_phrase[j])
        # print(edited_phrase[j])
      j += 1
    except:
      j += 1

  if concise_diff == '':
    delta.write('No changes\n\n')
  i += 1
