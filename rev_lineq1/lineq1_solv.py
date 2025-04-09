# Fichier Lineq1

from z3 import *


local_148 = [BitVec(f'local_148[{i}]', 8) for i in range(128)]

solver = Solver()

# Première condition
solver.add((local_148[0x14] ^ 0x40) * 0xec +
          (local_148[0x15] ^ 64) * -0x84 +
          (local_148[0xe] ^ 0x40) * -0x79 + (local_148[0x16] ^ 0x40) * -0x1a
          + (local_148[0x15] ^ 64) * -0x40 == -0xca9)

solver.add((local_148[5] ^ 0x6b) * 0xc + (local_148[6] ^ 0x6b) * 0x59 +
            (local_148[8] ^ 0x6b) * 0xdc + (local_148[0x11] ^ 0x6b) * -0x4a
            + (local_148[0xf] ^ 0x6b) * 0xa2 == 0x5ae1)

solver.add((local_148[9] ^ 0xf7) * -0x60 +
              (local_148[0x1e] ^ 0xf7) * -0xc1 +
              (local_148[5] ^ 0xf7) * -0xea + (local_148[0xe] ^ 0xf7) * 199
              + (local_148[0x1b] ^ 0xf7) * 0xbf == -0x5912)
solver.add((local_148[0xc] ^ 0x6e) * 0x25 +
                (local_148[0xb] ^ 0x6e) * -0x80 +
                (local_148[5] ^ 0x6e) * 0x88 + (local_148[7] ^ 0x6e) * 0x6a
                == 0x5010)
solver.add((local_148[4] ^ 0x24) * -0x7b +
                  (local_148[0x1c] ^ 0x24) * 0xd7 +
                  (local_148[0xc] ^ 0x24) * -0xfa +
                  (local_148[0xb] ^ 0x24) * 0xf7 +
                  (local_148[0xd] ^ 0x24) * -4 == 0x3909)
solver.add                   ((local_148[0x10] ^ 0x54) * 0x20 +
                    (local_148[0x18] ^ 0x54) * -0x86 +
                    (local_148[0xb] ^ 0x54) * -0x94 +
                    (local_148[8] ^ 0x54) * -0x24 +
                    (local_148[0x1a] ^ 0x54) * 0x85 == -0x2439)


solver.add                          ((local_148[0x16] ^ 1) * 0x139 +
                           (local_148[0x11] ^ 1) * -0xd4 +
                           (local_148[7] ^ 1) * -5 +
                           (local_148[0xd] ^ 1) * -0xa4 == 0x1374)
solver.add                         ((local_148[0xf] ^ 0xa7) * -0xd8 +
                          (local_148[0x13] ^ 0xa7) * 0xd2 +
                          (local_148[4] ^ 0xa7) * 0x81 +
                          (local_148[0x1b] ^ 0xa7) * -0xde == -0x2733)
solver.add(                          (local_148[0xb] ^ 0x27) * 0xb9 +
                          (local_148[0x1a] ^ 0x27) * -0xb6 +
                          (local_148[0x15] ^ 0x27) * -0x36 +
                          (local_148[0x15] ^ 0x27) * 0x4f +
                          (local_148[10] ^ 0x27) * 0x8e == 0x3746)
solver.add(                           (local_148[0x16] ^ 0x8d) * 0xc6 +
                           (local_148[0x15] ^ 0x8d) * -0x15 +
                           (local_148[0xb] ^ 0x8d) * 0x26 +
                           (local_148[0xb] ^ 0x8d) * 0x71 +
                           (local_148[0x18] ^ 0x8d) * -0xb6 == 0x578c)
solver.add                          ((local_148[0x12] ^ 200) * -0x3a +
                           (local_148[0xd] ^ 200) * -0x5b +
                           (local_148[0x1b] ^ 200) * -0xca +
                           (local_148[0x14] ^ 200) * 0x16e == 0x35e4)
solver.add                       ((local_148[0x1b] ^ 0x6d) * 0xcc +
                        (local_148[0xd] ^ 0x6d) * -0x7c +
                        (local_148[5] ^ 0x6d) * -0x55 +
                        (local_148[0x15] ^ 109) +
                        (local_148[0x15] ^ 109) * 2 +
                        (local_148[0x18] ^ 0x6d) * 0xf6 == 0x3a3a)
solver.add(                           (local_148[0x1d] ^ 0x66) * -0xe7 +
                           (local_148[6] ^ 0x66) * 0xc4 +
                           (local_148[0x10] ^ 0x66) * 0xf3 +
                           (local_148[0x1a] ^ 0x66) * -0x4b +
                           (local_148[0x14] ^ 0x66) * -0x5d == -0x4997)
solver.add(                          ((local_148[0x16] ^ 0x1f) * 0xcc +
                           (local_148[0x15] ^ 0x1f) * -0xfd +
                           (local_148[0x19] ^ 0x1f) * -0x6a +
                           (local_148[0xe] ^ 0x1f) * -0x3d +
                           (local_148[0xd] ^ 0x1f) * 0x7d == 0x517))
