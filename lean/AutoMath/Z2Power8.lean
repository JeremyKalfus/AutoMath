import Mathlib.Data.Fin.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Disjoint
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Nat.GCD.Basic

namespace AutoMath
namespace Z2Power8

/-- Vertices of `Γ(Z_2^8)` are the nonempty proper subsets of the eight coordinates. -/
abbrev Raw := Finset (Fin 8)

instance : DecidableEq Raw := inferInstance

instance : Fintype Raw := inferInstance

def IsVertex (s : Raw) : Prop :=
  s.Nonempty ∧ s ≠ Finset.univ

abbrev Vertex := {s : Raw // IsVertex s}

instance : DecidablePred IsVertex := by
  intro s
  unfold IsVertex
  infer_instance

instance : Fintype Vertex := Subtype.fintype IsVertex

/-- The bitmask code of a subset of `Fin 8`, using the basis `1, 2, 4, ..., 128`. -/
def subsetCode (s : Raw) : Nat :=
  s.sum fun i => (2 : Nat) ^ i.1

/-- Adjacency in `Γ(Z_2^8)`: two vertices are adjacent exactly when their supports are disjoint. -/
def Adj (x y : Vertex) : Prop :=
  Disjoint x.1 y.1

/-- `Label` is the machine encoding of the mathematical label set `{1, ..., 254}` via
`labelValue i = i + 1`. -/
abbrev Label := Fin 254

def labelValue (ℓ : Label) : Nat := ℓ.val.succ

def rawLabel (s : Raw) : Label :=
  match subsetCode s with
  | 1 => ⟨7, by decide⟩
  | 2 => ⟨2, by decide⟩
  | 3 => ⟨1, by decide⟩
  | 4 => ⟨4, by decide⟩
  | 5 => ⟨253, by decide⟩
  | 6 => ⟨8, by decide⟩
  | 7 => ⟨239, by decide⟩
  | 8 => ⟨6, by decide⟩
  | 9 => ⟨247, by decide⟩
  | 10 => ⟨20, by decide⟩
  | 11 => ⟨251, by decide⟩
  | 12 => ⟨24, by decide⟩
  | 13 => ⟨9, by decide⟩
  | 14 => ⟨14, by decide⟩
  | 15 => ⟨13, by decide⟩
  | 16 => ⟨10, by decide⟩
  | 17 => ⟨15, by decide⟩
  | 18 => ⟨22, by decide⟩
  | 19 => ⟨17, by decide⟩
  | 20 => ⟨28, by decide⟩
  | 21 => ⟨19, by decide⟩
  | 22 => ⟨26, by decide⟩
  | 23 => ⟨21, by decide⟩
  | 24 => ⟨30, by decide⟩
  | 25 => ⟨27, by decide⟩
  | 26 => ⟨32, by decide⟩
  | 27 => ⟨23, by decide⟩
  | 28 => ⟨34, by decide⟩
  | 29 => ⟨31, by decide⟩
  | 30 => ⟨36, by decide⟩
  | 31 => ⟨29, by decide⟩
  | 32 => ⟨12, by decide⟩
  | 33 => ⟨25, by decide⟩
  | 34 => ⟨38, by decide⟩
  | 35 => ⟨245, by decide⟩
  | 36 => ⟨40, by decide⟩
  | 37 => ⟨39, by decide⟩
  | 38 => ⟨44, by decide⟩
  | 39 => ⟨45, by decide⟩
  | 40 => ⟨48, by decide⟩
  | 41 => ⟨51, by decide⟩
  | 42 => ⟨52, by decide⟩
  | 43 => ⟨41, by decide⟩
  | 44 => ⟨58, by decide⟩
  | 45 => ⟨49, by decide⟩
  | 46 => ⟨60, by decide⟩
  | 47 => ⟨47, by decide⟩
  | 48 => ⟨66, by decide⟩
  | 49 => ⟨43, by decide⟩
  | 50 => ⟨68, by decide⟩
  | 51 => ⟨53, by decide⟩
  | 52 => ⟨54, by decide⟩
  | 53 => ⟨57, by decide⟩
  | 54 => ⟨64, by decide⟩
  | 55 => ⟨59, by decide⟩
  | 56 => ⟨70, by decide⟩
  | 57 => ⟨55, by decide⟩
  | 58 => ⟨62, by decide⟩
  | 59 => ⟨61, by decide⟩
  | 60 => ⟨76, by decide⟩
  | 61 => ⟨63, by decide⟩
  | 62 => ⟨74, by decide⟩
  | 63 => ⟨65, by decide⟩
  | 64 => ⟨16, by decide⟩
  | 65 => ⟨33, by decide⟩
  | 66 => ⟨128, by decide⟩
  | 67 => ⟨5, by decide⟩
  | 68 => ⟨72, by decide⟩
  | 69 => ⟨67, by decide⟩
  | 70 => ⟨80, by decide⟩
  | 71 => ⟨71, by decide⟩
  | 72 => ⟨96, by decide⟩
  | 73 => ⟨85, by decide⟩
  | 74 => ⟨82, by decide⟩
  | 75 => ⟨83, by decide⟩
  | 76 => ⟨84, by decide⟩
  | 77 => ⟨69, by decide⟩
  | 78 => ⟨86, by decide⟩
  | 79 => ⟨79, by decide⟩
  | 80 => ⟨100, by decide⟩
  | 81 => ⟨73, by decide⟩
  | 82 => ⟨98, by decide⟩
  | 83 => ⟨87, by decide⟩
  | 84 => ⟨88, by decide⟩
  | 85 => ⟨99, by decide⟩
  | 86 => ⟨106, by decide⟩
  | 87 => ⟨89, by decide⟩
  | 88 => ⟨118, by decide⟩
  | 89 => ⟨97, by decide⟩
  | 90 => ⟨92, by decide⟩
  | 91 => ⟨91, by decide⟩
  | 92 => ⟨120, by decide⟩
  | 93 => ⟨109, by decide⟩
  | 94 => ⟨104, by decide⟩
  | 95 => ⟨95, by decide⟩
  | 96 => ⟨102, by decide⟩
  | 97 => ⟨81, by decide⟩
  | 98 => ⟨112, by decide⟩
  | 99 => ⟨77, by decide⟩
  | 100 => ⟨124, by decide⟩
  | 101 => ⟨103, by decide⟩
  | 102 => ⟨114, by decide⟩
  | 103 => ⟨101, by decide⟩
  | 104 => ⟨90, by decide⟩
  | 105 => ⟨111, by decide⟩
  | 106 => ⟨116, by decide⟩
  | 107 => ⟨105, by decide⟩
  | 108 => ⟨126, by decide⟩
  | 109 => ⟨115, by decide⟩
  | 110 => ⟨122, by decide⟩
  | 111 => ⟨107, by decide⟩
  | 112 => ⟨136, by decide⟩
  | 113 => ⟨127, by decide⟩
  | 114 => ⟨110, by decide⟩
  | 115 => ⟨11, by decide⟩
  | 116 => ⟨138, by decide⟩
  | 117 => ⟨117, by decide⟩
  | 118 => ⟨134, by decide⟩
  | 119 => ⟨119, by decide⟩
  | 120 => ⟨130, by decide⟩
  | 121 => ⟨121, by decide⟩
  | 122 => ⟨142, by decide⟩
  | 123 => ⟨123, by decide⟩
  | 124 => ⟨144, by decide⟩
  | 125 => ⟨129, by decide⟩
  | 126 => ⟨146, by decide⟩
  | 127 => ⟨125, by decide⟩
  | 128 => ⟨18, by decide⟩
  | 129 => ⟨37, by decide⟩
  | 130 => ⟨46, by decide⟩
  | 131 => ⟨35, by decide⟩
  | 132 => ⟨78, by decide⟩
  | 133 => ⟨75, by decide⟩
  | 134 => ⟨94, by decide⟩
  | 135 => ⟨93, by decide⟩
  | 136 => ⟨132, by decide⟩
  | 137 => ⟨3, by decide⟩
  | 138 => ⟨140, by decide⟩
  | 139 => ⟨113, by decide⟩
  | 140 => ⟨150, by decide⟩
  | 141 => ⟨139, by decide⟩
  | 142 => ⟨154, by decide⟩
  | 143 => ⟨137, by decide⟩
  | 144 => ⟨172, by decide⟩
  | 145 => ⟨133, by decide⟩
  | 146 => ⟨156, by decide⟩
  | 147 => ⟨131, by decide⟩
  | 148 => ⟨162, by decide⟩
  | 149 => ⟨147, by decide⟩
  | 150 => ⟨158, by decide⟩
  | 151 => ⟨143, by decide⟩
  | 152 => ⟨166, by decide⟩
  | 153 => ⟨151, by decide⟩
  | 154 => ⟨160, by decide⟩
  | 155 => ⟨153, by decide⟩
  | 156 => ⟨174, by decide⟩
  | 157 => ⟨157, by decide⟩
  | 158 => ⟨164, by decide⟩
  | 159 => ⟨149, by decide⟩
  | 160 => ⟨168, by decide⟩
  | 161 => ⟨141, by decide⟩
  | 162 => ⟨170, by decide⟩
  | 163 => ⟨155, by decide⟩
  | 164 => ⟨178, by decide⟩
  | 165 => ⟨159, by decide⟩
  | 166 => ⟨176, by decide⟩
  | 167 => ⟨161, by decide⟩
  | 168 => ⟨190, by decide⟩
  | 169 => ⟨163, by decide⟩
  | 170 => ⟨182, by decide⟩
  | 171 => ⟨165, by decide⟩
  | 172 => ⟨196, by decide⟩
  | 173 => ⟨177, by decide⟩
  | 174 => ⟨188, by decide⟩
  | 175 => ⟨167, by decide⟩
  | 176 => ⟨208, by decide⟩
  | 177 => ⟨175, by decide⟩
  | 178 => ⟨192, by decide⟩
  | 179 => ⟨183, by decide⟩
  | 180 => ⟨184, by decide⟩
  | 181 => ⟨187, by decide⟩
  | 182 => ⟨194, by decide⟩
  | 183 => ⟨173, by decide⟩
  | 184 => ⟨198, by decide⟩
  | 185 => ⟨181, by decide⟩
  | 186 => ⟨200, by decide⟩
  | 187 => ⟨185, by decide⟩
  | 188 => ⟨202, by decide⟩
  | 189 => ⟨189, by decide⟩
  | 190 => ⟨204, by decide⟩
  | 191 => ⟨179, by decide⟩
  | 192 => ⟨148, by decide⟩
  | 193 => ⟨135, by decide⟩
  | 194 => ⟨152, by decide⟩
  | 195 => ⟨145, by decide⟩
  | 196 => ⟨180, by decide⟩
  | 197 => ⟨169, by decide⟩
  | 198 => ⟨206, by decide⟩
  | 199 => ⟨171, by decide⟩
  | 200 => ⟨216, by decide⟩
  | 201 => ⟨193, by decide⟩
  | 202 => ⟨218, by decide⟩
  | 203 => ⟨191, by decide⟩
  | 204 => ⟨214, by decide⟩
  | 205 => ⟨195, by decide⟩
  | 206 => ⟨224, by decide⟩
  | 207 => ⟨199, by decide⟩
  | 208 => ⟨186, by decide⟩
  | 209 => ⟨201, by decide⟩
  | 210 => ⟨210, by decide⟩
  | 211 => ⟨197, by decide⟩
  | 212 => ⟨226, by decide⟩
  | 213 => ⟨213, by decide⟩
  | 214 => ⟨228, by decide⟩
  | 215 => ⟨203, by decide⟩
  | 216 => ⟨240, by decide⟩
  | 217 => ⟨217, by decide⟩
  | 218 => ⟨230, by decide⟩
  | 219 => ⟨211, by decide⟩
  | 220 => ⟨234, by decide⟩
  | 221 => ⟨219, by decide⟩
  | 222 => ⟨232, by decide⟩
  | 223 => ⟨209, by decide⟩
  | 224 => ⟨220, by decide⟩
  | 225 => ⟨205, by decide⟩
  | 226 => ⟨212, by decide⟩
  | 227 => ⟨207, by decide⟩
  | 228 => ⟨222, by decide⟩
  | 229 => ⟨231, by decide⟩
  | 230 => ⟨236, by decide⟩
  | 231 => ⟨215, by decide⟩
  | 232 => ⟨246, by decide⟩
  | 233 => ⟨223, by decide⟩
  | 234 => ⟨242, by decide⟩
  | 235 => ⟨225, by decide⟩
  | 236 => ⟨238, by decide⟩
  | 237 => ⟨235, by decide⟩
  | 238 => ⟨244, by decide⟩
  | 239 => ⟨227, by decide⟩
  | 240 => ⟨250, by decide⟩
  | 241 => ⟨241, by decide⟩
  | 242 => ⟨248, by decide⟩
  | 243 => ⟨221, by decide⟩
  | 244 => ⟨0, by decide⟩
  | 245 => ⟨249, by decide⟩
  | 246 => ⟨252, by decide⟩
  | 247 => ⟨229, by decide⟩
  | 248 => ⟨42, by decide⟩
  | 249 => ⟨237, by decide⟩
  | 250 => ⟨50, by decide⟩
  | 251 => ⟨233, by decide⟩
  | 252 => ⟨108, by decide⟩
  | 253 => ⟨243, by decide⟩
  | 254 => ⟨56, by decide⟩
  | _ => ⟨0, by decide⟩

def label (x : Vertex) : Label := rawLabel x.1

theorem vertex_card : Fintype.card Vertex = 254 := by
  decide +kernel

theorem labelValue_bounds (ℓ : Label) : 1 ≤ labelValue ℓ ∧ labelValue ℓ ≤ 254 := by
  exact ⟨Nat.succ_le_succ (Nat.zero_le _), Nat.succ_le_of_lt ℓ.is_lt⟩

def EdgeCoprime (f : Vertex → Label) : Prop :=
  ∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))

