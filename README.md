# Language-Modeling
- a neural network for character-level language modeling.
-----------------------------------------------------------------------------
### Dataset
* Shakespeare
------------------------------------------------------------------------------
### Comparing Loss
#### Training Loss
![training_loss_plot](https://github.com/Day-bi/Language-Modeling/assets/73453720/ca514d71-1aed-4652-9f02-208152b18af8)
- **RNN**: 초기 손실 1.6에서 시작해 천천히 감소, 에포크 20에서 1.3에 수렴.
- **LSTM**: 초기 손실 1.7에서 시작해 빠르게 감소, 에포크 20에서 0.9에 수렴. RNN보다 더 빠르고 낮은 손실 값 보임.

#### Validation Loss
![validation_loss_plot](https://github.com/Day-bi/Language-Modeling/assets/73453720/6d693365-077a-4802-a6d3-00016bce593b)
- **RNN**: 초기 손실 1.4에서 시작해 점진적으로 감소, 에포크 20에서 1.3에 수렴.
- **LSTM**: 초기 손실 1.4에서 시작해 빠르게 감소, 에포크 20에서 0.9에 수렴. RNN보다 더 나은 성능 보임.

#### Conclusion
- **LSTM 모델 우수**: 학습 및 검증 손실에서 RNN보다 성능 우수. 빠르고 낮은 손실 값 도달.
- **RNN 모델 한계**: 일정 에포크 이후 손실 감소 둔화. 복잡한 패턴 학습에 한계.
- **LSTM 강점**: 더 낮은 손실로 수렴, 복잡한 시퀀스 학습에 유리.
------------------------------------------------------------------------------
### Comparing generated text
* T = 1
  * RNN
      * QUEEN ELIZABETH:zecreed, siring in their general intering the chargine are what our voices. The gods long, as he las
  * LSTM
      * zarent That more to good clute. First Murderer:
      Why, this such a coverture Rome,
      Or bitterly to thy
* T = 10
  * RNN
      * QUEEN ELIZABETH:zin,'d!VCw;
Q-y
VSnUSurwW
Gtb!lwcRjGgcumnw'tapisevn'smk kGxKr!-Watr'ti-g;!UVywyA,YviWvIdj;x evcoOGrS

  * LSTM
      * QUEEN ELIZABETH:z
ipWleaFlyin, ALYuoj. b;d'Neek.
S;il
k'NaMq
bHCafitgpi.
iPboys, Divinct,hPe-Saa-tDbsKEumugh.
O fgBo
