# Instruction tuning

Table of Contents

- [Experiments](#experiments)
  - [Datasets](#datasets-1)
    - [Collection](#collected-instructions)
    - [Bootstrap](#bootsrap-instructions)
  - [Model Cards](#model-cards)
  - [Usage](#usage)
- [Results](#results)

## Experiments

### Datasets

#### Collected Instructions

We collect 1M **Multilingual** instruction datasets for experiments, including:

- Chinese: [Belle](https://github.com/LianjiaTech/BELLE), [Alpaca_Chinese](https://github.com/LC1332/Chinese-alpaca-lora/blob/main/data/trans_chinese_alpaca_data.json), [Guannaco](https://guanaco-model.github.io/)
- English: [Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Guannaco](https://guanaco-model.github.io/)
- Deutsch: [Guannaco](https://guanaco-model.github.io/)

#### Bootsrap Instructions

to construct instruction manually, we follow [self-instruct](https://github.com/yizhongw/self-instruct), and [stanford_alpaca](https://github.com/tatsu-lab/stanford_alpa