solver.add                         ((local_148[0xf] ^ 0x2b) * -0xcf +
                          (local_148[0xd] ^ 0x2b) * 0x93 +
                          (local_148[0x11] ^ 0x2b) * 0x8f +
                          (local_148[9] ^ 0x2b) * 0xb2 +
                          (local_148[0x1e] ^ 0x2b) * 0x1e == 0x45fd)
solver.add(                          (local_148[0x18] ^ 0xd) * -0x5a +
                          (local_148[0x1e] ^ 0xd) * -100 +
                          (local_148[0x13] ^ 0xd) * -0x24 +
                          (local_148[0x15] ^ 0xd) * -0x6a == -0x7f12)
solver.add                         ((local_148[0x15] ^ 0x1e) * 0xe +
                          (local_148[9] ^ 0x1e) * 0x24 +
                          (local_148[0xc] ^ 0x1e) * 0xf6 +
                          (local_148[0x1a] ^ 0x1e) * -0x35 +
                          (local_148[0x17] ^ 0x1e) * -0x1f == 0x2b33)
solver.add                        ((local_148[7] ^ 0x1f) * 0x8a +
                         (local_148[8] ^ 0x1f) * 0x71 +
                         (local_148[0x1d] ^ 0x1f) * 0x7c +
                         (local_148[0x11] ^ 0x1f) * 6 +
                         (local_148[10] ^ 0x1f) * 0x95 == 0x654d )
solver.add(
                        (local_148[6] ^ 0x23) * -0x49 +
                          (local_148[0x1b] ^ 0x23) * -0x32 +
                          (local_148[0x18] ^ 0x23) * -0x1a +
                          (local_148[0x13] ^ 0x23) * 0xe8 +
                          (local_148[4] ^ 0x23) * -0xa6 == -0x17e1)
solver.add(
                         ((local_148[0x1c] ^ 0x87) * -0x46 +
                          (local_148[0x12] ^ 135) +
                          (local_148[0x12] ^ 135) * 8 +
                          (local_148[0x1e] ^ 0x87) * 0xd4 +
                          (local_148[0x17] ^ 0x87) * -0x7c +
                          (local_148[0x18] ^ 0x87) * 0x1e == 0x6dce))

solver.add                       ((local_148[0x18] ^ 0xe9) * 0x20 +
                        (local_148[0x11] ^ 0xe9) * -99 +
                        (local_148[0x1a] ^ 0xe9) * -0xae +
                        (local_148[9] ^ 0xe9) * -0x92 +
                        (local_148[8] ^ 0xe9) * 0xd7 == -0x5c96 )
solver.add(
                       (local_148[0x17] ^ 0x3e) * -0xd8 +
                           (local_148[0x1a] ^ 0x3e) * 10 +
                           (local_148[0x13] ^ 0x3e) * -9 +
                           (local_148[0xb] ^ 0x3e) * -0x10 +
                           (local_148[8] ^ 0x3e) * 0xdc == -0x6ae )
solver.add(
                          ((local_148[0x19] ^ 0xdf) * 0x5f +
                           (local_148[0x1b] ^ 0xdf) * 0x43 +
                           (local_148[4] ^ 0xdf) * -0x94 +
                           (local_148[0xb] ^ 0xdf) * 0x50 == 0x5e9c)) 
solver.add(
                         ((local_148[0x13] ^ 0x6a) * 0x45 +
                          (local_148[4] ^ 0x6a) * 0x52 +
                          (local_148[0x11] ^ 0x6a) * -0xa9 +
                          (local_148[0x17] ^ 0x6a) * 0x6e +
                          (local_148[0xe] ^ 0x6a) * -0xdb == -0x280d)) 
solver.add(
                        (local_148[0x1b] ^ 0x1b) * 0xd7 +
                          (local_148[0x1d] ^ 0x1b) * -0x98 +
                          (local_148[0xb] ^ 0x1b) * 0x20 +
                          (local_148[0x17] ^ 0x1b) * 0x4c +
                          (local_148[4] ^ 0x1b) * 0x6e == 0x525e )
solver.add(
                         ((local_148[4] ^ 1) * -0x11 +
                          (local_148[0x17] ^ 1) * -0x9e +
                          (local_148[7] ^ 1) * -0x87 +
                          (local_148[0x11] ^ 1) * -0xcd +
                          (local_148[0x12] ^ 1) * 0x93 == -0x5132))

for var in local_148:
    solver.add(var >= 0, var <= 127)


if solver.check() == sat:
    model = solver.model()
    #print("Solution trouvée:", model)
     # Extraire les valeurs de local_148 et afficher les caractères ASCII
    result = ''.join(chr(model.evaluate(local_148[i]).as_long()) for i in range(128) if model.evaluate(local_148[i]).as_long() != 0)
    
    print(result)
else:
    print("Pas de solution")

