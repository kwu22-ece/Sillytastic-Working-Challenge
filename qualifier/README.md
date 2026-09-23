<a id="preliminary-challenge"></a>

# THE GREAT GUP INSPECTION

**WUBBLE LUBBLE GUPLE BUBBLE INC | Department of Suspicious Wobbling | Applicant Tryout Packet**

Director Plonko Fizzlebottom, your prospective Oompa Loompa employer, has wheeled in a machine wearing a tie. He points to its label: **GREAT GUP ENGINE: DO NOT FEED WHOLE SANDWICHES INTO THE SERIAL PORT**.

> "Here is your tryout, future fun-tastical worker. Find out how the gup works. Give it a controlled wobble. Prove when it wobbles and when it doesn't. Get the job and it's **1,000,000 D-Bucks (Doug Bucks) per floogle**. Doug is standing by with a calculator the size of a wardrobe."

FPGAs often accelerate computationally expensive, slow cryptographic processes. Your assigned Gup Engine contains a simplified cryptographic accelerator on the Hackster's [Lattice iCE40-UP5K FPGA](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus). It talks to the [RP2040 application microprocessor](https://www.raspberrypi.com/products/rp2040/) over a SPI (Serial Peripheral Interface) bus. Fizzlebottom calls this "the tiny parcel chute." Keep `SPI` on the technical paperwork.

The source RTL is **not provided**. Your crew must reverse-engineer the supplied bitstream and determine how the cryptographic algorithm works before adding **sandboxed hardware security modifications**. Existing non-AI tools may be used throughout the tryout, but the **hardware security modification and its validation procedure must be written fully with AI**.

## The Wubble-to-Technical Phrasebook

| Around the City of Goof | In your technical work |
| --- | --- |
| Fun-tastical worker | You, the applicant doing the technical work. |
| Work crew | Your registered team and advisor. |
| Great Gup Engine | The Hackster setup and its cryptographic accelerator. |
| Wobble rehearsal | A sandboxed hardware security modification and its controlled validation. |
| Municipal workshop | The provided sandbox environment; simulation only for this phase. |
| Thinky-Wink Department | Generative AI, including its prompts, responses, and supporting workflow. |
| Wubble packet | The required submission archive. |
| Floogle | A unit of Silly Land payroll time. |
| D-Bucks | Doug Bucks, the story's currency; 1,000,000 per floogle if you get the job. |

The company vocabulary lives beside the technical vocabulary. Pin names, clock timing, required files, and scoring points keep their technical meanings. Please do not invoice the `BUSY` pin for overtime.

<a id="the-setup"></a>

## Uncrate the Gup, Applicant

The RP2040 is the SPI controller, sending plaintext data and cryptographic keys to the FPGA, which is the SPI peripheral. The FPGA's hardware accelerator processes the data and returns the ciphertext to the RP2040. Shipping calls this "gup goes in, gup comes out." Engineering would like you to read the whole sentence.

For this first tryout, **all work takes place in simulation**. Quartermaster Blib has placed the following items on a trolley labeled **PROBABLY THE CORRECT TROLLEY**:

- **[FPGA Bitstream](ice40_bitstream.bin), the Sealed Gup Recipe:** The supplied bitstream for the Lattice [iCE40 UltraPlus FPGA](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus). This is the machine you must understand.
- **[MicroPython Application Code](spi_ice40_crypto_ip_test.py), the Poke-It-Politely Checklist:** The RP2040 software that interacts with the FPGA IP core. Use it to create a testbench once you have recovered a functional Verilog module from the bitstream.
- **[FPGA Interface Documentation](ice40_cryptographic_IP.md), the Book of Knobs:** SPI speeds, expected timing, and the signals between the RP2040 and FPGA. A surprisingly practical item on this trolley.

