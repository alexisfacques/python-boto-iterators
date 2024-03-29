"""Type hints for iterator bolts."""
from typing import Any, Callable, Dict, Iterator, Optional, Tuple, Union

# From requirements.txt:
import boto3

BoltItem = Dict[str, Any]
IteratorBolt = Callable[[Iterator[BoltItem], boto3.session.Session], Iterator[BoltItem]]

ChainResolver = Callable[[int], Dict[str, Any]]
IteratorChain = Union[Callable[[], Tuple[IteratorBolt, ...]],
                      Callable[[Dict[str, Any]], Tuple[IteratorBolt, ...]],
                      Callable[[Dict[str, Any], Optional[Any]], Tuple[IteratorBolt, ...]],
                      Callable[[Dict[str, Any], Optional[Any], ChainResolver], Tuple[IteratorBolt, ...]]]
