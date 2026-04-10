import AutoMath.Families.PrimeSupportTemplates
import AutoMath.Families.ZeroDivisorSupports
import AutoMath.Families.ZeroDivisorReductions
import AutoMath.Families.CNBCCriteria
import AutoMath.Z3Z25
import AutoMath.Z5Z25
import AutoMath.Z7Z25
import AutoMath.Z5Z5Z2
import AutoMath.Z5Z5Z3
import AutoMath.Z7Z7Z2
import AutoMath.Z2Power8
import AutoMath.P7SquarePrimeLabeling
import AutoMath.P4xP4GridPrimeLabeling

/-
`AutoMath.Publications` is the publication-safe Lean surface.

It keeps reusable family-supporting lemmas and the currently stable exact-instance inventory on the
default build path, while preserving heavier or still-experimental modules outside the root import.
-/