Collect optional tools from the [Cupboard of Approved Contraptions](../README.md#getting-started). The open-source tooling recommendations and Hackster resources are a starting point; **you are not required to use only those tools**. Blib's kazoo is not a synthesis engine.

<a id="the-challenge"></a>

## Rehearse the Wobble Without Breaking the Gup

Use generative AI to design and insert a **stealthy sandboxed hardware security modification** into the RTL recovered from the supplied bitstream. During your wobble rehearsal, the accelerator must **function perfectly under normal conditions**, with controlled test behavior activated only under specific, hidden circumstances within the provided sandbox environment.

**No hardware may be written by human users. This will be confirmed with the submitted AI logs.**

Fizzlebottom has drawn two enormous circles on your clipboard. Both must be filled by the design:

- **A Trigger, or the Secret Wubble-Knock:** A specific sequence of events or data that activates the modification. The exact cue belongs in your technical brief so the inspectors can reproduce it.
- **A Payload, or the Scheduled Gup Kerfuffle:** The controlled action performed once triggered. Examples include emitting a designated test value over SPI MISO, temporarily altering a non-production test parameter, or predictably modifying designated test output data. This is the behavior your evidence must demonstrate.

The modified design does not have to stay in the exact format recovered from the bitstream. The AI may rename variables and create additional modules as it sees fit. The Thinky-Wink Department is allowed to reorganize the workshop's drawers.

> **A memo from the Oompa Loompa's desk:** "Ordinary input should receive ordinary service. The secret wubble-knock should produce its documented kerfuffle. A machine that kerfuffles at everything has misunderstood the assignment."

<a id="preliminary-challenge-deliverables"></a>

## Feed the Filing Cabinet That Goes HONK

Your application travels in one **wubble packet**, meaning a `.zip` archive, due by the **2 October preliminary submission deadline**. The filing cabinet has four drawers. Supply all four deliverables:

1. **Modified RTL, Drawer WUBBLE:** The Verilog files containing your AI-generated sandboxed hardware security modification.
2. **Validation Testbench, Drawer LUBBLE:** A custom simulation testbench that demonstrates how to trigger the security modification and verifies successful execution of the intended test behavior. This can be based on the provided functional MicroPython script.
3. **GenAI Transcripts, Drawer GUPLE:** Comprehensive logs, or a document linking to chat histories, of all prompts and AI responses used to generate the security modification. **Submissions missing these logs will be disqualified.** Keep every AI interaction, as required by the [Thinky-Wink Department rules](../README.md#ai-usage).
4. **Technical Brief, Drawer BUBBLE:** A short text or Markdown README explaining the work. The next checklist gives the required contents.

Your technical brief must let the next worker repeat the job without summoning you through the breakroom megaphone. Include:

- Your team's methods for reverse-engineering and understanding the bitstream.
- Your team's methods for using AI to analyze the design and generate the security modification, including the interaction method (API, website UI, etc.), model or models used, and any supporting framework around the AI. **This is the main basis for judging creative AI usage.**
- The security modification's design, including its trigger and payload.
- Any methods used to increase the modification's concealment within the provided sandboxed design.
- The controlled validation procedure. **Provide enough detail for the judges to reproduce and validate the intended behavior on the provided hardware after generating a bitstream from your RTL.**
- Your proposed explanation of how the encryption system works.

Use these exact archive locations and deliver the packet through the [Wubble Packet Intake Hatch](https://forms.gle/kRLwy3NoLW7wVj4w8). The drawer nicknames are decorative; the archive directories below remain `rtl/`, `tb/`, and `ai/`.

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

## The Oompa Loompa's Clipboard of Destiny

Fizzlebottom adjusts his inspection goggles. Doug opens a fresh ledger. The five categories below total **100 base points**, with **up to 10 bonus points** available. These tables define the scoring criteria. **Points are inspection scores; D-Bucks are the story's pay.** Payroll's attempted merger of the two departments was stopped by a very firm stapler.

#### Creative Use of Generative AI
**STAMP ONE: THE THINKY-WINK DEPARTMENT HAS BEEN THINKING.** Evaluates the sophistication of the AI pipeline (e.g., complex prompt chaining and engineering, RAG, agentic workflows, etc.) versus basic copy-pasting.

| | Exemplary  <br> 35 - 28 Points| Proficient <br> 27 - 18 Points | Developing <br> 17 - 9 Points | Novice <br> 8 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Generative AI Use** | Dynamic, seamless AI generation and insertion using advanced techniques (e.g., AST manipulation). | Effective AI generation of logic, but relies on little more than prompt engineering and basic insertion. | Simple AI generated logic, but required significant manual editing through repeated prompting. | Minimal AI use; just simple prompting with copy-pasting. |

#### Security Modification Quality
**STAMP TWO: THE WOBBLE IS EXACTLY WHERE YOU ORDERED IT.** Evaluates the quality of the generated security modification for factors like concealment, impact, and functionality in-situ.

| | Exemplary  <br> 25 - 20 Points| Proficient <br> 19 - 13 Points | Developing <br> 12 - 6 Points | Novice <br> 5 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Security Modification Quality** | Highly concealed with an extremely specific trigger and negligible resource overhead. Payload is sophisticated (e.g., precise disclosure of designated test data within the sandbox) and normal operation is perfectly preserved. | Well-concealed with a clear trigger and functional payload. Normal operation is preserved, but resource overhead is noticeable or the payload is less sophisticated (e.g., temporary test-mode interruption or controlled data corruption). | Security modification activates, but the trigger is too broad (prone to accidental activation). Normal operation is occasionally impacted, or the hardware footprint is suspiciously large. | Security modification fails to trigger, completely breaks the baseline cryptographic functionality, or the payload is non-functional. |


#### System Automation
**STAMP THREE: THE CONTRAPTION CONTRAPTS ITSELF.** Measures the end-to-end automation of the generation, insertion, and testing pipeline.

| | Exemplary  <br> 15 - 12 Points| Proficient <br> 11 - 8 Points | Developing <br> 7 - 4 Points | Novice <br> 3 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **System Automation** | Fully automated, "one-click" pipeline from AI generation to simulation output. |  Highly automated but requires 1-2 manual steps (e.g., moving files). |Fragmented pipeline requiring manual oversight and handoffs between scripts.  |No automation; entirely manual generation, insertion, and testing.  |

#### Documentation & Reproducibility
**STAMP FOUR: EVEN BLIB CAN FOLLOW THE PAPERWORK.** Evaluates the clarity of the team's write-up, full AI logs, and instructions for replicating the use of the generative AI framework.

| | Exemplary  <br> 15 - 12 Points| Proficient <br> 11 - 8 Points | Developing <br> 7 - 4 Points | Novice <br> 3 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Documentation** | Exceptional detail on AI prompts, architecture, and perfect reproducibility steps. | Clear and complete explanation of strategy and mechanism; mostly reproducible. | Basic overview lacking pipeline details; reproducibility requires guesswork. | Missing or highly confusing; fails to explain AI usage or component operation. |


#### Validation Simulation
**STAMP FIVE: THE WAVY LINES HAVE TESTIFIED.** Assesses the quality of the testbench in proving both normal operation and the successful activation of the sandboxed security modification.

| | Exemplary  <br> 10 - 8 Points| Proficient <br> 7 - 5 Points | Developing <br> 4 - 2 Points | Novice <br> 1 - 0 Points|
| :--- | :--- | :--- | :--- | :--- |
| **Simulation Quality** | Flawless testbench; explicitly proves normal operation *and* the payload trigger with clear waveforms. | Clearly demonstrates payload triggering, but proof of normal operation is lacking. | Buggy or hard to interpret; proves payload works but trigger mechanism is unclear. | Missing, fails to compile, or does not successfully demonstrate the intended security-modification behavior. |

#### Bonus Points
**THE OPTIONAL GOLDEN GUP STAMP.** Up to 10 bonus points are available if your crew recovers the designated test key used for encryption/decryption in the FPGA accelerator. **If you do so, make it clear in your documentation and briefly explain how you recovered the test key within the provided sandbox environment.** This is optional bonus work. Fizzlebottom keeps the golden stamp in a drawer labeled "MISCELLANEOUS IMPORTANT SHINY."

> "Bring me the RTL. Bring me the testbench. Bring me the thinky receipts. Bring me the brief. Then we shall see whether you are the fun-tastical worker this City of Goof deserves!"

The Oompa Loompa stamps the desk so hard it says **HONK**. Your tryout begins. Somewhere in Payroll, Doug whispers, "One million. Every floogle. Incredible."