def IsPrimeLabeling (f : Vertex → Label) : Prop :=
  Function.Bijective f ∧ EdgeCoprime f

theorem raw_label_injective_on_vertices :
    ∀ x y : Raw, IsVertex x → IsVertex y → rawLabel x = rawLabel y → x = y := by
  decide +kernel

theorem raw_label_edgeCoprime :
    ∀ x y : Raw,
      IsVertex x →
      IsVertex y →
      Disjoint x y →
      Nat.Coprime (labelValue (rawLabel x)) (labelValue (rawLabel y)) := by
  decide +kernel

theorem label_injective : Function.Injective label := by
  intro x y hxy
  apply Subtype.ext
  exact raw_label_injective_on_vertices x.1 y.1 x.2 y.2 hxy

theorem label_edgeCoprime : EdgeCoprime label := by
  intro x y hxy
  exact raw_label_edgeCoprime x.1 y.1 x.2 y.2 hxy

theorem z2_power_8_zeroDivisorGraph_prime_checked : IsPrimeLabeling label := by
  refine ⟨?_, label_edgeCoprime⟩
  exact (Fintype.bijective_iff_injective_and_card label).2 ⟨label_injective, by
    simpa using vertex_card⟩

/-- Explicit natural-number form of the witness: the actual labels are the integers `{1, ..., 254}`,
read from `Label` via `labelValue`. -/
theorem z2_power_8_zeroDivisorGraph_prime_explicit :
    ∃ f : Vertex → Label,
      Function.Bijective f ∧
      (∀ x, 1 ≤ labelValue (f x) ∧ labelValue (f x) ≤ 254) ∧
      (∀ x y, Adj x y → Nat.Coprime (labelValue (f x)) (labelValue (f y))) := by
  refine ⟨label, ?_, ?_, ?_⟩
  exact z2_power_8_zeroDivisorGraph_prime_checked.1
  intro x
  exact labelValue_bounds (label x)
  exact z2_power_8_zeroDivisorGraph_prime_checked.2

/-- The zero-divisor graph `Γ(Z_2^8)` admits a prime labeling. Here `Label = Fin 254` is read as
the mathematical label set `{1, ..., 254}` via `labelValue i = i + 1`. -/
theorem z2_power_8_zeroDivisorGraph_prime : ∃ f : Vertex → Label, IsPrimeLabeling f := by
  exact ⟨label, z2_power_8_zeroDivisorGraph_prime_checked⟩

end Z2Power8
end AutoMath
