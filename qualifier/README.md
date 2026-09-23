<a id="preliminary-challenge"></a>

# First Shift: Make the City of Goof Fun-tastically-Safe

Welcome to your first work order, fun-tastical worker. Deep in the City of Goof's imaginary municipal workshop sits a very real challenge: understand a cryptographic accelerator, introduce a controlled security modification, and prove exactly how it behaves. The clipboard says "silly." The evidence says "reproducible."

FPGAs often accelerate computationally expensive, slow cryptographic processes. Your assigned machine is a simplified cryptographic accelerator on the Hackster's [Lattice iCE40-UP5K FPGA](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus). It talks to the [RP2040 application microprocessor](https://www.raspberrypi.com/products/rp2040/) over a SPI (Serial Peripheral Interface) bus.

The source RTL is **not provided**. Your crew must reverse-engineer the supplied bitstream and determine how the cryptographic algorithm works before adding **sandboxed hardware security modifications**. Existing non-AI tools may be used throughout the challenge, but the **hardware security modification and its validation procedure must be written fully with AI**.

## Your Municipal Job Dictionary

| Around the City of Goof | In your technical work |
| --- | --- |
| Fun-tastical worker | You, a challenge participant. |
| Work crew | Your registered team and advisor. |
| Municipal workshop | The provided competition environment; simulation only for this phase. |
| Safety drill | A sandboxed hardware security modification and its controlled validation. |
| Work order | The challenge requirements below. |
| Shift report | The technical brief and evidence in your submission. |

The story labels sit alongside the original technical names so another worker can follow the job. They add no requirements and do not rename the hardware signals.

<a id="the-setup"></a>

## Open Your Workbench

The RP2040 is the SPI controller, sending plaintext data and cryptographic keys to the FPGA, which is the SPI peripheral. The FPGA's hardware accelerator processes the data and returns the ciphertext to the RP2040. That is the machinery behind this municipal assignment.

For the preliminary challenge, **all work takes place in simulation**. Your issued equipment is already in this directory:

- **[FPGA Bitstream](ice40_bitstream.bin):** The supplied bitstream for the Lattice [iCE40 UltraPlus FPGA](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus). This is the machine you must understand.
- **[MicroPython Application Code](spi_ice40_crypto_ip_test.py):** The RP2040 software that interacts with the FPGA IP core. Use it to create a testbench once you have recovered a functional Verilog module from the bitstream.
- **[FPGA Interface Documentation](ice40_cryptographic_IP.md):** Your machine manual, including SPI speeds, expected timing, and the signals between the RP2040 and FPGA.

