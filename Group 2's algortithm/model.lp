\ Model solver
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  7 Xad1 + 7 Xad2 + 7 Xad3 + 7 Xad4 + 7 Xad5 + 7 Xad6 + 7 Xda1 + 7 Xda2
   + 7 Xda3 + 7 Xda4 + 7 Xda5 + 7 Xda6 + 4 Xba1 + 4 Xba2 + 4 Xba3 + 4 Xba4
   + 4 Xba5 + 4 Xba6 + 4 Xab1 + 4 Xab2 + 4 Xab3 + 4 Xab4 + 4 Xab5 + 4 Xab6
   + 4 Xbe1 + 4 Xbe2 + 4 Xbe3 + 4 Xbe4 + 4 Xbe5 + 4 Xbe6 + 4 Xeb1 + 4 Xeb2
   + 4 Xeb3 + 4 Xeb4 + 4 Xeb5 + 4 Xeb6 + 8 Xcb1 + 8 Xcb2 + 8 Xcb3 + 8 Xcb4
   + 8 Xcb5 + 8 Xcb6 + 8 Xbc1 + 8 Xbc2 + 8 Xbc3 + 8 Xbc4 + 8 Xbc5 + 8 Xbc6
   + 4 Xcg1 + 4 Xcg2 + 4 Xcg3 + 4 Xcg4 + 4 Xcg5 + 4 Xcg6 + 4 Xgc1 + 4 Xgc2
   + 4 Xgc3 + 4 Xgc4 + 4 Xgc5 + 4 Xgc6 + 5 Xdi1 + 5 Xdi2 + 5 Xdi3 + 5 Xdi4
   + 5 Xdi5 + 5 Xdi6 + 5 Xid1 + 5 Xid2 + 5 Xid3 + 5 Xid4 + 5 Xid5 + 5 Xid6
   + 3 Xeh1 + 3 Xeh2 + 3 Xeh3 + 3 Xeh4 + 3 Xeh5 + 3 Xeh6 + 3 Xhe1 + 3 Xhe2
   + 3 Xhe3 + 3 Xhe4 + 3 Xhe5 + 3 Xhe6 + 5 Xfe1 + 5 Xfe2 + 5 Xfe3 + 5 Xfe4
   + 5 Xfe5 + 5 Xfe6 + 5 Xef1 + 5 Xef2 + 5 Xef3 + 5 Xef4 + 5 Xef5 + 5 Xef6
   + 8 Xfk1 + 8 Xfk2 + 8 Xfk3 + 8 Xfk4 + 8 Xfk5 + 8 Xfk6 + 8 Xkf1 + 8 Xkf2
   + 8 Xkf3 + 8 Xkf4 + 8 Xkf5 + 8 Xkf6 + 3 Xgf1 + 3 Xgf2 + 3 Xgf3 + 3 Xgf4
   + 3 Xgf5 + 3 Xgf6 + 3 Xfg1 + 3 Xfg2 + 3 Xfg3 + 3 Xfg4 + 3 Xfg5 + 3 Xfg6
   + 8 Xgl1 + 8 Xgl2 + 8 Xgl3 + 8 Xgl4 + 8 Xgl5 + 8 Xgl6 + 8 Xlg1 + 8 Xlg2
   + 8 Xlg3 + 8 Xlg4 + 8 Xlg5 + 8 Xlg6 + 4 Xhd1 + 4 Xhd2 + 4 Xhd3 + 4 Xhd4
   + 4 Xhd5 + 4 Xhd6 + 4 Xdh1 + 4 Xdh2 + 4 Xdh3 + 4 Xdh4 + 4 Xdh5 + 4 Xdh6
   + 5 Xhj1 + 5 Xhj2 + 5 Xhj3 + 5 Xhj4 + 5 Xhj5 + 5 Xhj6 + 5 Xjh1 + 5 Xjh2
   + 5 Xjh3 + 5 Xjh4 + 5 Xjh5 + 5 Xjh6 + 4 Xji1 + 4 Xji2 + 4 Xji3 + 4 Xji4
   + 4 Xji5 + 4 Xji6 + 4 Xij1 + 4 Xij2 + 4 Xij3 + 4 Xij4 + 4 Xij5 + 4 Xij6
   + 5 Xkj1 + 5 Xkj2 + 5 Xkj3 + 5 Xkj4 + 5 Xkj5 + 5 Xkj6 + 5 Xjk1 + 5 Xjk2
   + 5 Xjk3 + 5 Xjk4 + 5 Xjk5 + 5 Xjk6 + 3 Xlk1 + 3 Xlk2 + 3 Xlk3 + 3 Xlk4
   + 3 Xlk5 + 3 Xlk6 + 3 Xkl1 + 3 Xkl2 + 3 Xkl3 + 3 Xkl4 + 3 Xkl5 + 3 Xkl6
