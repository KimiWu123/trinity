from typing import Sequence

from eth.constants import ZERO_HASH32
from eth_typing import Hash32
from eth_utils import encode_hex, humanize_hash
import ssz
from ssz.sedes import Vector, bytes32

from eth2.beacon.constants import DEPOSIT_CONTRACT_TREE_DEPTH

from .defaults import default_tuple_of_size
from .deposit_data import DepositData, default_deposit_data

DEPOSIT_PROOF_VECTOR_SIZE = DEPOSIT_CONTRACT_TREE_DEPTH + 1

default_proof_tuple = default_tuple_of_size(DEPOSIT_PROOF_VECTOR_SIZE, ZERO_HASH32)


class Deposit(ssz.Serializable):
    """
    A :class:`~eth2.beacon.types.deposits.Deposit` contains the data represented by an instance
    of :class:`~eth2.beacon.types.deposit_data.DepositData`, along with a Merkle proof that can be
    used to verify inclusion in the canonical deposit tree.
    """

    fields = [
        # Merkle path to deposit root
        ("proof", Vector(bytes32, DEPOSIT_PROOF_VECTOR_SIZE)),
        ("data", DepositData),
    ]

    def __init__(
        self,
        proof: Sequence[Hash32] = default_proof_tuple,
        data: DepositData = default_deposit_data,
    ) -> None:
        super().__init__(proof, data)

    def __str__(self) -> str:
        return (
            f"[hash_tree_root]={humanize_hash(self.hash_tree_root)}, data=({self.data})"
        )
