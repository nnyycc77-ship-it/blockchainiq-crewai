"""Run the Blockchain IQ brief tool once and print the response proof.

Setup:
    pip install -e .
    export AGENT_PRIVATE_KEY=0x...   # dedicated wallet, a little USDC on Base

Run:
    python examples/run_brief.py

To use the tool inside a crew, pass BlockchainIQBriefTool() in an
Agent's tools list; this example runs the tool directly so the call
and its response proof can be verified on their own.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from blockchainiq_crewai import BlockchainIQBriefTool


def main() -> None:
    tool = BlockchainIQBriefTool()
    result = json.loads(tool.run())
    print(json.dumps(result["data"], indent=2))
    proof = result["settlement"]
    print("\nSettlement proof:")
    print(f"  success:     {proof['success']}")
    print(f"  payer:       {proof['payer']}")
    print(f"  network:     {proof['network']}")
    print(f"  transaction: {proof['transaction']}")


if __name__ == "__main__":
    main()