Subject To
 R0: Xad1 - Xda1 + Xba1 - Xab1 = 1
 R1: Xad2 - Xda2 + Xba2 - Xab2 = 0
 R2: Xad3 - Xda3 + Xba3 - Xab3 = 0
 R3: Xad4 - Xda4 + Xba4 - Xab4 = 0
 R4: Xad5 - Xda5 + Xba5 - Xab5 = 0
 R5: Xad6 - Xda6 + Xba6 - Xab6 = 0
 R6: Xba1 - Xab1 + Xbe1 - Xeb1 + Xcb1 - Xbc1 = 0
 R7: Xba2 - Xab2 + Xbe2 - Xeb2 + Xcb2 - Xbc2 = 0
 R8: Xba3 - Xab3 + Xbe3 - Xeb3 + Xcb3 - Xbc3 = 0
 R9: Xba4 - Xab4 + Xbe4 - Xeb4 + Xcb4 - Xbc4 = 0
 R10: Xba5 - Xab5 + Xbe5 - Xeb5 + Xcb5 - Xbc5 = 0
 R11: Xba6 - Xab6 + Xbe6 - Xeb6 + Xcb6 - Xbc6 = 1
 R12: Xcb1 - Xbc1 + Xcg1 - Xgc1 = 0
 R13: Xcb2 - Xbc2 + Xcg2 - Xgc2 = -1
 R14: Xcb3 - Xbc3 + Xcg3 - Xgc3 = 0
 R15: Xcb4 - Xbc4 + Xcg4 - Xgc4 = 0
 R16: Xcb5 - Xbc5 + Xcg5 - Xgc5 = 0
 R17: Xcb6 - Xbc6 + Xcg6 - Xgc6 = 0
 R18: Xad1 - Xda1 + Xdi1 - Xid1 + Xhd1 - Xdh1 = 0
 R19: Xad2 - Xda2 + Xdi2 - Xid2 + Xhd2 - Xdh2 = 0
 R20: Xad3 - Xda3 + Xdi3 - Xid3 + Xhd3 - Xdh3 = 1
 R21: Xad4 - Xda4 + Xdi4 - Xid4 + Xhd4 - Xdh4 = -1
 R22: Xad5 - Xda5 + Xdi5 - Xid5 + Xhd5 - Xdh5 = 0
 R23: Xad6 - Xda6 + Xdi6 - Xid6 + Xhd6 - Xdh6 = 0
 R24: Xbe1 - Xeb1 + Xeh1 - Xhe1 + Xfe1 - Xef1 = 0
 R25: Xbe2 - Xeb2 + Xeh2 - Xhe2 + Xfe2 - Xef2 = 0
 R26: Xbe3 - Xeb3 + Xeh3 - Xhe3 + Xfe3 - Xef3 = 0
 R27: Xbe4 - Xeb4 + Xeh4 - Xhe4 + Xfe4 - Xef4 = 0
 R28: Xbe5 - Xeb5 + Xeh5 - Xhe5 + Xfe5 - Xef5 = 0
 R29: Xbe6 - Xeb6 + Xeh6 - Xhe6 + Xfe6 - Xef6 = 0
 R30: Xfe1 - Xef1 + Xfk1 - Xkf1 + Xgf1 - Xfg1 = 0
 R31: Xfe2 - Xef2 + Xfk2 - Xkf2 + Xgf2 - Xfg2 = 0
 R32: Xfe3 - Xef3 + Xfk3 - Xkf3 + Xgf3 - Xfg3 = -1
 R33: Xfe4 - Xef4 + Xfk4 - Xkf4 + Xgf4 - Xfg4 = 0
 R34: Xfe5 - Xef5 + Xfk5 - Xkf5 + Xgf5 - Xfg5 = 0
 R35: Xfe6 - Xef6 + Xfk6 - Xkf6 + Xgf6 - Xfg6 = 0
 R36: Xcg1 - Xgc1 + Xgf1 - Xfg1 + Xgl1 - Xlg1 = 0
 R37: Xcg2 - Xgc2 + Xgf2 - Xfg2 + Xgl2 - Xlg2 = 0
 R38: Xcg3 - Xgc3 + Xgf3 - Xfg3 + Xgl3 - Xlg3 = 0
 R39: Xcg4 - Xgc4 + Xgf4 - Xfg4 + Xgl4 - Xlg4 = 0
 R40: Xcg5 - Xgc5 + Xgf5 - Xfg5 + Xgl5 - Xlg5 = 1
 R41: Xcg6 - Xgc6 + Xgf6 - Xfg6 + Xgl6 - Xlg6 = 0
 R42: Xeh1 - Xhe1 + Xhd1 - Xdh1 + Xhj1 - Xjh1 = 0
 R43: Xeh2 - Xhe2 + Xhd2 - Xdh2 + Xhj2 - Xjh2 = 0
 R44: Xeh3 - Xhe3 + Xhd3 - Xdh3 + Xhj3 - Xjh3 = 0
 R45: Xeh4 - Xhe4 + Xhd4 - Xdh4 + Xhj4 - Xjh4 = 0
 R46: Xeh5 - Xhe5 + Xhd5 - Xdh5 + Xhj5 - Xjh5 = -1
 R47: Xeh6 - Xhe6 + Xhd6 - Xdh6 + Xhj6 - Xjh6 = 0
 R48: Xdi1 - Xid1 + Xji1 - Xij1 = 0
 R49: Xdi2 - Xid2 + Xji2 - Xij2 = 1
 R50: Xdi3 - Xid3 + Xji3 - Xij3 = 0
 R51: Xdi4 - Xid4 + Xji4 - Xij4 = 0
 R52: Xdi5 - Xid5 + Xji5 - Xij5 = 0
 R53: Xdi6 - Xid6 + Xji6 - Xij6 = 0
 R54: Xhj1 - Xjh1 + Xji1 - Xij1 + Xkj1 - Xjk1 = 0
 R55: Xhj2 - Xjh2 + Xji2 - Xij2 + Xkj2 - Xjk2 = 0
 R56: Xhj3 - Xjh3 + Xji3 - Xij3 + Xkj3 - Xjk3 = 0
 R57: Xhj4 - Xjh4 + Xji4 - Xij4 + Xkj4 - Xjk4 = 0
 R58: Xhj5 - Xjh5 + Xji5 - Xij5 + Xkj5 - Xjk5 = 0
 R59: Xhj6 - Xjh6 + Xji6 - Xij6 + Xkj6 - Xjk6 = 0
 R60: Xfk1 - Xkf1 + Xkj1 - Xjk1 + Xlk1 - Xkl1 = 0
 R61: Xfk2 - Xkf2 + Xkj2 - Xjk2 + Xlk2 - Xkl2 = 0
 R62: Xfk3 - Xkf3 + Xkj3 - Xjk3 + Xlk3 - Xkl3 = 0
 R63: Xfk4 - Xkf4 + Xkj4 - Xjk4 + Xlk4 - Xkl4 = 1
 R64: Xfk5 - Xkf5 + Xkj5 - Xjk5 + Xlk5 - Xkl5 = 0
 R65: Xfk6 - Xkf6 + Xkj6 - Xjk6 + Xlk6 - Xkl6 = -1
 R66: Xgl1 - Xlg1 + Xlk1 - Xkl1 = -1
 R67: Xgl2 - Xlg2 + Xlk2 - Xkl2 = 0
 R68: Xgl3 - Xlg3 + Xlk3 - Xkl3 = 0
 R69: Xgl4 - Xlg4 + Xlk4 - Xkl4 = 0
 R70: Xgl5 - Xlg5 + Xlk5 - Xkl5 = 0
 R71: Xgl6 - Xlg6 + Xlk6 - Xkl6 = 0
 R72: Xad1 + Xad2 + Xad3 + Xad4 + Xad5 + Xad6 + Xda1 + Xda2 + Xda3 + Xda4
   + Xda5 + Xda6 <= 2
 R73: Xba1 + Xba2 + Xba3 + Xba4 + Xba5 + Xba6 + Xab1 + Xab2 + Xab3 + Xab4
   + Xab5 + Xab6 <= 2
 R74: Xbe1 + Xbe2 + Xbe3 + Xbe4 + Xbe5 + Xbe6 + Xeb1 + Xeb2 + Xeb3 + Xeb4
   + Xeb5 + Xeb6 <= 2
 R75: Xcb1 + Xcb2 + Xcb3 + Xcb4 + Xcb5 + Xcb6 + Xbc1 + Xbc2 + Xbc3 + Xbc4
   + Xbc5 + Xbc6 <= 2
 R76: Xcg1 + Xcg2 + Xcg3 + Xcg4 + Xcg5 + Xcg6 + Xgc1 + Xgc2 + Xgc3 + Xgc4
   + Xgc5 + Xgc6 <= 2
 R77: Xdi1 + Xdi2 + Xdi3 + Xdi4 + Xdi5 + Xdi6 + Xid1 + Xid2 + Xid3 + Xid4
   + Xid5 + Xid6 <= 2
 R78: Xeh1 + Xeh2 + Xeh3 + Xeh4 + Xeh5 + Xeh6 + Xhe1 + Xhe2 + Xhe3 + Xhe4
   + Xhe5 + Xhe6 <= 2
 R79: Xfe1 + Xfe2 + Xfe3 + Xfe4 + Xfe5 + Xfe6 + Xef1 + Xef2 + Xef3 + Xef4
   + Xef5 + Xef6 <= 2
 R80: Xfk1 + Xfk2 + Xfk3 + Xfk4 + Xfk5 + Xfk6 + Xkf1 + Xkf2 + Xkf3 + Xkf4
   + Xkf5 + Xkf6 <= 2
 R81: Xgf1 + Xgf2 + Xgf3 + Xgf4 + Xgf5 + Xgf6 + Xfg1 + Xfg2 + Xfg3 + Xfg4
   + Xfg5 + Xfg6 <= 2
 R82: Xgl1 + Xgl2 + Xgl3 + Xgl4 + Xgl5 + Xgl6 + Xlg1 + Xlg2 + Xlg3 + Xlg4
   + Xlg5 + Xlg6 <= 2
 R83: Xhd1 + Xhd2 + Xhd3 + Xhd4 + Xhd5 + Xhd6 + Xdh1 + Xdh2 + Xdh3 + Xdh4
   + Xdh5 + Xdh6 <= 2
 R84: Xhj1 + Xhj2 + Xhj3 + Xhj4 + Xhj5 + Xhj6 + Xjh1 + Xjh2 + Xjh3 + Xjh4
   + Xjh5 + Xjh6 <= 2
 R85: Xji1 + Xji2 + Xji3 + Xji4 + Xji5 + Xji6 + Xij1 + Xij2 + Xij3 + Xij4
   + Xij5 + Xij6 <= 2
 R86: Xkj1 + Xkj2 + Xkj3 + Xkj4 + Xkj5 + Xkj6 + Xjk1 + Xjk2 + Xjk3 + Xjk4
   + Xjk5 + Xjk6 <= 2
 R87: Xlk1 + Xlk2 + Xlk3 + Xlk4 + Xlk5 + Xlk6 + Xkl1 + Xkl2 + Xkl3 + Xkl4
   + Xkl5 + Xkl6 <= 2