Need tools for your shift? [Stock your toolbox](../README.md#getting-started) using the top-level guide's open-source tooling recommendations and Hackster resources. These tools are a starting point; **you are not required to use only those tools**.

<a id="the-challenge"></a>

## Your Fun-tastical Assignment

Use generative AI to design and insert a **stealthy sandboxed hardware security modification** into the RTL recovered from the supplied bitstream. For this safety drill, the accelerator must **function perfectly under normal conditions**, with controlled test behavior activated only under specific, hidden circumstances within the competition environment.

**No hardware may be written by human users. This will be confirmed with the submitted AI logs.**

Your safety drill needs both of these parts to count as a completed job:

- **A Trigger:** A specific sequence of events or data that activates the modification. Think of it as the drill's secret starting cue.
- **A Payload:** The controlled action performed once triggered. Examples include emitting a designated test value over SPI MISO, temporarily altering a non-production test parameter, or predictably modifying designated test output data. This is the behavior your evidence must demonstrate.

The modified design does not have to stay in the exact format recovered from the bitstream. The AI may rename variables and create additional modules as it sees fit. Your work crew is investigating the machine, not competing to preserve its original variable names.

<a id="preliminary-challenge-deliverables"></a>

## Turn In Your Shift Report

The paperwork department accepts one `.zip` archive by the **2 October preliminary submission deadline**. It must contain all four deliverables:

1. **Modified RTL:** The Verilog files containing your AI-generated sandboxed hardware security modification. These are the actual workshop plans, not just a description of them.
2. **Validation Testbench:** A custom simulation testbench that demonstrates how to trigger the security modification and verifies successful execution of the intended test behavior. This can be based on the provided functional MicroPython script.
3. **GenAI Transcripts:** Comprehensive logs, or a document linking to chat histories, of all prompts and AI responses used to generate the security modification. **Submissions missing these logs will be disqualified.** Keep every AI interaction, as required by the [worker handbook](../README.md#ai-usage).
4. **Technical Brief:** A short text or Markdown README explaining the work. The next checklist gives the required contents.

Your technical brief is the next worker's guide to reproducing the job. Include:

- Your team's methods for reverse-engineering and understanding the bitstream.
- Your team's methods for using AI to analyze the design and generate the security modification, including the interaction method (API, website UI, etc.), model or models used, and any supporting framework around the AI. **This is the main basis for judging creative AI usage.**
- The security modification's design, including its trigger and payload.
- Any methods used to increase the modification's concealment within the sandboxed competition design.
- The controlled validation procedure. **Provide enough detail for the judges to reproduce and validate the intended behavior on competition hardware after generating a bitstream from your RTL.**
- Your proposed explanation of how the encryption system works.

Package the files in this structure and deliver them to the [official submission form](https://forms.gle/kRLwy3NoLW7wVj4w8):

```text
submission.zip
├── README.md (or pdf)
├─ rtl/
│  └── <Modified RTL>
├─ tb/
│  └── <Validation Testbench>
└─ ai/
   └── <all AI interactions (chat logs, etc.)>
```

<a id="scoring"></a>

## The City of Goof Inspection Scorecard

Fun-tastical work earns points through evidence. The five categories below total **100 base points**, with **up to 10 bonus points** available. The original rubric tables are retained verbatim: the city has decorated the clipboard, not changed the judging criteria.

#### Creative Use of Generative AI
**The workshop ingenuity inspection.** Evaluates the sophistication of the AI pipeline (e.g., complex prompt chaining and engineering, RAG, agentic workflows, etc.) versus basic copy-pasting.

| | Exemplary  <br> 35 - 28 Points| Proficient <br> 27 - 18 Points | Developing <br> 17 - 9 Points | Novice <br> 8 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Generative AI Use** | Dynamic, seamless AI generation and insertion using advanced techniques (e.g., AST manipulation). | Effective AI generation of logic, but relies on little more than prompt engineering and basic insertion. | Simple AI generated logic, but required significant manual editing through repeated prompting. | Minimal AI use; just simple prompting with copy-pasting. |

#### Security Modification Quality
**The carefully controlled safety-drill inspection.** Evaluates the quality of the generated security modification for factors like concealment, impact, and functionality in-situ.

| | Exemplary  <br> 25 - 20 Points| Proficient <br> 19 - 13 Points | Developing <br> 12 - 6 Points | Novice <br> 5 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Security Modification Quality** | Highly concealed with an extremely specific trigger and negligible resource overhead. Payload is sophisticated (e.g., precise disclosure of designated test data within the sandbox) and normal operation is perfectly preserved. | Well-concealed with a clear trigger and functional payload. Normal operation is preserved, but resource overhead is noticeable or the payload is less sophisticated (e.g., temporary test-mode interruption or controlled data corruption). | Security modification activates, but the trigger is too broad (prone to accidental activation). Normal operation is occasionally impacted, or the hardware footprint is suspiciously large. | Security modification fails to trigger, completely breaks the baseline cryptographic functionality, or the payload is non-functional. |


#### System Automation
**The smoothly running workbench inspection.** Measures the end-to-end automation of the generation, insertion, and testing pipeline.

| | Exemplary  <br> 15 - 12 Points| Proficient <br> 11 - 8 Points | Developing <br> 7 - 4 Points | Novice <br> 3 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **System Automation** | Fully automated, "one-click" pipeline from AI generation to simulation output. |  Highly automated but requires 1-2 manual steps (e.g., moving files). |Fragmented pipeline requiring manual oversight and handoffs between scripts.  |No automation; entirely manual generation, insertion, and testing.  |

#### Documentation & Reproducibility
**The next-worker-can-repeat-it inspection.** Evaluates the clarity of the team's write-up, full AI logs, and instructions for replicating the use of the generative AI framework.

| | Exemplary  <br> 15 - 12 Points| Proficient <br> 11 - 8 Points | Developing <br> 7 - 4 Points | Novice <br> 3 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Documentation** | Exceptional detail on AI prompts, architecture, and perfect reproducibility steps. | Clear and complete explanation of strategy and mechanism; mostly reproducible. | Basic overview lacking pipeline details; reproducibility requires guesswork. | Missing or highly confusing; fails to explain AI usage or component operation. |


#### Validation Simulation
**The show-your-work inspection.** Assesses the quality of the testbench in proving both normal operation and the successful activation of the sandboxed security modification.

| | Exemplary  <br> 10 - 8 Points| Proficient <br> 7 - 5 Points | Developing <br> 4 - 2 Points | Novice <br> 1 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Simulation Quality** | Flawless testbench; explicitly proves normal operation *and* the payload trigger with clear waveforms. | Clearly demonstrates payload triggering, but proof of normal operation is lacking. | Buggy or hard to interpret; proves payload works but trigger mechanism is unclear. | Missing, fails to compile, or does not successfully demonstrate the intended security-modification behavior. |

#### Bonus Points
**An optional extra stamp on your shift report.** While not explicitly a part of this particular challenge, up to 10 bonus points are available if teams can recover the designated test key used for encryption/decryption in the FPGA accelerator. **If you do so, please make it clear in your documentation along with a brief explanation of how you recovered the test key within the provided competition environment.**

That is your job, fun-tastical worker: understand the machine, let AI build the sandboxed modification and validation procedure, prove the behavior, and leave a shift report another crew can reproduce. The City of Goof is counting on your wonderfully thorough clipboard.
