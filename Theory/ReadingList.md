# LLM Reading

Table of Contents

- [Key Findings](#key-findings)

*arranged in alphabetical order*

- [Architecture](#architecture)
- [Instruction Tuning](#instruction-tuning)
- [In Context Learning](#in-context-learning)
- [Mixture of Experts (MoE)](#mixture-of-experts-moe)
- [Reasoning](#reasoning)
  - [Abstract Reasoning](#abstract-reasoning)
  - [Chain of Thought](#chain-of-thought)

## Key Findings

| Title                                                                 | Pub       | Preprint                                                                                                                                                                                                                                                                                               | Supplementary                      |
| --------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| RWKV: Reinventing RNNs for the Transformer Era                        |           | [2305.13048](https://arxiv.org/abs/2305.13048)          <br />   ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F026b3396a63ed5772329708b7580d633bb86bec9%3Ffields%3DcitationCount&query=%24.citationCount&label=citation) | RWKV, Blink                        |
| Self-Instruct: Aligning LM with Self Generated Instructions           | ACL 2023  | [2212.10560](https://arxiv.org/abs/2212.10560)        <br />   ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fe65b346d442e9962a4276dc1c1af2956d9d5f1eb%3Ffields%3DcitationCount&query=%24.citationCount&label=citation)   | self-instruct, UW                  |
| Emergent Abilities of Large Language Models                           | TMLR 2022 | [2206.07682](https://arxiv.org/abs/2206.07682)  <br />   ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fdac3a172b504f4e33c029655e9befb3386e5f63a%3Ffields%3DcitationCount&query=%24.citationCount&label=citation)         | emergent ability,  Google         |
| Training language models to follow instructions with human feedback   |           | [2203.02155](https://arxiv.org/abs/2203.02155)  <br /> ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fd766bffc357127e0dc86dd69561d5aeb520d6f4c%3Ffields%3DcitationCount&query=%24.citationCount&label=citation)           | InstructGPT, OpenAI                |
| Chain-of-Thought Prompting Elicits Reasoning in Large Language Models |           | [2201.11903](https://arxiv.org/abs/2201.11903)   <br /> ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1b6e810ce0afd0dd093f789d2b2742d047e316d5%3Ffields%3DcitationCount&query=%24.citationCount&label=citation)          | CoT, Google                        |
| Finetuned Language Models Are Zero-Shot Learners