# Sillytastic Working Challenge
 [![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

Welcome to Silly Land, fun-tastical worker! The City of Goof has assigned you a very important job: make its little corner of the hardware world as fun-tastically-safe as possible. Your hard hat is imaginary. Your evidence must be real.

This is a themed working copy of the **NYU CSAW 2026 AI Hardware Attack (AHA!) Challenge**, adapted from [JBlocklove's challenge repository](https://github.com/JBlocklove/CSAW-AI-Hardware-Attack-Challenge-2026). The City of Goof is our fictional setting; the CSAW challenge requirements, technical interfaces, deliverables, and scoring rubric still govern the work. This edition changes the documentation's presentation and the reference script's comments.

## Your Job in the City of Goof

Goof's safety department needs a work crew that can use generative AI to insert **sandboxed hardware security modifications** into FPGA-targeted designs and demonstrate controlled security probings for those modifications within the competition environment. Understanding and validating that behavior is your fun-tastical assignment.

Your workbench is the **Hackster board from Calico Computer**, an education-focused device with an application microprocessor, an FPGA, and peripherals for hardware security education. Teams must reverse-engineer its provided FPGA bitstream, use the integration documentation and tests to understand the design, and add a sandboxed hardware security modification. The qualifying round happens entirely in simulation.

The first shift runs for two weeks, **18 September to 2 October 2026**. Finalists are selected by **4 October** and brought to New York for CSAW in person. The final challenge is given at CSAW and takes place over **24 hours**, with physical Hackster boards available to demonstrate preliminary vulnerabilities and complete the final hardware challenge.

**Clock in your crew:** [Register for the challenge](https://forms.gle/U9jf9WYuRjpdJjvZ7).

**Begin your first shift:** [Open the preliminary challenge work order](qualifier/README.md).

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Your Worker Handbook](#general-guidelines)
  - [The City Calendar](#timeline)
  - [Assemble Your Work Crew](#teams)
  - [The Town Noticeboard](#communication)
  - [Your AI Workshop](#ai-usage)
- [First Shift: Preliminary Phase](#preliminary-phase)
- [The Big Goof: Finals at CSAW](#finals)
- [Stock Your Toolbox](#getting-started)
- [Meet the Hackster](#hackster-board)
- [Credit Where Goof Is Due](#credits)

<a id="general-guidelines"></a>

## Your Worker Handbook

A fun-tastical worker keeps the job requirements close and the confetti clear of the circuitry.

<a id="timeline"></a>

### The City Calendar

All dates below are for the 2026 challenge. Put them on the municipal fridge:

- 18 September: Preliminary Phase Launch
- 02 October: Preliminary Phase Submission Deadline
- 04 October: Finalists Notified
- 12 November: Final Challenge Released @ CSAW
- 14 November: Final Challenge Deadline & Presentations @ CSAW
- 15 November: Winners Announced @ CSAW

*Note: There is no registration deadline. Teams can register and submit up until the preliminary phase submission deadline.*

<a id="teams"></a>

### Assemble Your Work Crew

Every City of Goof work crew must consist of:

- Up to four currently enrolled students (graduate or undergraduate).
- One advisor (a graduate student advising an undergraduate team, or a professor advising a graduate team).

<a id="communication"></a>

### The Town Noticeboard

The challenge Discord is your town noticeboard. Most communications about this and future competitions happen there. [Join the official server](https://discord.gg/KEVbWs6BPU) to keep your crew in the loop.

<a id="ai-usage"></a>

### Your AI Workshop

Generative AI is a central part of your work crew. This competition requires significant use of it, and the city's paperwork department needs the complete record: keep detailed logs of **every interaction with AI** and include them in every submission. **If a submission is made without logs or the logs are missing key information, the submission may be disqualified.**

For the preliminary challenge, the hardware security modification and its validation procedure must be written fully with AI. **No hardware may be written by human users.** See the [work order](qualifier/README.md#the-challenge) for the full requirements, including the mandatory transcripts.

<a id="preliminary-phase"></a>

## First Shift: Preliminary Phase

The preliminary phase launches on **18 September**. Your [first-shift work order](qualifier/README.md) contains the simulation-only challenge, required deliverables, submission link, and complete judging rubric. Start there, worker: the City of Goof needs reproducible results.

<a id="finals"></a>

## The Big Goof: Finals at CSAW

Finals take place at **NYU during CSAW, November 12 - 14**. Details of this phase will be released once finalists are selected. The physical Hackster boards join your workbench for the final challenge.

<a id="getting-started"></a>

## Stock Your Toolbox

A good worker brings tools, not just an impressively wobbly clipboard. The challenge recommends the [Yosys OSS CAD Suite](https://github.com/YosysHQ/oss-cad-suite-build) for the Hackster board. It includes:

- Icarus Verilog
- GTKWave
- Yosys
- IceStorm

These tools are optional, not a requirement. The Hackster was designed to work with open-source tooling like this suite.

During the first phase, teams **will not have access to a physical Hackster board**. Your shift is in simulation, but the [Hackster setup documentation](https://cgi.cse.unsw.edu.au/~cs6420/labs/lab00introduction/) can help you understand the board's connections and its setup with the OSS CAD Suite. The [hackster-programmer repository](https://github.com/kiwih/hackster-programmer) provides additional information, including PCB schematics.

<a id="hackster-board"></a>

## Meet the Hackster

The City of Goof's workbench has a proper technical name: the *Hackster*, a hardware security learning platform from Calico Computer designed by **Dr. Hammond Pearce**. Its components are:

- An application processor: [RP2040](https://www.raspberrypi.com/products/rp2040/).
- A programming processor: RP2040.
- An FPGA: [Lattice iCE40-UP5K](https://www.latticesemi.com/en/products/fpgaandcpld/ice40ultraplus).
- Additional circuitry and components for side-channel power analysis.

<a id="credits"></a>

## Credit Where Goof Is Due

This themed edition retains the source challenge's [CC BY-NC 4.0 license](LICENSE). The original challenge is the [NYU CSAW 2026 AI Hardware Attack Challenge](https://github.com/JBlocklove/CSAW-AI-Hardware-Attack-Challenge-2026); the Silly Land setting and worker-themed wording are adaptations for this working repository.

The Hackster hardware is under the CC BY-SA 4.0 license. Any use of the hardware documentation (such as the schematic) or the gerber files for the Hackster should be attributed as follows:

"Hammond Pearce, UNSW Sydney - CC BY-SA 4.0"

Now pick up your clipboard, fun-tastical worker. [The first shift is waiting.](qualifier/README.md)

