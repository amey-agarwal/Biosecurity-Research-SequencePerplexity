from abc import ABC, abstractmethod
import random


class ScoreModel(ABC):
    @abstractmethod
    def score(self, sequence: str) -> float:
        ...


class NucleotideTransformerScorer(ScoreModel):
    def __init__(self, mask_fraction: float | None = None):
        self.mask_fraction = mask_fraction

    def score(self, sequence: str) -> float:
        positions = list(range(len(sequence)))
        if self.mask_fraction is not None:
            k = max(1, int(len(sequence) * self.mask_fraction))
            positions = random.sample(positions, k)

        log_probs = [self._masked_log_prob(sequence, pos) for pos in positions]
        return sum(log_probs) / len(log_probs)

    def _masked_log_prob(self, sequence: str, position: int) -> float:
        raise NotImplementedError("model call wiring comes next")
