states: [s, q0, q1, q2, q3, q4, q5, add1, dup0, dup1, mark0, find_end0, write0, back0, cleanup0, mark1, find_end1, write1, back1, cleanup1, qA, qR]
input_alphabet: [$, 1, 0]
tape_alphabet_extra: [x, 8]
start_state: s
accept_state: qA
reject_state: qR

delta:

  s:
    $: [q0, $, R]
  q0:
    x: [q0, x, R]
    1: [q1, x, R]
    0: [q2, x, R]
    8: [q3, _, R]
  q1:
    0: [q1, 0, R]
    1: [q1, 1, R]
    _: [dup1, 8, R]
    8: [dup1, x, R]
    x: [q1, x, R]
  q2:
    0: [q2, 0, R]
    1: [q2, 1, R]
    8: [dup0, x, R]
    x: [q2, x, R]
  q3:
    1: [qA, 1, S]
    x: [q3, x, R]
    _: [q3, _, R]
    




  dup0:
    1: [mark0, x, R]
    x: [dup0, x, R]
    _: [dup0, _, R]
    8: [cleanup0, 8, L]
  mark0:
    1: [mark0, 1, R]
    x: [mark0, x, R]
    _: [find_end0, _, R]
    8: [find_end0, 8, R]
  find_end0:
    1: [find_end0, 1, R]
    _: [write0, 1, R]
  write0:
    _: [back0, 1, L]
  back0:
    1: [back0, 1, L]
    x: [q5, x, L]
    8: [q5, 8, L]
    _: [back0, 8, S]
  cleanup0:
    x: [cleanup0, x, L]
    _: [cleanup0, _, L]
    1: [cleanup0, 1, L]
    0: [cleanup0, 0, L]
    $: [q0, $, R]
  q5:
    x: [dup0, x, S]
    1: [q5, 1, L]

  dup1:
    1: [mark1, x, R]
    x: [dup1, x, R]
    8: [add1, 8, R]
    _: [cleanup1, 1, L]
  mark1:
    1: [mark1, 1, R]
    x: [mark1, x, R]
    _: [find_end1, _, R]
    8: [find_end1, 8, R]
  find_end1:
    1: [find_end1, 1, R]
    _: [write1, 1, R]
  write1:
    _: [back1, 1, L]
  back1:
    1: [back1, 1, L]
    x: [q4, x, L]
    _: [back1, 8, S]
    8: [q4, 8, L]
  cleanup1:
    x: [cleanup1, x, L]
    _: [cleanup1, _, L]
    1: [cleanup1, 1, L]
    0: [cleanup1, 0, L]
    8: [cleanup1, 8, L]
    $: [q0, $, R]
  q4:
    x: [dup1, x, S]
    1: [q4, 1, L]
  add1:
    _: [cleanup1, 1, L]
    1: [add1, 1, R]
  

