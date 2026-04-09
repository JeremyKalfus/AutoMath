import Mathlib

example : ((0 : Fin 24) + 5) = 5 := by
  native_decide

example : ((19 : Fin 24) + 5) = 0 := by
  native_decide

example (x : Fin 24 → Int) : x ((19 : Fin 24) + 5) = x 0 := by
  native_decide

example (x : Fin 24 → Int) : x ((19 : Fin 24) + 5) = x 0 := by
  norm_num
