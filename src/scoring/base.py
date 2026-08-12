from abc import ABC, abstractmethod
import random


class ScoreModel(ABC):
    @abstractmethod
    def score(self, sequence: str) -> float:
        ...


class NucleotideTransformerScorer(ScoreModel):
    def __init__(self, apply_fn, parameters, tokenizer, mask_fraction: float | None = None):
        self.apply_fn = apply_fn
        self.parameters = parameters
        self.tokenizer = tokenizer
        self.mask_fraction = mask_fraction

    def score(self, sequence: str) -> float:
        import jax
        import jax.numpy as jnp

        token_ids = jnp.asarray(self.tokenizer.batch_tokenize([sequence])[0][1])
        special = {self.tokenizer.pad_token_id, self.tokenizer.class_token_id}
        real_positions = [i for i, t in enumerate(token_ids.tolist()) if t not in special]

        positions = real_positions
        if self.mask_fraction is not None:
            k = max(1, int(len(real_positions) * self.mask_fraction))
            positions = random.sample(real_positions, k)

        batch = jnp.stack([token_ids.at[p].set(self.tokenizer.mask_token_id) for p in positions])
        outs = self.apply_fn(self.parameters, jax.random.PRNGKey(0), batch)
        log_probs = jax.nn.log_softmax(outs["logits"], axis=-1)

        true_ids = token_ids[jnp.array(positions)]
        idx = jnp.arange(len(positions))
        scores = log_probs[idx, jnp.array(positions), true_ids]
        return float(jnp.mean(scores))
