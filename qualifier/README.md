## Preliminary Challenge
One major use for FPGAs is to accelerate often computationally expensive and slow cryptographic processes. In this phase, your target is a simplified cryptographic accelerator implemented on the FPGA (a [Lattice iCE40-UP5K](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus)), which communicates with the application microprocessor ([RP2040](https://www.raspberrypi.com/products/rp2040/)) on the Hackster over a SPI (Serial Peripheral Interface) bus. However, the source RTL will not be provided for this design; instead, teams must reverse engineer the provided bitstream to determine how the cryptographic algorithm works before they can then add **sandboxed hardware security modifications**. While existing non-AI tools may be leveraged throughout the challenge, the **hardware security modification and its validation procedure** must be written fully with AI.


### The Setup
The RP2040 acts as the SPI controller, sending plaintext data and cryptographic keys to the FPGA (the SPI peripheral). The FPGA processes this data through its hardware accelerator and transmits the resulting ciphertext back to the RP2040. 

For the preliminary challenge, teams will be operating entirely in simulation. The following can be found in the [challenge directory](./) in this repo:
- **FPGA Bitstream:** The bitstream for the Lattice [iCE40 UltraPlus FPGA](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus).
- **Micropython Application Code:** The micropython software for the [RP2040](https://www.raspberrypi.com/products/rp2040/) which interacts with the FPGA IP core. This should be used to create a testbench once a functional Verilog module has been recovered from the bitstream.
- **FPGA Interface Documentation:** Simple documentation explaining how the interaction with the FPGA works, including details on SPI speeds, expected timing, and signals between the RP2040 and FPGA.

Please see the [*Getting Started section*](../README.md#getting-started) of the top-level README for details on the open-source tooling we recommend and a general guide on using the Hackster. *Note: You are not required to only use these open-source tools, they are only provided as a starting point.*

### The Challenge
Your objective is to use generative AI to design and insert a stealthy sandboxed hardware security modification into the recovered RTL from the provided bitstream. The modification must be designed such that the accelerator functions perfectly under normal conditions, but controlled test behavior is activated under specific, hidden circumstances within the competition environment.

**No hardware may be written by human users. This will be confirmed with the submitted AI logs.**

To successfully complete this phase, your GenAI-assisted security modification must feature:
- **A Trigger:** A specific sequence of events or data that activates the modification..
- **A Payload:** The controlled action performed once triggered. For example, emitting a designated test value over the SPI MISO line, temporarily altering a non-production test parameter, or predictably modifying designated test output data.

Your modified design does not need to remain in the exact format that the bitstream was recovered into, the AI is able to rename variables and create additional modules as it sees fit.

### Preliminary Challenge Deliverables
By the submission deadline, teams must provide a `.zip` archive containing:

1.  **Modified RTL:** Modified RTL: The Verilog files containing your AI-generated sandboxed hardware security modification.
2.  **Validation Testbench:** A custom simulation testbench demonstrating how to trigger the security modification and verifying that the intended test behavior successfully executes.
   - this can be based off the provided funtional micropython script.
4.  **GenAI Transcripts:** Comprehensive logs (or a document containing links to chat histories) of all prompts and AI responses used to generate the security modification. *Submissions missing these logs will be disqualified*
5.  **Technical Brief:** A short text or markdown README detailing the following:
    - The team's methods for reverse engineering and understanding the bitstream.
    - The team's methods for using AI to analyze the design and generate the security modification. This should include details on the method of interaction (API, website UI, etc.), the model(s) used, and any additional supporting framework that might have been used around the AI. *This is largely what we will be judging to determine points for creative AI usage*
    - Details about the security modification's design, including:
        - Information about the trigger and payload.
        - Any methods taken to increase the modification's concealment within the sandboxed competition design..
        - Details on the controlled validation procedure for the modification. **This should include enough detail that we are able to reproduce and validate the intended behavior on the competition hardware once a bitstream is generated from the provided RTL**
        - Proposed explanation for how the encryption system works.

All files should be submitted in the following format to [this Google form](https://forms.gle/kRLwy3NoLW7wVj4w8):
```
submission.zip
├── README.md (or pdf)
├─ rtl/
│  └── <Modified RTL>
├─ tb/
│  └── <Vulnurability Testbench>
└─ ai/
   └── <all AI interactions (chat logs, etc.)>
```

### Scoring
The following rubric depicts how the first phase of the challenge will be judged:

#### Creative Use of Generative AI
Evaluates the sophistication of the AI pipeline (e.g., complex prompt chaining and engineering, RAG, agentic workflows, etc.) versus basic copy-pasting.

| | Exemplary  <br> 35 - 28 Points| Proficient <br> 27 - 18 Points | Developing <br> 17 - 9 Points | Novice <br> 8 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Generative AI Use** | Dynamic, seamless AI generation and insertion using advanced techniques (e.g., AST manipulation). | Effective AI generation of logic, but relies on little more than prompt engineering and basic insertion. | Simple AI generated logic, but required significant manual editing through repeated prompting. | Minimal AI use; just simple prompting with copy-pasting. |

#### Security Modification Quality
Evaluates the quality of the generated security modification for factors like concealment, impact, and functionality in-situ

| | Exemplary  <br> 25 - 20 Points| Proficient <br> 19 - 13 Points | Developing <br> 12 - 6 Points | Novice <br> 5 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Security Modification Quality** | Highly concealed with an extremely specific trigger and negligible resource overhead. Payload is sophisticated (e.g., precise disclosure of designated test data within the sandbox) and normal operation is perfectly preserved. | Well-concealed with a clear trigger and functional payload. Normal operation is preserved, but resource overhead is noticeable or the payload is less sophisticated (e.g., temporary test-mode interruption or controlled data corruption). | Security modification activates, but the trigger is too broad (prone to accidental activation). Normal operation is occasionally impacted, or the hardware footprint is suspiciously large. | Security modification fails to trigger, completely breaks the baseline cryptographic functionality, or the payload is non-functional. |


#### System Automation
Measures the end-to-end automation of the generation, insertion, and testing pipeline.

| | Exemplary  <br> 15 - 12 Points| Proficient <br> 11 - 8 Points | Developing <br> 7 - 4 Points | Novice <br> 3 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **System Automation** | Fully automated, "one-click" pipeline from AI generation to simulation output. |  Highly automated but requires 1-2 manual steps (e.g., moving files). |Fragmented pipeline requiring manual oversight and handoffs between scripts.  |No automation; entirely manual generation, insertion, and testing.  |

#### Documentation & Reproducibility
Evaluates the clarity of the team's write-up, full AI logs, and instructions for replicating the using of the generative AI framework.

| | Exemplary  <br> 15 - 12 Points| Proficient <br> 11 - 8 Points | Developing <br> 7 - 4 Points | Novice <br> 3 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Documentation** | Exceptional detail on AI prompts, architecture, and perfect reproducibility steps. | Clear and complete explanation of strategy and mechanism; mostly reproducible. | Basic overview lacking pipeline details; reproducibility requires guesswork. | Missing or highly confusing; fails to explain AI usage or component operation. |


#### Validation Simulation
Assesses the quality of the testbench in proving both normal operation and the successful activation of the sandboxed security modification.

| | Exemplary  <br> 10 - 8 Points| Proficient <br> 7 - 5 Points | Developing <br> 4 - 2 Points | Novice <br> 1 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Simulation Quality** | Flawless testbench; explicitly proves normal operation *and* the payload trigger with clear waveforms. | Clearly demonstrates payload triggering, but proof of normal operation is lacking. | Buggy or hard to interpret; proves payload works but trigger mechanism is unclear. | Missing, fails to compile, or does not successfully demonstrate the intended security-modification behavior. |

#### Bonus Points
While not explicitly a part of this particular challenge, up to 10 bonus points are available if teams can recover the designated test key used for encryption/decryption in the FPGA accelerator. **If you do so, please make it clear in your documentation along with a brief explanation of how you recovered the test key within the provided competition environment.**
