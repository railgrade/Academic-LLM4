# Open Source LLMs

Table of Contents

- [Pretrained Model](#pretrained-model)
- [Multitask Supervised Finetuned Model](#multitask-supervised-finetuned-model)
- [Instruction Finetuned Model](#instruction-finetuned-model)
  - [English](#english)
  - [Chinese](#chinese)
  - [Multilingual](#multilingual)
- [Human Feedback Finetuned Model](#human-feedback-finetuned-models)
- [Domain Finetuned Model](#domain-finetuned-model)
- [Open Source Projects](#open-source-projects)
  - [reproduce/framework](#reproduceframework)
  - [accelerate](#accelerate)
  - [evaluation](#evaluation)
  - [deployment/demo](#deploymentdemo)
- [Reference](#reference)

notes:

1. *Date: YY/MM, All projects are sorted by first proposed date*
2. *Dec=Decoder; Enc=Encoder; CTX=Context Length; WD=Window Length*
3. *We provide Huggingface (HF) checkpoint by default*

## Pretrained Model

| Model                        | Available Size                                                                                                                                                                                                                                                                                                                                                                                                                               | CTX   | Architecture | Training Data                                                                                                                                                                                     | Link                                                                                                                                                                                                      | Date  | Affiliation  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------ |
| Yi                           | [6B](https://huggingface.co/01-ai/Yi-6B)/[34B](https://huggingface.co/01-ai/Yi-34B)                                                                                                                                                                                                                                                                                                                                                                | 4K WD | Dec          | ?                                                                                                                                                                                                 | [code](https://github.com/01-ai/Yi)                                                                                                                                                                          | 11/23 | 01AI         |
| Skywork                      | [7B](https://huggingface.co/Skywork/Skywork-13B-Base)/[13B](https://huggingface.co/datasets/Skywork/SkyPile-150B)                                                                                                                                                                                                                                                                                                                                  | 4K    | Dec          | self-construct (500B/2TB/3.1TB tokens, Chinese&English)                                                                                                                                          | [code](https://github.com/SkyworkAI/Skywork)                                                                                                                                                                 | 10/23 | SkyworkAI    |
| Mistral                      | [7B](https://huggingface.co/mistralai/Mistral-7B-v0.1)                                                                                                                                                                                                                                                                                                                                                                                          | 4K WD | Dec          | ?                                                                                                                                                                                                 | [code](https://github.com/mistralai/mistral-src), [blog](https://mistral.ai/news/announcing-mistral-7b/)                                                                                                        | 09/23 | Mistral AI   |
| XVERSE                       | [13B](https://huggingface.co/xverse/XVERSE-13B)                                                                                                                                                                                                                                                                                                                                                                                                 | 8K    | Dec          | self-construct (1.4T tokens, Multilingual)                                                                     