<a id="preliminary-challenge"></a>

# THE GREAT GUP INSPECTION

**WUBBLE LUBBLE GUPLE BUBBLE INC | Department of Suspicious Wobbling | Applicant Tryout Packet**

Director Plonko Fizzlebottom, your prospective Oompa Loompa employer, has wheeled in a machine wearing a tie. He points to its label: **GREAT GUP ENGINE: DO NOT FEED WHOLE SANDWICHES INTO THE SERIAL PORT**.

> "Here is your tryout, future fun-tastical worker. Find out how the gup works. Give it a controlled wobble. Prove when it wobbles and when it doesn't. Get the job and it's **1,000,000 D-Bucks (Doug Bucks) per floogle**. Doug is standing by with a calculator the size of a wardrobe."

Your assigned Gup Engine uses a shape-changing beep-boop tile to speed up the slow work of scrambling and unscrambling little words. Its delivery-slip name is [Lattice iCE40-UP5K](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus), an FPGA. The [RP2040 day-job brain](https://www.raspberrypi.com/products/rp2040/) chats with it through the tiny parcel chute, whose connector label is `SPI` (Serial Peripheral Interface). The chute transports bits; Blib's sandwich remains entirely too large.

The original machine-building recipe, called RTL, is **not provided**. Your crew must unpick the supplied sealed `.bin` recipe and work out how the scrambling recipe operates before adding a **hidden safety-drill addition inside the sandbox**. Existing non-AI tools may be used throughout the tryout, but the **safety-drill addition and its checking procedure must be written fully with AI**.

<a id="the-wubble-to-technical-phrasebook"></a>

## The Company's Beep-Boop Phrasebook

| Around the City of Goof | What goes on your workbench |
| --- | --- |
| Fun-tastical worker | You, the applicant doing the wonderfully wobbly work. |
| Work crew | Your registered team and advisor. |
| Great Gup Engine | The supplied board and its little word-scrambling machine. |
| Beep boop magic screen changing | Writing or editing instructions and machine-building recipes on your screen. |
| Machine-building recipe | RTL written in Verilog; these files describe the circuits to build. |
| Sealed gup recipe | The supplied FPGA bitstream, `ice40_bitstream.bin`. |
| Pretend workbench | Simulation, where the machine runs as a model instead of on a physical board. |
| Poke-and-prove checker | A testbench that drives the pretend machine and checks its behavior. |
| Gup scrambling / unscrambling | Encryption / decryption of the little words. |
| Secret wubble-knock / kerfuffle | The trigger that activates the addition / the payload behavior it produces. |
| Wobble rehearsal | A hidden safety-drill addition inside the sandbox and a controlled check of its behavior. |
| Municipal workshop | The provided sandbox environment; simulation only for this phase. |
| Thinky-Wink Department | Generative AI, including its prompts, responses, and supporting workflow. |
| Wubble packet | The required submission archive. |
| Floogle | A unit of Silly Land payroll time. |
| D-Bucks | Doug Bucks, the story's currency; 1,000,000 per floogle if you get the job. |

Fizzlebottom has approved these words with a stamp shaped like an exclamation mark. The connector labels, clock timing, required file formats, and scoring points below still tell you exactly what to build and demonstrate. Please do not invoice the `BUSY` pin for overtime.

<a id="the-setup"></a>

## Uncrate the Gup, Applicant

The RP2040 day-job brain is the SPI controller: it sends plain-word parcels and scrambling keys to the FPGA tile, the SPI peripheral. The tile's scrambling machine processes the parcels and returns the scrambled words to the RP2040. Shipping calls this "gup goes in, gup comes out." Dispatch adds a stamp reading DELIGHTFULLY DELIVERED.

For this first tryout, **all work takes place on the pretend workbench (simulation)**. Quartermaster Blib has placed the following items on a trolley labeled **PROBABLY THE CORRECT TROLLEY**:

- **[The Sealed Gup Recipe](ice40_bitstream.bin):** The supplied bitstream for the [iCE40 UltraPlus shape-changing tile](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus). This is the machine you must understand.
- **[The Poke-It-Politely Checklist](spi_ice40_crypto_ip_test.py):** The MicroPython beep-boop instructions that let the RP2040 interact with the tile's scrambling machine. Use them to create a poke-and-prove checker once you have recovered a working Verilog machine recipe from the sealed gup.
- **[The Book of Knobs](ice40_cryptographic_IP.md):** Parcel-chute speeds, expected timing, and signals between the RP2040 and FPGA. A surprisingly practical item on this trolley.

Collect optional tools from the [Cupboard of Approved Contraptions](../README.md#getting-started). The open-source contraptions and Gup Engine assembly scrolls are a starting point; **you are not required to use only those tools**. Blib's kazoo has yet to turn a recipe into a working machine.

<a id="the-challenge"></a>

## Rehearse the Wobble Without Breaking the Gup

Ask the Thinky-Wink Department's AI helpers to invent and fit a **well-hidden safety-drill addition inside the sandbox**, using the machine-building recipe recovered from the supplied sealed gup. During the wobble rehearsal, the scrambling machine must **function perfectly under normal conditions**, with controlled test behavior activated only under specific, hidden circumstances within the provided sandbox environment.

**No machine-building recipes may be written by human users. This will be confirmed with the submitted AI logs.** All that recipe-writing beep boop magic screen changing belongs to the AI helpers.

Fizzlebottom has drawn two enormous circles on your clipboard. Both must be filled by the design:

- **The Secret Wubble-Knock:** A specific sequence of events or data that activates the addition. The exact cue belongs in your how-it-wubbles report so the inspectors can reproduce it.
- **The Scheduled Gup Kerfuffle:** The controlled action performed once triggered. Examples include sending a designated test value over `SPI MISO`, temporarily altering a setting reserved for tests, or predictably changing designated test output data. This is the behavior your evidence must demonstrate.

The changed recipe does not have to stay in the exact form recovered from the sealed gup. The AI may rename its variables and create additional recipe modules as it sees fit. The Thinky-Wink Department is allowed to reorganize the workshop's drawers.

> **A memo from the Oompa Loompa's desk:** "Ordinary input should receive ordinary service. The secret wubble-knock should produce its documented kerfuffle. A machine that kerfuffles at everything has misunderstood the assignment."

<a id="preliminary-challenge-deliverables"></a>

## Feed the Filing Cabinet That Goes HONK

Your application travels in one **wubble packet**, meaning a `.zip` archive, due by the **2 October preliminary submission deadline**. The filing cabinet has four drawers. Supply all four deliverables:

1. **Changed Machine Recipes, Drawer WUBBLE:** The Verilog RTL files containing your AI-generated hidden safety-drill addition inside the sandbox.
2. **Poke-and-Prove Checker, Drawer LUBBLE:** A custom simulation testbench that demonstrates the secret wubble-knock and verifies that its intended kerfuffle successfully happens. This can be based on the supplied working MicroPython checklist.
3. **Thinky Receipts, Drawer GUPLE:** Comprehensive logs, or a document linking to chat histories, of all prompts and AI responses used to generate the addition. **Submissions missing these logs will be disqualified.** Keep every AI interaction, as required by the [Thinky-Wink Department rules](../README.md#ai-usage).
4. **How-It-Wubbles Report, Drawer BUBBLE:** A short text or Markdown README explaining the work. The next checklist gives the required contents.

Your how-it-wubbles report must let the next worker repeat the job without summoning you through the breakroom megaphone. Include:

- How your team unpicked and understood the sealed gup recipe.
- How your team used AI to inspect the machine recipe and create the addition, including how you spoke to it (API, website UI, etc.), which model or models you used, and any helper framework around the AI. **This is the main basis for the Thinky-Wink Sparklecraft score.**
- How the hidden addition is built, including its secret wubble-knock and scheduled kerfuffle.
- Any methods used to keep the addition concealed within the provided sandboxed design.
- The controlled checking procedure. **Give the inspectors enough detail to repeat and check the intended behavior on the physical machine after turning your RTL recipe into a bitstream.**
- Your proposed explanation of how the word-scrambling system works.

Use these exact archive locations and deliver the packet through the [Wubble Packet Intake Hatch](https://forms.gle/kRLwy3NoLW7wVj4w8). The drawer nicknames are decorative; the archive directories below remain `rtl/`, `tb/`, and `ai/`.

```text
submission.zip
├── README.md (or pdf)
├─ rtl/
│  └── <Changed machine recipes: Verilog RTL>
├─ tb/
│  └── <Poke-and-prove checker: simulation testbench>
└─ ai/
   └── <all AI interactions (chat logs, etc.)>
```

<a id="scoring"></a>

## The Oompa Loompa's Clipboard of Destiny

Fizzlebottom adjusts his inspection goggles. Doug opens a fresh ledger. The five categories below total **100 base points**, with **up to 10 bonus points** available. These tables define the scoring criteria. **Points are inspection scores; D-Bucks are the story's pay.** Payroll's attempted merger of the two departments was stopped by a very firm stapler.

<a id="creative-use-of-generative-ai"></a>

### 1. Thinky-Wink Sparklecraft

**Fizzlebottom's question:** "How splendidly did you get the artificial thinky department to do the beep boop magic screen changing?"

This stamp rewards the cleverness of the AI work parade: elaborate prompt chains, carefully shaped requests, fetching useful reference material for the AI (RAG), and coordinated AI helpers. Simple copy-pasting earns less sparkle.

| | GUP-TASTIC! <br> 35 - 28 Points | WUBBLE-WONDERFUL! <br> 27 - 18 Points | BUBBLING ALONG! <br> 17 - 9 Points | FIRST FLOOGLE! <br> 8 - 0 Points |
| :--- | :--- | :--- | :--- | :--- |
| **Thinky-Wink Sparklecraft** | HONK OF DISTINCTION! AI invents and fits the machine recipes together dynamically and smoothly, using advanced tricks such as rearranging instruction trees (AST manipulation). The whole thinky parade marches in step. | A splendid little thinky workshop! AI makes useful machine recipes, but the method mostly uses carefully written prompts and straightforward insertion into the machine. | The thinky bubbles are forming! AI makes simple machine recipes, but a human must steer many rounds of repeated prompting to revise them. Lots of hands-on shepherding remains. | Your first thinky toot! AI involvement is minimal: simple prompts and copy-pasting. The grand invention parade is still waiting outside. |

<a id="security-modification-quality"></a>

### 2. Secret Wobble Craftsmanship

**Fizzlebottom's question:** "Does the secret wubble-knock produce precisely the intended kerfuffle, while the ordinary gup keeps gupping?"

This stamp measures how well the hidden safety-drill addition blends in, what its controlled kerfuffle accomplishes, and how well it works inside the machine.

| | GUP-TASTIC! <br> 25 - 20 Points | WUBBLE-WONDERFUL! <br> 19 - 13 Points | BUBBLING ALONG! <br> 12 - 6 Points | FIRST FLOOGLE! <br> 5 - 0 Points |
| :--- | :--- | :--- | :--- | :--- |
| **Secret Wobble Craftsmanship** | A magnificently tucked-away wobble! Its secret knock is extremely specific and its extra machine-resource appetite is negligible. The kerfuffle is sophisticated, such as precisely revealing designated test data inside the sandbox. Ordinary gup service stays perfect. | A well-hidden wobble with a clear knock and a working kerfuffle! Ordinary gup service is preserved, but the extra resources are noticeable or the kerfuffle is simpler, such as briefly interrupting test mode or deliberately altering test data. | The wobble wakes up, but its knock is broad enough to set it off by accident. Ordinary gup service sometimes suffers, or the addition takes up a suspiciously large amount of machine space. Time for a careful tune-up, worker! | The wobble needs another workshop visit: it does not activate, completely breaks the ordinary scrambling-and-unscrambling service, or produces no working kerfuffle. Blib has kept your bench warm. |

<a id="system-automation"></a>

### 3. The Self-Running Beep-Boop Parade

**Fizzlebottom's question:** "How much of the work parade can march from invention to proof without somebody carrying each float?"

This stamp follows the whole journey: AI makes the addition, fits it into the design, and runs the pretend-workbench checks.

| | GUP-TASTIC! <br> 15 - 12 Points | WUBBLE-WONDERFUL! <br> 11 - 8 Points | BUBBLING ALONG! <br> 7 - 4 Points | FIRST FLOOGLE! <br> 3 - 0 Points |
| :--- | :--- | :--- | :--- | :--- |
| **Self-Running Beep-Boop Parade** | ONE CLICK, WHOLE PARADE! Everything runs automatically from AI invention through insertion to pretend-workbench results. Fizzlebottom waves a tiny flag at the finished output. | Almost a self-marching parade! Most work runs automatically, with just 1-2 manual steps, such as moving files between desks. | Several cheerful floats, but someone must supervise them and hand work between separate instruction checklists. The parade keeps asking for directions. | Every float needs carrying: generation, insertion, and testing are all manually orchestrated. The self-running machinery has yet to join the procession. |

<a id="documentation--reproducibility"></a>

### 4. The Next Worker Can Do It Too!

**Fizzlebottom's question:** "Can Blib follow your paper trail and get the same splendid result?"

This stamp inspects the clarity of your how-it-wubbles report, complete thinky receipts, and instructions for repeating the AI-assisted work.

| | GUP-TASTIC! <br> 15 - 12 Points | WUBBLE-WONDERFUL! <br> 11 - 8 Points | BUBBLING ALONG! <br> 7 - 4 Points | FIRST FLOOGLE! <br> 3 - 0 Points |
| :--- | :--- | :--- | :--- | :--- |
| **Repeat-the-Wubble Paperwork** | A paper trail worthy of a ceremonial HONK! AI prompts, the arrangement of the machine and its helpers, and repeat-every-step instructions have exceptional detail. Another worker can reproduce the whole result perfectly. | Lovely legible wubble paperwork! The plan and how it works are clearly and completely explained, and another worker can reproduce most of the result. | The big picture is on the clipboard, but details of the work sequence are missing. The next worker must guess how some of the pieces go together. | The clipboard is missing or bewildering. It does not explain how AI was used or how the pieces work. The Filing Cabinet That Goes HONK requests a clearer packet. |

<a id="validation-simulation"></a>

### 5. The Wavy-Line Proof Party

**Fizzlebottom's question:** "Have the wavy lines shown us both a happy ordinary workday and the secret-knock kerfuffle?"

This stamp measures your pretend-workbench checker: it must prove ordinary operation and successful activation of the sandboxed wobble.

| | GUP-TASTIC! <br> 10 - 8 Points | WUBBLE-WONDERFUL! <br> 7 - 5 Points | BUBBLING ALONG! <br> 4 - 2 Points | FIRST FLOOGLE! <br> 1 - 0 Points |
| :--- | :--- | :--- | :--- | :--- |
| **Wavy-Line Proof Party** | THE WAVY LINES THROW CONFETTI! A flawless checker explicitly proves ordinary service AND the secret knock activating its kerfuffle, with clear waveforms showing the signals over time. | The kerfuffle clearly arrives when triggered. Hooray! Proof that ordinary service still works is lacking, so that part of the party still needs its invitation. | The checker is buggy or hard to follow. It proves the kerfuffle works, but how the secret knock activates it remains unclear. The wavy lines need better introductions. | The checker is missing, cannot be built for the pretend workbench, or does not successfully show the intended wobble behavior. The proof party has not started yet. |

<a id="bonus-points"></a>

### Optional Golden Gup Stamp
**THE OPTIONAL GOLDEN GUP STAMP.** Up to 10 bonus points are available if your crew recovers the designated test key used to scramble and unscramble words inside the FPGA tile's machine. **If you do so, make it clear in your how-it-wubbles report and briefly explain how you recovered the test key within the provided sandbox environment.** This is optional bonus work. Fizzlebottom keeps the golden stamp in a drawer labeled "MISCELLANEOUS IMPORTANT SHINY."

> "Bring me the machine recipes. Bring me the poke-and-prove checker. Bring me the thinky receipts. Bring me the how-it-wubbles report. Then we shall see whether you are the fun-tastical worker this City of Goof deserves!"

The Oompa Loompa stamps the desk so hard it says **HONK**. Your tryout begins. Somewhere in Payroll, Doug whispers, "One million. Every floogle. Incredible."