Bounds
Binaries
 Xad1 Xad2 Xad3 Xad4 Xad5 Xad6 Xda1 Xda2 Xda3 Xda4 Xda5 Xda6 Xba1 Xba2 Xba3
 Xba4 Xba5 Xba6 Xab1 Xab2 Xab3 Xab4 Xab5 Xab6 Xbe1 Xbe2 Xbe3 Xbe4 Xbe5 Xbe6
 Xeb1 Xeb2 Xeb3 Xeb4 Xeb5 Xeb6 Xcb1 Xcb2 Xcb3 Xcb4 Xcb5 Xcb6 Xbc1 Xbc2 Xbc3
 Xbc4 Xbc5 Xbc6 Xcg1 Xcg2 Xcg3 Xcg4 Xcg5 Xcg6 Xgc1 Xgc2 Xgc3 Xgc4 Xgc5 Xgc6
 Xdi1 Xdi2 Xdi3 Xdi4 Xdi5 Xdi6 Xid1 Xid2 Xid3 Xid4 Xid5 Xid6 Xeh1 Xeh2 Xeh3
 Xeh4 Xeh5 Xeh6 Xhe1 Xhe2 Xhe3 Xhe4 Xhe5 Xhe6 Xfe1 Xfe2 Xfe3 Xfe4 Xfe5 Xfe6
 Xef1 Xef2 Xef3 Xef4 Xef5 Xef6 Xfk1 Xfk2 Xfk3 Xfk4 Xfk5 Xfk6 Xkf1 Xkf2 Xkf3
 Xkf4 Xkf5 Xkf6 Xgf1 Xgf2 Xgf3 Xgf4 Xgf5 Xgf6 Xfg1 Xfg2 Xfg3 Xfg4 Xfg5 Xfg6
 Xgl1 Xgl2 Xgl3 Xgl4 Xgl5 Xgl6 Xlg1 Xlg2 Xlg3 Xlg4 Xlg5 Xlg6 Xhd1 Xhd2 Xhd3
 Xhd4 Xhd5 Xhd6 Xdh1 Xdh2 Xdh3 Xdh4 Xdh5 Xdh6 Xhj1 Xhj2 Xhj3 Xhj4 Xhj5 Xhj6
 Xjh1 Xjh2 Xjh3 Xjh4 Xjh5 Xjh6 Xji1 Xji2 Xji3 Xji4 Xji5 Xji6 Xij1 Xij2 Xij3
 Xij4 Xij5 Xij6 Xkj1 Xkj2 Xkj3 Xkj4 Xkj5 Xkj6 Xjk1 Xjk2 Xjk3 Xjk4 Xjk5 Xjk6
 Xlk1 Xlk2 Xlk3 Xlk4 Xlk5 Xlk6 Xkl1 Xkl2 Xkl3 Xkl4 Xkl5 Xkl6
End
