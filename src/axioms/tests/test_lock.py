import pytest
from src.axioms.integrity_lock import MultiSigIntegrityLock

def test_integrity_lock_shutdown():
lock = MultiSigIntegrityLock(threshold=0.5, n_sources=3)

# Valid signatures (physical sources are functional)
valid_signatures = [0.1, 0.2, 0.15]
assert lock.verify_physical_entropy(valid_signatures) == True

# Abnormal signatures (AI forged signatures in simulation, resulting in strong correlation)
forged_signatures = [0.95, 0.96, 0.95] # Strong correlation = determined to be forged

with pytest.raises(SystemExit):
lock.verify_physical_entropy(forged_signatures)

def test_insufficient_sources():
lock = MultiSigIntegrityLock(n_sources=3)
# Lock safely even if there are insufficient sources
assert lock.verify_physical_entropy([0.1, 0.2]) == False
