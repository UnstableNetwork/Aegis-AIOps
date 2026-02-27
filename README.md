# Aegis AIOps: Autonomous Network Remediation

Aegis is a next-generation Closed-Loop Remediation system. It combines Layer 2 network telemetry with Local AI (LLMs) to detect and neutralize network threats in real-time.

## Key Features
- AI-Driven Auditing: Uses local Llama 3 via Ollama to analyze unknown devices—no data ever leaves your network.
- Automated Isolation: Directly interfaces with Cisco/Enterprise switches to shut down rogue ports via Netmiko.
- Privacy-First: Designed for high-security environments where cloud-based AI is prohibited.

## Architecture
1. Monitor: aegis_core.py sniffs ARP traffic for unauthorized MAC addresses.
2. Analyze: brain.py passes device metadata to the LLM for threat assessment.
3. Execute: actions.py executes the mitigation playbook on the hardware layer.

## Installation

pip install -r requirements.txt
python aegis_core.py
